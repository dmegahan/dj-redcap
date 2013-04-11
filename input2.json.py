class Demographics(models.Model):
    study_id = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Study ID', blank=True)
    gender = models.IntegerField(help_text='', null=True, verbose_name='Gender', blank=True, choices=[(0, 'Female'), (1, 'Male'), (2, 'Other')]) # This field type is a guess
    other_gender = models.IntegerField(help_text='Newborn Screening LTFU', null=True, verbose_name='Other gender | Please specify $placeholder gender', blank=True, choices=[(1, 'Not tested'), (2, 'XX genotype/Female'), (3, 'XY genotype/Male'), (4, "XXY Klinefelter's Syndrome"), (5, "XO Turner's Syndrome"), (6, 'XXXY syndrome'), (7, 'XXYY syndrome'), (8, 'Mosaic including XXXXY'), (9, 'Penta X syndrome'), (10, 'XYY'), (11, 'Unknown'), (12, 'Other')]) # This field type is a guess
    year_of_birth = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Year of birth (XXXX)', blank=True)
    ethnicity = models.IntegerField(help_text='', null=True, verbose_name='Ethnicity', blank=True, choices=[(1, 'Non-Hispanic'), (2, 'Hispanic or Latino'), (3, 'Unknown')]) # This field type is a guess
    ethnicity_followup = models.IntegerField(help_text='', null=True, verbose_name='Ethnicity follow-up', blank=True, choices=[(1, 'Ashkenazi Jewish'), (2, 'Amish'), (3, 'French Canadian'), (4, 'None of the above'), (5, 'Unknown')]) # This field type is a guess
    race = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Race', choices=[(1, 'White'), (2, 'Black or African American'), (3, 'American Indian or Alaska Native'), (4, 'Native Hawaiian or Other Pacific Islander'), (5, 'Asian'), (6, 'More than one race'), (7, 'Unknown or Not reported')])
    demographics_feedback = models.TextField(help_text='', null=True, verbose_name='Please provide any feedback for this form (for example: missing questions, questions not relevant for a disease area, ambiguities, places where a textbox could be replaced with discrete choices, missing discrete choices)', blank=True) # This field type is a guess

    class Meta:
	 db_table = 'demographics'


class PediseqStudyId(models.Model):
    family_code = models.FloatField(help_text='', null=True, verbose_name='Family Code', blank=True)
    family_member_code = models.CharField(help_text='P - Proband, S - Sibling, M - Mother, F - Father', null=True, max_length=2000, verbose_name='Family Member', blank=True)
    other_family_member = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Other family member', blank=True)
    affected_status = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Affected Status', blank=True)
    validation_or_prospective = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Validation or Prospective', blank=True)

    class Meta:
	 db_table = 'pediseq_study_id'


class StudyIds(models.Model):
    original_study_id = models.CharField(help_text="Enter the subject's ID from the original consenting study (HLS, Mito, etc.)", null=True, max_length=2000, verbose_name='Original Study ID', blank=True)
    discarded_clinical = models.NullBooleanField(help_text='', verbose_name='Discarded Clinical Specimen?', blank=True)

    class Meta:
	 db_table = 'study_ids'


class BirthHistory(models.Model):
    birthweight = models.TextField(help_text='Please indicate out to one decimal place unless units are lbs. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Birthweight', blank=True) # This field type is a guess
    birth_length = models.TextField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Birth length', blank=True) # This field type is a guess
    birth_head_circumference = models.FloatField(help_text='Please indicate out to one decimal place. Please round up to the nearest tenth if the hundredth position is 5 or higher. ', null=True, verbose_name='Birth head circumference (cm)', blank=True)
    gestational_age_wks = models.IntegerField(help_text='Specify partial week in days below. If full term but exact month and days are unknown, specify 40 weeks and 0 days.', null=True, verbose_name='Gestational age full weeks', blank=True)
    gestational_age_days = models.IntegerField(help_text='', null=True, verbose_name='Gestation age days', blank=True)
    mother_birth_age = models.CharField(help_text='Please round up if the age is 6 months or more into the current year.', null=True, max_length=2000, verbose_name="Mother's age when child was born (years)", blank=True)
    gravida = models.IntegerField(help_text='', null=True, verbose_name='Gravida\\n(Number of prior gestations including proband)', blank=True)
    para = models.IntegerField(help_text='', null=True, verbose_name='Para\\n(Number of live births including the proband)', blank=True)
    assisted_reproduction_bool = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Was any type of assisted reproduction (for example sperm donation, in vitro fertilization) used in the pregnancy for this child?', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    assisted_reproduction_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Please specify type of assisted reproduction', blank=True)
    prior_pregnancy_history = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Did the mother have any of the following', blank=True)
    miscarriages_no = models.IntegerField(help_text='', null=True, verbose_name='Number of spontaneous miscarriages', blank=True)

    class Meta:
	 db_table = 'birth_history'


