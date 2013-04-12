class Genepanel(models.Model):
    gene_panel = models.CharField(help_text='For example, cardiomyopathy panel or hearing loss panel', null=True, max_length=2000, verbose_name='Name of $s gene panel performed', blank=True)
    panel${d}_laboratory = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Which laboratory performed $s gene panel?', blank=True)
    panel${d}_date_performed = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year $s panel was performed', blank=True)
    panel${d}_result_type = models.IntegerField(max_length=2000, blank=True, help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name='Indicate ALL types of results identified on panel. ', choices=[(1, 'Positive - disease-causing mutation identified'), (2, 'Negative - no definite/possible disease-causing mutation identified'), (3, 'Variant of uncertain significance'), (4, 'Polymorphism'), (5, 'Results pending'), (6, 'Results not known')])
    panel${d}_list_gene = models.IntegerField(max_length=2000, blank=True, help_text='Optional', null=True, verbose_name='Would you like to list the genes that were on the panel?', choices=[(1, 'Yes'), (2, 'No')])
    panel${d}_list_gene_entry = models.CharField(help_text='Example: PTPN11, HRAS, SOS1', null=True, max_length=2000, verbose_name='List genes on this panel (Separate with commas)', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'GenePanel'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    prior_genetic_testing = models.ForeignKey(prior_genetic_testing)

    class Meta:
	 db_table = 'DCM'


class Genepanel(models.Model):
    gene_panel = models.CharField(help_text='For example, cardiomyopathy panel or hearing loss panel', null=True, max_length=2000, verbose_name='Name of $s gene panel performed', blank=True)
    panel${d}_laboratory = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Which laboratory performed $s gene panel?', blank=True)
    panel${d}_date_performed = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year $s panel was performed', blank=True)
    panel${d}_result_type = models.IntegerField(max_length=2000, blank=True, help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name='Indicate ALL types of results identified on panel. ', choices=[(1, 'Positive - disease-causing mutation identified'), (2, 'Negative - no definite/possible disease-causing mutation identified'), (3, 'Variant of uncertain significance'), (4, 'Polymorphism'), (5, 'Results pending'), (6, 'Results not known')])
    panel${d}_list_gene = models.IntegerField(max_length=2000, blank=True, help_text='Optional', null=True, verbose_name='Would you like to list the genes that were on the panel?', choices=[(1, 'Yes'), (2, 'No')])
    panel${d}_list_gene_entry = models.CharField(help_text='Example: PTPN11, HRAS, SOS1', null=True, max_length=2000, verbose_name='List genes on this panel (Separate with commas)', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'GenePanel'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    prior_genetic_testing = models.ForeignKey(prior_genetic_testing)

    class Meta:
	 db_table = 'DCM'


class Genepanel(models.Model):
    gene_panel = models.CharField(help_text='For example, cardiomyopathy panel or hearing loss panel', null=True, max_length=2000, verbose_name='Name of $s gene panel performed', blank=True)
    panel${d}_laboratory = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Which laboratory performed $s gene panel?', blank=True)
    panel${d}_date_performed = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year $s panel was performed', blank=True)
    panel${d}_result_type = models.IntegerField(max_length=2000, blank=True, help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name='Indicate ALL types of results identified on panel. ', choices=[(1, 'Positive - disease-causing mutation identified'), (2, 'Negative - no definite/possible disease-causing mutation identified'), (3, 'Variant of uncertain significance'), (4, 'Polymorphism'), (5, 'Results pending'), (6, 'Results not known')])
    panel${d}_list_gene = models.IntegerField(max_length=2000, blank=True, help_text='Optional', null=True, verbose_name='Would you like to list the genes that were on the panel?', choices=[(1, 'Yes'), (2, 'No')])
    panel${d}_list_gene_entry = models.CharField(help_text='Example: PTPN11, HRAS, SOS1', null=True, max_length=2000, verbose_name='List genes on this panel (Separate with commas)', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'GenePanel'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    prior_genetic_testing = models.ForeignKey(prior_genetic_testing)

    class Meta:
	 db_table = 'DCM'


class Genepanel(models.Model):
    gene_panel = models.CharField(help_text='For example, cardiomyopathy panel or hearing loss panel', null=True, max_length=2000, verbose_name='Name of $s gene panel performed', blank=True)
    panel${d}_laboratory = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Which laboratory performed $s gene panel?', blank=True)
    panel${d}_date_performed = models.FloatField(help_text='Please specify four digit year', null=True, verbose_name='Year $s panel was performed', blank=True)
    panel${d}_result_type = models.IntegerField(max_length=2000, blank=True, help_text='For example, if testing showed both a disease-causing mutation and a polymorphism, check positive and polymorphism.', null=True, verbose_name='Indicate ALL types of results identified on panel. ', choices=[(1, 'Positive - disease-causing mutation identified'), (2, 'Negative - no definite/possible disease-causing mutation identified'), (3, 'Variant of uncertain significance'), (4, 'Polymorphism'), (5, 'Results pending'), (6, 'Results not known')])
    panel${d}_list_gene = models.IntegerField(max_length=2000, blank=True, help_text='Optional', null=True, verbose_name='Would you like to list the genes that were on the panel?', choices=[(1, 'Yes'), (2, 'No')])
    panel${d}_list_gene_entry = models.CharField(help_text='Example: PTPN11, HRAS, SOS1', null=True, max_length=2000, verbose_name='List genes on this panel (Separate with commas)', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'GenePanel'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    genepanel = models.ForeignKey(GenePanel)

    class Meta:
	 db_table = 'DCM'


class Gene(models.Model):
    gene_result = models.CharField(help_text='Example: GNE1', null=True, max_length=2000, verbose_name='$s gene tested on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'Gene'


class Dcm(models.Model):
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='Change at cDNA level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    change${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='Change at protein level for $s disease-causing mutation on $s2 gene on $s1 gene panel ', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_dna_level = models.CharField(help_text='Example c.33C>G', null=True, max_length=2000, verbose_name='$s variant of unknown significance at cDNA level on $s2 gene on $s1 gene panel', blank=True)
    vus${d}_at_protein_level = models.CharField(help_text='Example: p.Ala11Tyr', null=True, max_length=2000, verbose_name='$s variant of unknown significance at protein level on $s2 gene on $s1 gene panel', blank=True)
    gene = models.ForeignKey(Gene)

    class Meta:
	 db_table = 'DCM'


