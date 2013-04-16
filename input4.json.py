class CardiacFamilyHistory(models.Model):
    cfhx_seizure = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Unexplained seizures', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_drowning = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Near drowning', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_hypertension = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with High blood pressure (Hypertension)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_diabetes = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with Diabetes', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_congen_deaf = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Any blood relatives with congenital deafness (Deaf at birth)', choices=[(1, 'None'), (2, 'Mother'), (3, 'Father'), (4, 'Sister'), (5, 'Brother'), (6, 'Maternal Grandmother'), (7, 'Maternal Grandfather'), (8, 'Paternal Grandmother'), (9, 'Paternal Grandfather'), (10, 'Maternal Aunt'), (11, 'Paternal Aunt'), (12, 'Maternal Uncle'), (13, 'Paternal Uncle'), (14, 'Maternal Cousin'), (15, 'Paternal Cousin'), (16, 'Other')])
    cfhx_explanation = models.TextField(help_text='', null=True, verbose_name='Explain the cardiac family history stated above', blank=True) # This field type is a guess

    class Meta:
	 db_table = 'CardiacFamilyHistory'


class EcgResults(models.Model):
    ecg_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Electrocardiogram done', choices=[(1, 'Yes'), (2, 'No')])
    ecgresults = models.ForeignKey(EcgResults)

    class Meta:
	 db_table = 'EcgResults'


class Ecg(models.Model):
    ecg_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the $s ECG | Other test category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    ecg_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of $s ECG', blank=True)
    ecg_time = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Time of $s ECG', blank=True)
    ecg_ventricular_rate = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ventricular Rate / bpm for $s ECG', blank=True)
    ecg_pr_interval = models.CharField(help_text='', null=True, max_length=2000, verbose_name='PR Interval / msec for $ECG', blank=True)
    ecg_qrs_inter_machine = models.CharField(help_text='', null=True, max_length=2000, verbose_name='QRS Interval / msec  (ECG Computer) for $s ECG', blank=True)
    ecg_qt_inter_machine = models.CharField(help_text='', null=True, max_length=2000, verbose_name='QT Interval / msec   (ECG Computer) for $s ECG', blank=True)
    ecg_qtc_inter_machine = models.CharField(help_text='', null=True, max_length=2000, verbose_name='QTc Interval / msec   (ECG Computer) for $s ECG', blank=True)
    ecg_qtc_inter_manual = models.CharField(help_text='', null=True, max_length=2000, verbose_name='QTc Interval / msec   (Manual Calculation) for $s ECG', blank=True)
    ecg_p_axis_degree = models.CharField(help_text='NOTE: Must use positive numbers. (360 degrees minus X)', null=True, max_length=2000, verbose_name='P axis for $s ECG', blank=True)
    ecg_p_axis_type = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='P Axis Type for $s ECG', choices=[(1, 'Sinus (0 to +90 degree)'), (2, 'LRA (-1 to -90 degree)'), (3, 'HLA (+91 to +180 degree)'), (4, 'LLA (-91 to -179 or +181 to +270 degree)')])
    ecg_qrs_axis_degree = models.CharField(help_text='NOTE: Must use positive numbers. (360 degrees minus X)', null=True, max_length=2000, verbose_name='QRS axis for $s ECG', blank=True)
    ecg_qrs_axis_type = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='QRS Axis Type for $s ECG', choices=[(1, 'Normal'), (2, 'RAD (>+100 degree)'), (3, 'Rightward (+90 to +100 degree)'), (4, 'LAD (negative degree)')])
    ecg_twave_axis_degree = models.CharField(help_text='NOTE: Must use positive numbers. (360 degrees minus X)', null=True, max_length=2000, verbose_name='T wave axis for $s ECG', blank=True)
    ecg_twave_axis_type = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='T wave axis Type for $s ECG', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Wide QRS-T angle')])
    ecg_interp_rhythm = models.IntegerField(max_length=2000, blank=True, help_text='Check all that apply', null=True, verbose_name='$s ECG Interpretation: Predominant Rhythm.  ', choices=[(10, 'None'), (1, 'Normal Sinus Rhythm'), (2, 'Normal Sinus Rhythm with Sinus Arrhythmia'), (3, 'Normal Sinus Rhythm with Sinus Bradycardia'), (4, 'Normal Sinus Rhythm with Sinus Tachycardia'), (5, 'Low Right Atrial Rhythm'), (6, 'Ectopic Atrial Rhythm'), (7, 'Normal Sinus Rhythm alternating with Ectopic Atrial Rhythm'), (8, 'Junctional Rhythm (accelerated or escape)'), (9, 'Ventricular Rhythm (accelerated or escape)')])
    ecg_interp_arrhythmia = models.CharField(help_text='Check all that apply.', null=True, max_length=2000, verbose_name='$s ECG Interpretation: Arrhythmia/Conduction. ', blank=True)
    ecg_interp_axis = models.CharField(help_text='Check all that apply.', null=True, max_length=2000, verbose_name='$s ECG Interpretation: Axis.', blank=True)
    ecg_interp_structure = models.IntegerField(max_length=2000, blank=True, help_text='Check all that apply', null=True, verbose_name='$s ECG Interpretation: Structural. ', choices=[(1, 'None'), (2, 'Right atrial enlargement (RAE)'), (3, 'Left atrial enlargement (LAE)'), (4, 'Bi-atrial enlargement  (BAE)'), (5, 'Biventricular hypertrophy'), (6, 'Right ventricular hypertrophy (RVH)'), (7, 'Right ventricular hypertrophy (RVH) with strain'), (8, 'Left ventricular hypertrophy (LVH)'), (9, 'Left ventricular hypertrophy (LVH) with strain'), (10, 'Hypertrophic Cardiomyopathy (HCM)'), (11, 'Dilated Cardiomyopathy (DCM)'), (12, 'Dextrocardia')])
    ecg_interp_other = models.TextField(help_text='', null=True, verbose_name='$s ECG Interpretation:  Other (not listed above)', blank=True) # This field type is a guess
    ecg_result = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s ECG Result', choices=[(1, 'Normal'), (2, 'VON - Variant of Normal'), (3, 'Abnormal'), (4, 'Not Determined')])

    class Meta:
	 db_table = 'Ecg'


class EchoResults(models.Model):
    echo_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Echocardiogram done', choices=[(1, 'Yes'), (2, 'No')])
    echoresults = models.ForeignKey(EchoResults)

    class Meta:
	 db_table = 'EchoResults'


class Echotest(models.Model):
    echo_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the $s ECHO | Other test category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    echo_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of $s ECHO', blank=True)
    echo_ht_report = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Height/cm on $s ECHO report', blank=True)
    echo_wt_report = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Weight/kg on $s ECHO report', blank=True)
    echo_bsa = models.CharField(help_text='', null=True, max_length=2000, verbose_name='BSA - Body Surface Area on $s ECHO report', blank=True)
    echo_ivsd = models.CharField(help_text='', null=True, max_length=2000, verbose_name='IVSd - (Diastolic septal thickness/cm) on $s ECHO report', blank=True)
    echo_ivsd_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='IVSd Zscore- (Diastolic septal thickness/zscore) on $s ECHO report', blank=True)
    echo_lvidd = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVIDd - (LV Diastolic dimension/cm) on $s ECHO report', blank=True)
    echo_lvidd_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVIDd Zscore- (LV Diastolic dimension/zscore) on $s ECHO report', blank=True)
    echo_lvids = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVIDs - (LV Systolic dimension/cm) on $s ECHO report', blank=True)
    echo_lvids_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVIDs Zscore- (LV Systolic dimension/zscore) on $s ECHO report', blank=True)
    echo_lvpwd = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVPWd - (LV diastolic wall thickness/cm) on $s ECHO report', blank=True)
    echo_lvpwd_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVPWd Zscore- (LV diastolic wall thickness/zscore) on $s ECHO report', blank=True)
    echo_lv_mass = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV mass - (M-mode LV mass-ASE corr./g) on $s ECHO report', blank=True)
    echo_lv_mass_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV mass Zscore- (M-mode LV mass-ASE corr./g/zscore) on $s ECHO report', blank=True)
    echo_lv_mass_index = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV mass index (g/h^2.7) on $s ECHO report', blank=True)
    echo_lv_vol_d_4c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (4C) - (mL) on $s ECHO report', blank=True)
    echo_lv_vol_d_2c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (2C) - (mL) on $s ECHO report', blank=True)
    echo_lv_vol_d_biplane = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (biplane) - (mL) on $s ECHO report', blank=True)
    echo_lv_vol_s_4c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, s (4C) - (mL) on $s ECHO report', blank=True)
    echo_lv_vol_s_2c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, s (2C) - (mL) on $s ECHO report', blank=True)
    echo_lv_vol_s_biplane = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, s (biplane) - (mL) on $s ECHO report', blank=True)
    echo_lv_vol_d_4c_index = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (4C) index - (mL/m^2) on $s ECHO report', blank=True)
    echo_lv_vol_d_2c_index = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (2C) index - (mL/m^2) on $s ECHO report', blank=True)
    echo_lv_vol_d_biplane_ind = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV volume, d (biplane) index - (mL/m^2) on $s ECHO report', blank=True)
    echo_aov_annulus = models.CharField(help_text='', null=True, max_length=2000, verbose_name='AoV annulus - (Aortic Annulus diameter/cm) on $s ECHO report', blank=True)
    echo_aov_annulus_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='AoV annulus Zscore- (Aortic Annulus diameter/zscore) on $s ECHO report', blank=True)
    echo_ao_root = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao Root - (Aortic Root diameter/cm) on $s ECHO report', blank=True)
    echo_ao_root_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao Root Zscore- (Aortic Root diameter/zscore) on $s ECHO report', blank=True)
    echo_ao_st_junct_s = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao ST junct, s - (Sinotubular junction diameter/cm) on $s ECHO report', blank=True)
    echo_ao_st_junct_s_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao ST junct, s Zscore- (Sinotubular junction diameter/zscore) on $s ECHO report', blank=True)
    echo_ao_asc_d = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao asc,d - (cm) on $s ECHO report', blank=True)
    echo_ao_asc_d_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao asc,d, Zscore on $s ECHO report', blank=True)
    echo_ao_dsc_d = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao dsc,d - (cm) on $s ECHO report', blank=True)
    echo_ao_dsc_d_zscore = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Ao dsc,d, Zscore on $s ECHO report', blank=True)
    echo_aov_area = models.CharField(help_text='', null=True, max_length=2000, verbose_name='AoV Area - (Aortic valve area/cm^2) on $s ECHO report', blank=True)
    echo_lv_sf = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV SF - (LV shortening fraction M-mode/%) on $s ECHO report', blank=True)
    echo_lv_ef = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV EF - (Ejection fraction M-mode/%) on $s ECHO report', blank=True)
    echo_lv_ef_4c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV EF (4C) - (Ejection fraction/%) on $s ECHO report', blank=True)
    echo_lv_ef_2c = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV EF (2C) - (Ejection fraction/%) on $s ECHO report', blank=True)
    echo_lv_ef_biplane = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV EF (biplane) - (Ejection fraction/%) on $s ECHO report', blank=True)
    echo_lv_ef_aov = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV ejection time (AoV) - (msec) on $s ECHO report', blank=True)
    echo_lv_intra_avv = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV Intra AVV Time (MV) - (msec) on $s ECHO report', blank=True)
    echo_lv_mpi = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV MPI on $s ECHO report', blank=True)
    echo_lv_septal_annulus = models.CharField(help_text='', null=True, max_length=2000, verbose_name="LV Diastolic Function: Septal annulus e' - (m/s) on $s ECHO report", blank=True)
    echo_lv_mitral_septal = models.CharField(help_text='', null=True, max_length=2000, verbose_name="LV Diastolic Function: E/e' (mitral septal) on $s ECHO report", blank=True)
    echo_lv_mitral_lateral = models.CharField(help_text='', null=True, max_length=2000, verbose_name="LV Diastolic Function: E/e' (mitral lateral) on $s ECHO report", blank=True)
    echo_lv_mitral_inflow = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV Diastolic Function: E/A (mitral inflow) on $s ECHO report', blank=True)
    echo_lvot_peak_vel = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVOTO Doppler: Peak velocity (m/s) on $s ECHO report', blank=True)
    echo_lvot_peak_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVOTO Doppler: Peak gradient (mmHg) on $s ECHO report', blank=True)
    echo_lvot_mean_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVOTO Doppler: Mean gradient (mmHg) on $s ECHO report', blank=True)
    echo_av_peak_vel = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Aortic Valve Doppler: Peak Velocity (m/s) on $s ECHO report', blank=True)
    echo_av_peak_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Aortic Valve Doppler: Peak Gradient (mmHg) on $s ECHO report', blank=True)
    echo_av_mean_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Aortic Valve Doppler: Mean Gradient (mmHg) on $s ECHO report', blank=True)
    echo_av_eject_time = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Aortic Valve Doppler: Ejection time (msec) on $s ECHO report', blank=True)
    echo_mv_peak_e = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Mitral Valve Doppler: Peak E (m/s) on $s ECHO report', blank=True)
    echo_mv_peak_a = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Mitral Valve Doppler: Peak A (m/s) on $s ECHO report', blank=True)
    echo_myocard_perf_index = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Myocardial Performance Index on $s ECHO report', blank=True)
    echo_samm = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Systolic Anterior Motion of Mitral Valve on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    echo_samm_degree = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Degree of SAMM on $s ECHO report', blank=True)
    echo_lvoto = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='LVOTO - (Left Ventricular Outflow Tract Obstruction) on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    echo_lvoto_gradient = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='LVOTO Gradient on $s ECHO report', choices=[(1, 'Mild'), (2, 'Moderate'), (3, 'Severe'), (4, 'Other')])
    echo_lvoto_gradient_oth = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LVOTO Gradient Other - Specify on $s ECHO report', blank=True)
    echo_rvoto = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='RVOTO - (Right Ventricular Outflow Tract Obstruction) on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Unknown/Not documented')])
    echo_rvoto_gradient = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='RVOTO Gradient on $s ECHO report', choices=[(1, 'Mild'), (2, 'Moderate'), (3, 'Severe'), (4, 'Other')])
    echo_rvoto_gradient_oth = models.CharField(help_text='', null=True, max_length=2000, verbose_name='RVOTO Gradient Other - Specify on $s ECHO report', blank=True)
    echo_rv_chamber = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='RV chamber on $s ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal')])
    echo_rv_specify = models.CharField(help_text='', null=True, max_length=2000, verbose_name='RV: Specify on $s ECHO report', blank=True)
    echo_lv_chamber = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='LV chamber on $s ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal')])
    echo_lv_specify = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LV: Specify on $s ECHO report', blank=True)
    echo_ra = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='RA on $s ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal')])
    echo_ra_specify = models.CharField(help_text='', null=True, max_length=2000, verbose_name='RA: Specify on $s ECHO report', blank=True)
    echo_la = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='LA on $s ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal')])
    echo_la_specify = models.CharField(help_text='', null=True, max_length=2000, verbose_name='LA: Specify on $s ECHO report', blank=True)
    echo_aortic_root = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic Root on $s ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal')])
    echo_aortic_root_specify = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Aortic Root: Specify on $s ECHO report', blank=True)
    echo_bicuspid_aortic_val = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Bicuspid aortic valve on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_aortic_insuff = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic valve insufficiency on $s ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_ai_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic valve insufficiency: Severity on $s ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_aortic_stenosis = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic stenosis on $s ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_as_sever = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic stenosis: Severity on $s ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_as_peak_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='AS-Peak gradient (m/sec) on $s ECHO report', blank=True)
    echo_as_mean_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='AS-Mean gradient (m/sec) on $s ECHO report', blank=True)
    echo_region_aortic_sten = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Region of aortic stenosis on $s ECHO report', choices=[(1, 'Valve'), (2, 'Subvalvular'), (3, 'Supravalvular'), (4, 'Other')])
    echo_region_as_oth = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Region of aortic stenosis: Specify on $s ECHO report', blank=True)
    echo_hcm = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Hypertrophic Cardiomyopathy on $s ECHO report', blank=True)
    echo_hcm_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Hypertrophic Cardiomyopathy: Severity on $s ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_hypertrophy_loc = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Location of Hypertrophy on $s ECHO report', choices=[(1, 'Septal'), (2, 'Apical'), (3, 'Concentric'), (4, 'Other')])
    echo_hyper_other = models.TextField(help_text='', null=True, verbose_name='Location of Hypertrophy Other - Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_pul_insuff = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pulmonary valve insufficiency on $s ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_pi_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pulmonary valve insufficiency: Severity on $s ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_pul_stenosis = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pulmonary stenosis on $s ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_ps_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pulmonary stenosis: Severity on $s ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_ps_peak_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='PS-Peak gradient (m/sec) on $s ECHO report', blank=True)
    echo_ps_mean_grad = models.CharField(help_text='', null=True, max_length=2000, verbose_name='PS-Mean gradient (m/sec) on $s ECHO report', blank=True)
    echo_mit_insuff = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitral valve insufficiency on $s ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_mi_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitral valve insufficiency: Severity on $s ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_mit_val_prolapse = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitral valve prolapse on $s ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_mvp_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Mitral valve prolapse: Severity on $s ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_ms_gradient = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='MS gradient on $s ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_ms_grad_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='MS gradient: Severity on $s ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_ms_jet_velocity = models.CharField(help_text='', null=True, max_length=2000, verbose_name='MS mean jet velocity (m/sec) on $s ECHO report', blank=True)
    echo_tri_insuff = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tricuspid valve insufficiency on $s ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_ti_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tricuspid valve insufficiency: Severity on $s ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_tri_stenosis = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tricuspid valve stenosis on $s ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_tri_sten_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Tricuspid valve stenosis: Severity on $s ECHO report', choices=[(1, 'Trivial'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe')])
    echo_tri_sten_gradient = models.CharField(help_text='', null=True, max_length=2000, verbose_name='TS-Peak gradient (m/sec) on $s ECHO report', blank=True)
    echo_rv_pressure = models.CharField(help_text='', null=True, max_length=2000, verbose_name='RV pressure estimate (mm/Hg > right atrial v wave) on $s ECHO report', blank=True)
    echo_asd = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Atrial septal defect on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_asd_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='ASD: Size on $s ECHO report', choices=[(1, 'Small'), (2, 'Moderate'), (3, 'Large')])
    echo_asd_specify_small = models.TextField(help_text='', null=True, verbose_name='ASD (small): Specify (cm) on $s ECHO report', blank=True) # This field type is a guess
    echo_asd_specify_mod = models.TextField(help_text='', null=True, verbose_name='ASD (moderate): Specify (cm) on $s ECHO report', blank=True) # This field type is a guess
    echo_asd_specify_large = models.TextField(help_text='', null=True, verbose_name='ASD (large): Specify (cm) on $s ECHO report', blank=True) # This field type is a guess
    echo_pfo = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Patent foramen ovale on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_pfo_severity = models.CharField(help_text='', null=True, max_length=2000, verbose_name='PFO: Specify on $s ECHO report', blank=True)
    echo_vsd = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ventricular septal defect on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_vsd_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='VSD: Size on $s ECHO report', choices=[(1, 'Small'), (2, 'Moderate'), (3, 'Large')])
    echo_vsd_specify_small = models.TextField(help_text='', null=True, verbose_name='VSD (small): Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_vsd_specify_mod = models.TextField(help_text='', null=True, verbose_name='ASD (moderate): Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_vsd_specify_large = models.TextField(help_text='', null=True, verbose_name='ASD (large): Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_pda = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Patent ductus arteriosus on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_pda_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='PDA: Severity on $s ECHO report', choices=[(1, 'Small'), (2, 'Moderate'), (3, 'Large')])
    echo_pda_specify_small = models.TextField(help_text='', null=True, verbose_name='PDA (small): Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_pda_specify_mod = models.TextField(help_text='', null=True, verbose_name='PDA (moderate): Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_pda_specify_large = models.TextField(help_text='', null=True, verbose_name='PDA (large): Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_coarct = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Coarctation of the aorta on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Other')])
    echo_coarct_severity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Coarctation of the aorta: Severity on $s ECHO report', choices=[(1, 'Mild'), (2, 'Moderate'), (3, 'Severe')])
    echo_coarct_sever_oth = models.TextField(help_text='', null=True, verbose_name='Coarctation of the aorta/Other: Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_peri_effusion = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pericardial effusion on $s ECHO report', choices=[(1, 'Yes'), (2, 'No')])
    echo_peri_eff_location = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Pericardial effusion: Location on $s ECHO report', choices=[(1, 'RA'), (2, 'RV'), (3, 'LA'), (4, 'LA'), (5, 'LV'), (6, 'Other')])
    echo_peri_eff_loc_oth = models.TextField(help_text='', null=True, verbose_name='Pericardial effusion/Other: Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_peri_eff_size = models.TextField(help_text='', null=True, verbose_name='Pericardial effusion/Size: Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_rt_coronary_art = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Right coronary artery on $s ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not well seen'), (4, 'Unknown/Not documented')])
    echo_lt_coronary_main = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left coronary artery _ Main on $s ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not well seen'), (4, 'Unknown/Not documented')])
    echo_lt_coronary_ant_desc = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left coronary artery _ Anterior descending on $s ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not well seen'), (4, 'Unknown/Not documented')])
    echo_lt_coronary_circum = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Left coronary artery _ Circumflex on $s ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not well seen'), (4, 'Unknown/Not documented')])
    echo_anom_ca_origin = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anomalous origin of coronary artery on $s ECHO report', choices=[(1, 'Both from R sinus'), (2, 'Both from L sinus'), (3, 'Single'), (4, 'Intramural'), (5, 'Other')])
    echo_anom_ca_origin_oth = models.TextField(help_text='', null=True, verbose_name='Anomalous origin CA/Other: Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_coronary_ostia = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Coronary artery ostia on $s ECHO report', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Not well seen'), (4, 'Not documented'), (5, 'Other')])
    echo_coronary_ostia_oth = models.TextField(help_text='', null=True, verbose_name='Coronary artery ostia Other - specify on $s ECHO report', blank=True) # This field type is a guess
    echo_aortic_arch = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Aortic Arch on $s ECHO report', choices=[(1, 'Normal branching'), (2, 'Right aortic arch'), (3, 'Aberrant Right subclavian'), (4, 'Double aortic arch'), (5, 'Other')])
    echo_aortic_arch_oth = models.TextField(help_text='', null=True, verbose_name='Aortic Arch other - Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_number_pul_vein = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Number of pulmonary veins seen entering the left atrium on $s ECHO report', choices=[(1, '4 veins'), (2, '3 veins'), (3, '2 veins'), (4, '1 vein'), (5, 'Not well seen'), (6, 'Not documented')])
    echo_anom_pul_vein = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anomalous pulmonary veins on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_anom_pul_vein_spec = models.TextField(help_text='', null=True, verbose_name='Anomalous pulmonary veins: Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_anom_ven_structure = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anomalous venous structures on $s ECHO report', choices=[(1, 'Yes'), (2, 'No'), (3, 'Not well seen')])
    echo_anom_ven_location = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Anomalous venous structures location on $s ECHO report', choices=[(1, 'SVC'), (2, 'LSVC to CS'), (3, 'Bilateral SVC'), (4, 'Azygos vein continuation of interrupted inferior vena cava (IVC)'), (5, 'Other')])
    echo_anom_ven_loc_oth = models.TextField(help_text='', null=True, verbose_name='Anomalous venous structures location/Other: Specify on $s ECHO report', blank=True) # This field type is a guess
    echo_other_chd = models.TextField(help_text='', null=True, verbose_name='Other congenital heart disease or findings on $s ECHO report', blank=True) # This field type is a guess
    echo_comments_report = models.TextField(help_text='', null=True, verbose_name='Additional comments from $s ECHO report not listed above.', blank=True) # This field type is a guess

    class Meta:
	 db_table = 'Echotest'


class EstResults(models.Model):
    est_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Exercise Stress Test done', choices=[(1, 'Yes'), (2, 'No')])
    estresults = models.ForeignKey(EstResults)

    class Meta:
	 db_table = 'EstResults'


class Exercisestresstest(models.Model):
    est_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the $s exercise stress test | Other test category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    est_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of $s EST', blank=True)
    est_machine = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST performed on', choices=[(1, 'Stationary Bicycle'), (2, 'Ramp/Treadmill')])
    est_hr = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Heart rate ', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_hr_other = models.TextField(help_text='', null=True, verbose_name='$s EST Heart rate - Other: Specify', blank=True) # This field type is a guess
    est_hr_rest = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Heart rate - rest', blank=True)
    est_hr_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Heart rate - maximum', blank=True)
    est_hr_response = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Heart rate response', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_hr_response_oth = models.TextField(help_text='', null=True, verbose_name='$s EST Heart rate response Other - Specify', blank=True) # This field type is a guess
    est_bp = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Blood pressure response', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_bp_response = models.TextField(help_text='', null=True, verbose_name='$s EST Blood pressure response - Other: Specify', blank=True) # This field type is a guess
    est_bp_rest = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Blood Pressure - rest', blank=True)
    est_bp_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Blood Pressure - maximum', blank=True)
    est_o2_sat = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Oxygen saturation', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_o2_other = models.TextField(help_text='', null=True, verbose_name='$s EST Oxygen saturated - Other: Specify', blank=True) # This field type is a guess
    est_o2_sat_rest = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Oxygen saturation - rest', blank=True)
    est_o2_sat_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Oxygen saturation - maximum', blank=True)
    est_work_rate = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Work rate', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_work_rate_other = models.TextField(help_text='', null=True, verbose_name='$s EST Work rate - Other: Specify', blank=True) # This field type is a guess
    est_work_rate_watts = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Work rate - Watts', blank=True)
    est_o2_consump = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Oxygen consumption', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_os_comsump_oth = models.TextField(help_text='', null=True, verbose_name='$s EST Oxygen consumption - Other: Specify', blank=True) # This field type is a guess
    est_os_comsump_rest_vo2 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Oxygen consumption - rest VO2 (L/min)', blank=True)
    est_os_comsump_max_vo2 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Oxygen consumption - max VO2 (L/min)', blank=True)
    est_os_comsump_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Oxygen consumption - max (ml/kg/min)', blank=True)
    est_os_comsump_max_at = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Oxygen consumption - Anerobic Threshold (AT)', blank=True)
    est_cardiac_output = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Cardiac output', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_cardiac_output_oth = models.TextField(help_text='', null=True, verbose_name='$s EST Cardiac output - Other: Specify', blank=True) # This field type is a guess
    est_cardiac_output_rest = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Cardiac output - rest', blank=True)
    est_card_output_rest_ci = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Cardiac output - rest - CI', blank=True)
    est_cardiac_output_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Cardiac output - maximum', blank=True)
    est_card_output_max_mci = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Cardiac output - maximum - MCI', blank=True)
    est_rhythm = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Rhythm', choices=[(1, 'Sinus'), (2, 'PAC-Premature Atrial Complexes'), (3, 'PVC-Premature Ventricular Complexes'), (4, 'PVC Couplets'), (5, 'Ventricular Tachycardia'), (6, 'Supraventricular Tachycardia'), (7, 'Ventricular Fibrillation'), (8, 'First Degree AV Block'), (9, 'Second Degree AV Block (Mobitz Type I Wenckebach)'), (10, 'Second Degree AV Block (Mobitz Type II)'), (11, 'Third Degree (or Complete) AV Block'), (12, 'Atrial Fibrillation'), (13, 'Atrial Flutter'), (14, 'Atrial Tachycardia'), (15, 'Bradycardia'), (16, 'Junctional rhythm'), (17, 'Ventricular fibrillation'), (18, 'Prolonged QT Interval'), (19, 'Wolff-Parkinson-White'), (20, 'Torsades de pointes'), (21, 'Other')])
    est_rhythm_other = models.TextField(help_text='', null=True, verbose_name='$s EST Rhythm - Other: Specify', blank=True) # This field type is a guess
    est_st_seg_change = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST ST segment changes', choices=[(1, 'None'), (2, 'Other')])
    est_st_seg_change_oth = models.TextField(help_text='', null=True, verbose_name='$s EST ST segment changes - Other: Specify', blank=True) # This field type is a guess
    est_symptom = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Symptoms', choices=[(1, 'None'), (2, 'Other')])
    est_symptom_oth = models.TextField(help_text='', null=True, verbose_name='$s EST Symptoms - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_rest = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Pulmonary function (rest)', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_pul_func_rest_oth = models.TextField(help_text='', null=True, verbose_name='$s EST Pulmonary function  (rest) - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_reserve = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Pulmonary function (reserve)', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_pul_func_reserve_oth = models.TextField(help_text='', null=True, verbose_name='$s EST Pulmonary function (reserve) - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_post = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s EST Pulmonary function (post)', choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Other')])
    est_pul_func_post_oth = models.TextField(help_text='', null=True, verbose_name='$s EST Pulmonary function (post) - Other: Specify', blank=True) # This field type is a guess
    est_pul_func_ve = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Pulmonary function - VE', blank=True)
    est_pul_func_rq = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s EST Pulmonary function - RQ', blank=True)
    est_summary = models.TextField(help_text='', null=True, verbose_name='EST $s Summary', blank=True) # This field type is a guess

    class Meta:
	 db_table = 'Exercisestresstest'


class HolterResults(models.Model):
    hm_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Holter Monitor test done', choices=[(1, 'Yes'), (2, 'No')])
    holterresults = models.ForeignKey(HolterResults)

    class Meta:
	 db_table = 'HolterResults'


class Hm(models.Model):
    hm_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the $s holter monitor test | Other test category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    hm_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of $s Holter Monitor test', blank=True)
    hm_hr_total = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Heart Rate Data: Total beats', blank=True)
    hm_hr_min = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Heart Rate Data: Min HR (bpm)', blank=True)
    hm_hr_avg = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Heart Rate Data: Avg HR (bpm)', blank=True)
    hm_hr_max = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Heart Rate Data: Max HR (bpm)', blank=True)
    hm_hr_var_asdnn5 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter HR Variability: ASDNN 5 (msec)', blank=True)
    hm_hr_var_sdnn5 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter HR Variability: SDANN 5 (msec)', blank=True)
    hm_hr_var_sdnn = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter HR Variability: SDNN (msec)', blank=True)
    hm_hr_var_rmssd = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter HR Variability: RMSSD (msec)', blank=True)
    hm_ve_total_beat = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Total VE Beats (%)', blank=True)
    hm_ve_vent_run = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Vent Runs', blank=True)
    hm_ve_beat = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Beats', blank=True)
    hm_ve_long = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Longest', blank=True)
    hm_ve_fast = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Fastest (bpm)', blank=True)
    hm_ve_triplet = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Triplets (Events)', blank=True)
    hm_ve_couplet = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Couplets (Events)', blank=True)
    hm_ve_ront = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: R on T', blank=True)
    hm_ve_bi_trigem = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Bi/Trigeminy (Beats)', blank=True)
    hm_ve_max_ve_min = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Max VE/Minute  (Beats)', blank=True)
    hm_ve_max_ve_hr = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Max VE/Hour  (Beats)', blank=True)
    hm_ve_mean_hour = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: Mean VE/Hour', blank=True)
    hm_ve_ve_1000 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Ventricular Ectopy: VE/1000 (% of rhythm)', blank=True)
    hm_sve_total_beat = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: Total SVE Beats (%)', blank=True)
    hm_sve_svt_run = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: SVT Runs', blank=True)
    hm_sve_beat = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: Beats', blank=True)
    hm_sve_long = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: Longest', blank=True)
    hm_sve_fast = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: Fastest (bpm)', blank=True)
    hm_sve_atr_pair = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: Atrial Pairs (Events)', blank=True)
    hm_sve_long_rr = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: Longest R-R (Longest Pause/sec)', blank=True)
    hm_sve_max_sve_min = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: Max SVE/Minute (Beats)', blank=True)
    hm_sve_max_sve_hour = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: Max SVE/Hour (Beats)', blank=True)
    hm_sve_mean_sve_hour = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: Mean SVE/Hour (Beats)', blank=True)
    hm_sve_sve_1000 = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Supraventricular Ectopy: SVE/1000 (% of rhythm)', blank=True)
    hm_summary = models.IntegerField(help_text='', null=True, verbose_name='$s Holter Monitor Interpretation: Heart rate interpretation', blank=True, choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Increased vagal tone'), (4, 'Increased sympathetic tone')]) # This field type is a guess
    hm_brady_percent = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Monitor Interpretation: Bradycardia % of rhythm', blank=True)
    hm_avblock_percent = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s Holter Monitor Interpretation: AV Block', choices=[(1, 'None'), (2, 'First degree'), (3, 'Second degree'), (4, 'Third degree')])
    hm_pr_interval = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Monitor Interpretation: PR Interval', blank=True)
    hm_qrs_interval = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Monitor Interpretation: QRS Interval', blank=True)
    hm_qtc_interval = models.CharField(help_text='', null=True, max_length=2000, verbose_name='$s Holter Monitor Interpretation: QTc Interval', blank=True)
    hm_addit_info = models.TextField(help_text='', null=True, verbose_name='$s Holter Monitor Interpretation: Additional information ', blank=True) # This field type is a guess

    class Meta:
	 db_table = 'Hm'


class CmriResults(models.Model):
    cmri_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Cardiac MRI done', choices=[(1, 'Yes'), (2, 'No')])
    cmriresults = models.ForeignKey(CmriResults)

    class Meta:
	 db_table = 'CmriResults'


class Cardiacmri(models.Model):
    cmri_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the $s cardiac MRI | Other test category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    cmri_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of Cardiac $s MRI', blank=True)
    cmri_evidence = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='$s Cardiac MRI Summary showed evidence of ', choices=[(6, 'None'), (1, 'HCM- Hypertrophic cardiomyopathy'), (2, 'LE- Myocardial late enhancement'), (3, 'ARVD/C- Arrhythmogenic right ventricular dysplasia/cardiomyopathy'), (4, 'LVNC- Left ventricular noncompaction'), (5, 'DCM- Dilated cardiomyopathy')])
    cmri_hypertrophy_loc = models.IntegerField(help_text='', null=True, verbose_name='Location of Hypertrophy | Location of Hypertrophy Other - Specify', blank=True, choices=[(1, 'Septal'), (2, 'Apical'), (3, 'Concentric'), (4, 'Other')]) # This field type is a guess
    cmri_summary = models.TextField(help_text='', null=True, verbose_name='$s Cardiac MRI Summary/Final report', blank=True) # This field type is a guess

    class Meta:
	 db_table = 'Cardiacmri'


class CardiacCathProcedures(models.Model):
    ccath_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Cardiac catheterization done', choices=[(1, 'Yes'), (2, 'No')])
    cardiaccathprocedures = models.ForeignKey(CardiacCathProcedures)

    class Meta:
	 db_table = 'CardiacCathProcedures'


class Cardiaccatherizations(models.Model):
    ccath_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the $s cardiac catherization | Other procedure category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    ccath_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of $s Cardiac cathertization', blank=True)
    ccath_summary = models.TextField(help_text='', null=True, verbose_name='$s Cardiac catherization summary', blank=True) # This field type is a guess

    class Meta:
	 db_table = 'Cardiaccatherizations'


class CardiacSurgery(models.Model):
    cardsurg_done = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Cardiac surgery done', choices=[(1, 'Yes'), (2, 'No')])
    cardiacsurgery = models.ForeignKey(CardiacSurgery)

    class Meta:
	 db_table = 'CardiacSurgery'


class Cardiacsurgery(models.Model):
    cardsurg_enrollment = models.IntegerField(help_text='', null=True, verbose_name='How would you categorize the $s cardiac surgery | Other procedure category', blank=True, choices=[(1, 'Initial test'), (2, 'Enrollment test'), (3, 'Post-enrollment test'), (4, 'Other')]) # This field type is a guess
    cardsurg_date = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Date of $s cardiac surgery', blank=True)
    cardsurg_name = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Name of $s cardiac surgery', blank=True)
    cardsurg_summary = models.TextField(help_text='', null=True, verbose_name='$s cardiac surgery summary', blank=True) # This field type is a guess
    cardiacsurgery = models.ForeignKey(CardiacSurgery)

    class Meta:
	 db_table = 'Cardiacsurgery'


