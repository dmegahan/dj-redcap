import csv
import json
import keyword
import sys

header_keys = (
	'field_name',
	'form_name',
	'section_name',
	'field_type',
	'field_label',
	'choices',
	'field_note',
	'validation_type',
	'min_value',
	'max_value',
	'is_identifier',
	'branching_logic',
	'required',
	'custom_alignment',
	'question_number',
)

field_types = {
	'date_ymd': 'DateField',
	'number': 'FloatField',
	'integer': 'IntegerField',
	'email': 'EmailField',
	'text': 'CharField',
	'textarea': 'TextField',
	'calc': 'FloatField',
	'radio': 'CharField',
	'select': 'CharField',
	'checkbox': 'CharField',
	'yesno': 'BooleanField',
	'truefalse': 'BooleanField',
}
def readFile(fileName=None):
	if not fileName:
		fileName = raw_input('Enter a valid filename: ');
	
	fin = open(fileName);
	dialect = csv.Sniffer().sniff(fin.read(1024));
	fin.seek(0);
	reader = csv.DictReader(fin, fieldnames=header_keys,dialect=dialect);
	
	reader.next();
	if fileName.find('.json') == -1:
		fileName = csv2json(reader, fileName);
	json2dj(fileName);
def csv2json(reader, fileName):
	"""
		Function that converts csv file to valid json. 
	"""
	fout = open(fileName + '.json', "w+");
	
	repeat_num_stack = [];
	repeat_rows_list = [];
	last_form_name = None;
	cur_depth = 1;
	for row in reader:
		form_name = row['form_name'];
		"""
		Needed for special case csv's with repeats used, not needed otherwise.
		Determines if a field_name has startrepeat,repeat,or endrepeat in it,
		then extracts the number of repeats and the field it refers to.
		"""
		if row['field_name'].find('startrepeat') != -1:
			repeat_info = row['field_name'].strip().split();
			row['field_name'] = repeat_info[0];
			#repeat_num = repeat_info[2];
			#repeat_pointer = ' '.join(repeat_info[3:]);
			#row['form_name'] = repeat_pointer;
			
			repeat_rows_list = last_inner_append(repeat_rows_list, [row],0,cur_depth);
			repeat_num_stack.append(repeat_info[2]);
			cur_depth = cur_depth + 1;
		elif row['field_name'].find('endrepeat') != -1:
			row['field_name'] = row['field_name'].strip().split()[0];
			#repeat_num = cur_repeat_num;
			#repeat_pointer = cur_repeat_pointer;
			#row['form_name'] = repeat_pointer;
			
			repeat_rows_list = last_inner_append(repeat_rows_list, row,0,cur_depth);
			cur_depth = cur_depth - 1;
			repeat_rows_list = last_inner_append(repeat_rows_list,'',0,cur_depth);
		elif row['field_name'].find(' repeat ') != -1:
			repeat_info = row['field_name'].strip().split();
			row['field_name'] = repeat_info[0];
			#repeat_num = repeat_info[2];
			#repeat_pointer = ' '.join(repeat_info[3:]);
			
			repeat_num_stack.append(repeat_info[2]);
			repeat_rows_list = last_inner_append(repeat_rows_list, [row],0,cur_depth);
			cur_depth = cur_depth - 1;
			repeat_rows_list = last_inner_append(repeat_rows_list,'',0,cur_depth);
			#row['form_name'] = repeat_pointer;
		elif repeat_num_stack:
			#row['form_name'] = repeat_pointer;
			
			repeat_rows_list = last_inner_append(repeat_rows_list, row,0,cur_depth);
	print_list(repeat_num_stack,repeat_rows_list,fout,-1,);
	return fout.name;

def print_list(num_repeats,repeats_list,fout,num_repeats_index):
	"""Recursive method for generating the json for a list of lines that use repeats.
	The function iterates through the list, generating the json for each dictionary it encounters.
	When it finds another list, this function is recursively called on that list and does the same. The
	function uses num_repeats and num_repeats_index to keep track of how many iterations it should do for each list, nested
	or not.
	"""
	for i in range(int(num_repeats[num_repeats_index])):
		for j,item in enumerate(repeats_list):
			if isinstance(repeats_list[j],list):
				print_list(num_repeats,item,fout,num_repeats_index+1);
			elif repeats_list[j] == '':
				repeats_list.pop(j);
			else:
				fout.write(generateJson(item));
				fout.write('\n');

def last_inner_append(x,y,curDepth,depth):
	"""Finds the deepest index in a list, that is not a list itself. If a list is 
	found, the function is called recursively on that list.
	"""
	try:
		if(curDepth != depth):
			if isinstance(x[-1],list):
				curDepth = curDepth + 1;
				last_inner_append(x[-1],y,curDepth,depth);
				return x;
	except IndexError:
		pass;
	x.append(y);
	return x;

def generateJson(row):
	return (json.dumps({'form':
                                        {'form name': row['form_name'],
                                        'section header': row['section_name'],
                                        'field':
                                        {'field name': row['field_name'],
                                         'field label': row['field_label'],
                                         'field note': row['field_note'],
                                         'type':
                                                {'field type': row['field_type'],
                                                 'choices': row['choices']},
                                         'text validation':
                                                {'validation type': row['validation_type'],
                                                 'min value': row['min_value'],
                                                 'max value': row['max_value']},
                                         'identifier': row['is_identifier'],
                                         'branching logic': row['branching_logic'],
                                         'required?': row['required'],
                                         'alignment': row['custom_alignment'],
                                         'question number': row['question_number'],
                                        },},},indent=0, separators=(',',':')));	

def json2dj(fileName):
	form2model = lambda form_name: form_name.title().replace('_','').replace(' ','').replace('-','');
	
	fout = open(fileName + '.py', 'w+');

	prev_form_name = None
	
	for line in open(fileName,'r'):
		form_name = get_field_value(line, 'form name');
		#if statement checks for endrepeats so a new class isn't created when one is found
		if form_name != prev_form_name and get_field_value(line,'field name').strip().replace('_','') != 'endrepeat':
			if prev_form_name:
				for meta_line in get_meta(prev_form_name):
					fout.write(meta_line);
			prev_form_name = form_name;
			fout.write('class %s(models.Model):' % form2model(form_name));
			fout.write('\n');
			
		column_name = get_field_value(line, 'field name');
		att_name = column_name.lower();
		comment_notes = [];
		extra_params = {};

		extra_params['verbose_name'] = get_field_value(line, 'field label');
		
		extra_params['help_text'] = get_field_value(line, 'field note');
		
		if ' ' in att_name or '-' in att_name or keyword.iskeyword(att_name) or column_name != att_name:
			extra_params['db_column'] = column_name;
		
		if ' ' in att_name:
			att_name = att_name.replace(' ','_');
			comment_notes.append('Field renamed to remove spaces.');
		if '-' in att_name:
			att_name = att_name.replace('-','_');
			comment_notes.append('Field renamed to remove dashes.');
		if column_name != att_name:
			comment_notes.append('Field name made lowercase.');
	
		field_type, field_params, field_notes = get_field_type(line);
		extra_params.update(field_params);
		comment_notes.extend(field_notes);
		
		field_type += '('

		if keyword.iskeyword(att_name):
			att_name += '_field';
			comment_notes.append('Field renamed because it was a Python reserved word.');
		if att_name[0].isdigit():
			att_name = 'number_%s' % att_name;
			extra_params['db_column'] = unicode(column_name);
			comment_notes.append("Field renamed because it wasn't a valid python identifier.");
		
		if att_name == 'id' and field_type == 'AutoField(' and extra_params == {'primary_key': True}:
			continue
		field_desc = '%s = models.%s' % (att_name, field_type);
		if extra_params:
			if not field_desc.endswith('('):
				field_desc += ', ';
			field_desc += ', '.join(['%s=%r' % (k, v) for k, v in extra_params.items()])
		field_desc += ')';
		if comment_notes:
			field_desc += ' # ' + ' '.join(comment_notes);
		
		fout.write('    %s\n' % field_desc);
	#final meta class
	for meta_line in get_meta(form_name):
		fout.write(meta_line);
def get_field_type(line):
	"""Given the database connection, the table name, and the cursor row description,
	this routine will return the given field type name, as well as any additional keyword
	parameters and notes for the field.
	"""
	field_params = {};
	field_notes = [];
	
	required = get_field_value(line,'required?');
	validation_type = get_field_value(line,'validation type');
	field_type = get_field_value(line,'field type');

	try:
		field_type = field_types.get(validation_type, field_types[field_type]);
	except KeyError:
		field_type = 'TextField';
		field_notes.append('This field type is a guess');
	if not required:
		field_params['blank'] = True
		if field_type is 'BooleanField':
			field_type = 'NullBooleanField';
		else:
			field_params['null'] = True;
	if field_type == 'CharField':
		field_params['max_length'] = 2000;

	choices = None;
	if get_field_value(line,'choices'):
		try:
			choices = [(int(v.strip()), k.strip()) for v, k in [choice.split(',') \
				for choice in get_field_value(line,'choices').split('|')]]
			field_type = 'IntegerField'
		except (ValueError, TypeError):
			pass
	
	if choices:
		field_params['choices'] = choices;
	
	return field_type, field_params, field_notes;
def get_field_value(line, field):
	"""
		Determines the value of a field from the json representation.
		
		This function first finds the begining of the field name (not the value).
		Then adds the length of the field to the index, and then adds another 3 to it. 
		The additional 3 come from the way the Json is structured. A typical Json 'field' 
		looks like this example: "identifier":"some_value". The added 3 index comes from 
		the second quotation mark, the colon, and the third quotation.
		
		Then finds the length of the field_value and returns that substring using the determined indices.
	"""
	field_index = line.find('"' + field + '"');
	field_index = field_index + len(field) + 4;
	current_char = line[field_index];
	field_len = 0;
	while current_char != '"':
		field_len += 1;
		current_char = line[field_index+field_len];
	field_value = line[field_index:field_index+field_len];
	return field_value;	
def get_meta(table_name):
	"""	Return a sequence comprising the lines of code necessary
		to construct the inner Meta class for the model 
		corresponding to the given database table name.
	"""
	return ['\n',
		'    class Meta:\n',
		'	 db_table = %r\n' % table_name,
		'\n',
		'\n'];
if len(sys.argv) > 1:
	readFile(sys.argv[1]);
else:
	readFile();
