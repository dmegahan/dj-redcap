class birth_history(models.Model):
    assisted_reproduction_spec = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Please specify type of assisted reproduction', blank=True)
    prior_pregnancy_history = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Did the mother have any of the following', blank=True)
    miscarriages_no = models.IntegerField(help_text='', null=True, verbose_name='Number of spontaneous miscarriages', blank=True)
    still_births_no = models.IntegerField(help_text='', null=True, verbose_name='Number of still births', blank=True)
    terminations_no = models.IntegerField(help_text='', null=True, verbose_name='Number of terminations', blank=True)
    multiples_no = models.IntegerField(help_text='', null=True, verbose_name='Number of multiple births', blank=True)

    class Meta:
	 db_table = 'birth_history'


