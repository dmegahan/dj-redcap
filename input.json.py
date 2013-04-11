class Demographics(models.Model):
    study_id = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Study ID', blank=True)

    class Meta:
	 db_table = 'demographics'


