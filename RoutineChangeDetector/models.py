from django.db import models

# Create your models here.


class UserData(models.Model):

    # * Record ID Fields
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(max_length=100, editable=False)
    timestamp = models.BigIntegerField(editable=False)



    # * Accelerometer Fields
    raw_acc_magnitude_stats_mean = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_stats_std = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_stats_moment3 = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_stats_moment4 = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_stats_percentile25 = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_stats_percentile50 = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_stats_percentile75 = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_stats_value_entropy = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_stats_time_entropy = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_spectrum_log_energy_band0 = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_spectrum_log_energy_band1 = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_spectrum_log_energy_band2 = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_spectrum_log_energy_band3 = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_spectrum_log_energy_band4 = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_spectrum_spectral_entropy = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_autocorrelation_period = models.FloatField(null=True, blank=True)
    raw_acc_magnitude_autocorrelation_normalized_ac = models.FloatField(null=True, blank=True)
    raw_acc_3d_mean_x = models.FloatField(null=True, blank=True)
    raw_acc_3d_mean_y = models.FloatField(null=True, blank=True)
    raw_acc_3d_mean_z = models.FloatField(null=True, blank=True)
    raw_acc_3d_std_x = models.FloatField(null=True, blank=True)
    raw_acc_3d_std_y = models.FloatField(null=True, blank=True)
    raw_acc_3d_std_z = models.FloatField(null=True, blank=True)
    raw_acc_3d_ro_xy = models.FloatField(null=True, blank=True)
    raw_acc_3d_ro_xz = models.FloatField(null=True, blank=True)
    raw_acc_3d_ro_yz = models.FloatField(null=True, blank=True)



    # * Gyroscope Fields
    proc_gyro_magnitude_stats_mean = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_stats_std = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_stats_moment3 = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_stats_moment4 = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_stats_percentile25 = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_stats_percentile50 = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_stats_percentile75 = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_stats_value_entropy = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_stats_time_entropy = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_spectrum_log_energy_band0 = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_spectrum_log_energy_band1 = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_spectrum_log_energy_band2 = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_spectrum_log_energy_band3 = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_spectrum_log_energy_band4 = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_spectrum_spectral_entropy = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_autocorrelation_period = models.FloatField(null=True, blank=True)
    proc_gyro_magnitude_autocorrelation_normalized_ac = models.FloatField(null=True, blank=True)
    proc_gyro_3d_mean_x = models.FloatField(null=True, blank=True)
    proc_gyro_3d_mean_y = models.FloatField(null=True, blank=True)
    proc_gyro_3d_mean_z = models.FloatField(null=True, blank=True)
    proc_gyro_3d_std_x = models.FloatField(null=True, blank=True)
    proc_gyro_3d_std_y = models.FloatField(null=True, blank=True)
    proc_gyro_3d_std_z = models.FloatField(null=True, blank=True)
    proc_gyro_3d_ro_xy = models.FloatField(null=True, blank=True)
    proc_gyro_3d_ro_xz = models.FloatField(null=True, blank=True)
    proc_gyro_3d_ro_yz = models.FloatField(null=True, blank=True)



    # * Magnetometer Fields
    raw_magnet_magnitude_stats_mean = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_stats_std = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_stats_moment3 = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_stats_moment4 = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_stats_percentile25 = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_stats_percentile50 = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_stats_percentile75 = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_stats_value_entropy = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_stats_time_entropy = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_spectrum_log_energy_band0 = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_spectrum_log_energy_band1 = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_spectrum_log_energy_band2 = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_spectrum_log_energy_band3 = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_spectrum_log_energy_band4 = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_spectrum_spectral_entropy = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_autocorrelation_period = models.FloatField(null=True, blank=True)
    raw_magnet_magnitude_autocorrelation_normalized_ac = models.FloatField(null=True, blank=True)
    raw_magnet_3d_mean_x = models.FloatField(null=True, blank=True)
    raw_magnet_3d_mean_y = models.FloatField(null=True, blank=True)
    raw_magnet_3d_mean_z = models.FloatField(null=True, blank=True)
    raw_magnet_3d_std_x = models.FloatField(null=True, blank=True)
    raw_magnet_3d_std_y = models.FloatField(null=True, blank=True)
    raw_magnet_3d_std_z = models.FloatField(null=True, blank=True)
    raw_magnet_3d_ro_xy = models.FloatField(null=True, blank=True)
    raw_magnet_3d_ro_xz = models.FloatField(null=True, blank=True)
    raw_magnet_3d_ro_yz = models.FloatField(null=True, blank=True)
    raw_magnet_avr_cosine_similarity_lag_range0 = models.FloatField(null=True, blank=True)
    raw_magnet_avr_cosine_similarity_lag_range1 = models.FloatField(null=True, blank=True)
    raw_magnet_avr_cosine_similarity_lag_range2 = models.FloatField(null=True, blank=True)
    raw_magnet_avr_cosine_similarity_lag_range3 = models.FloatField(null=True, blank=True)
    raw_magnet_avr_cosine_similarity_lag_range4 = models.FloatField(null=True, blank=True)



    # * Watch Fields
    watch_acc_magnitude_stats_mean = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_stats_std = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_stats_moment3 = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_stats_moment4 = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_stats_percentile25 = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_stats_percentile50 = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_stats_percentile75 = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_stats_value_entropy = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_stats_time_entropy = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_spectrum_log_energy_band0 = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_spectrum_log_energy_band1 = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_spectrum_log_energy_band2 = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_spectrum_log_energy_band3 = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_spectrum_log_energy_band4 = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_spectrum_spectral_entropy = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_autocorrelation_period = models.FloatField(null=True, blank=True)
    watch_acc_magnitude_autocorrelation_normalized_ac = models.FloatField(null=True, blank=True)
    watch_acc_3d_mean_x = models.FloatField(null=True, blank=True)
    watch_acc_3d_mean_y = models.FloatField(null=True, blank=True)
    watch_acc_3d_mean_z = models.FloatField(null=True, blank=True)
    watch_acc_3d_std_x = models.FloatField(null=True, blank=True)
    watch_acc_3d_std_y = models.FloatField(null=True, blank=True)
    watch_acc_3d_std_z = models.FloatField(null=True, blank=True)
    watch_acc_3d_ro_xy = models.FloatField(null=True, blank=True)
    watch_acc_3d_ro_xz = models.FloatField(null=True, blank=True)
    watch_acc_3d_ro_yz = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_x_log_energy_band0 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_x_log_energy_band1 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_x_log_energy_band2 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_x_log_energy_band3 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_x_log_energy_band4 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_y_log_energy_band0 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_y_log_energy_band1 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_y_log_energy_band2 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_y_log_energy_band3 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_y_log_energy_band4 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_z_log_energy_band0 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_z_log_energy_band1 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_z_log_energy_band2 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_z_log_energy_band3 = models.FloatField(null=True, blank=True)
    watch_acc_spectrum_z_log_energy_band4 = models.FloatField(null=True, blank=True)
    watch_acc_relative_directions_avr_cosine_similarity_lag_range0 = models.FloatField(null=True, blank=True)
    watch_acc_relative_directions_avr_cosine_similarity_lag_range1 = models.FloatField(null=True, blank=True)
    watch_acc_relative_directions_avr_cosine_similarity_lag_range2 = models.FloatField(null=True, blank=True)
    watch_acc_relative_directions_avr_cosine_similarity_lag_range3 = models.FloatField(null=True, blank=True)
    watch_acc_relative_directions_avr_cosine_similarity_lag_range4 = models.FloatField(null=True, blank=True)
    watch_heading_mean_cos = models.FloatField(null=True, blank=True)
    watch_heading_std_cos = models.FloatField(null=True, blank=True)
    watch_heading_mom3_cos = models.FloatField(null=True, blank=True)
    watch_heading_mom4_cos = models.FloatField(null=True, blank=True)
    watch_heading_mean_sin = models.FloatField(null=True, blank=True)
    watch_heading_std_sin = models.FloatField(null=True, blank=True)
    watch_heading_mom3_sin = models.FloatField(null=True, blank=True)
    watch_heading_mom4_sin = models.FloatField(null=True, blank=True)
    watch_heading_entropy_8bins = models.FloatField(null=True, blank=True)



    # * Location Fields
    location_num_valid_updates = models.FloatField(null=True, blank=True)
    location_log_latitude_range = models.FloatField(null=True, blank=True)
    location_log_longitude_range = models.FloatField(null=True, blank=True)
    location_min_altitude = models.FloatField(null=True, blank=True)
    location_max_altitude = models.FloatField(null=True, blank=True)
    location_min_speed = models.FloatField(null=True, blank=True)
    location_max_speed = models.FloatField(null=True, blank=True)
    location_best_horizontal_accuracy = models.FloatField(null=True, blank=True)
    location_best_vertical_accuracy = models.FloatField(null=True, blank=True)
    location_diameter = models.FloatField(null=True, blank=True)
    location_log_diameter = models.FloatField(null=True, blank=True)
    location_quick_features_std_lat = models.FloatField(null=True, blank=True)
    location_quick_features_std_long = models.FloatField(null=True, blank=True)
    location_quick_features_lat_change = models.FloatField(null=True, blank=True)
    location_quick_features_long_change = models.FloatField(null=True, blank=True)
    location_quick_features_mean_abs_lat_deriv = models.FloatField(null=True, blank=True)
    location_quick_features_mean_abs_long_deriv = models.FloatField(null=True, blank=True)



    # * Audio Fields
    audio_naive_mfcc0_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc1_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc2_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc3_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc4_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc5_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc6_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc7_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc8_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc9_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc10_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc11_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc12_mean = models.FloatField(null=True, blank=True)
    audio_naive_mfcc0_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc1_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc2_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc3_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc4_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc5_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc6_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc7_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc8_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc9_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc10_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc11_std = models.FloatField(null=True, blank=True)
    audio_naive_mfcc12_std = models.FloatField(null=True, blank=True)
    audio_properties_max_abs_value = models.FloatField(null=True, blank=True)
    audio_properties_normalization_multiplier = models.FloatField(null=True, blank=True)



    # * App State
    discrete_app_state_is_active = models.NullBooleanField(blank=True, default=False)
    discrete_app_state_is_inactive = models.NullBooleanField(blank=True, default=False)
    discrete_app_state_is_background = models.NullBooleanField(blank=True, default=False)
    discrete_app_state_missing = models.NullBooleanField(blank=True, default=False)



    # * Battery State 
    discrete_battery_plugged_is_ac = models.NullBooleanField(blank=True, default=False)
    discrete_battery_plugged_is_usb = models.NullBooleanField(blank=True, default=False)
    discrete_battery_plugged_is_wireless = models.NullBooleanField(blank=True, default=False)
    discrete_battery_plugged_missing = models.NullBooleanField(blank=True, default=False)
    discrete_battery_state_is_unknown = models.NullBooleanField(blank=True, default=False)
    discrete_battery_state_is_unplugged = models.NullBooleanField(blank=True, default=False)
    discrete_battery_state_is_not_charging = models.NullBooleanField(blank=True, default=False)
    discrete_battery_state_is_discharging = models.NullBooleanField(blank=True, default=False)
    discrete_battery_state_is_charging = models.NullBooleanField(blank=True, default=False)
    discrete_battery_state_is_full = models.NullBooleanField(blank=True, default=False)
    discrete_battery_state_missing = models.NullBooleanField(blank=True, default=False)



    # * Call State
    discrete_on_the_phone_is_False = models.NullBooleanField(blank=True, default=False)
    discrete_on_the_phone_is_True = models.NullBooleanField(blank=True, default=False)
    discrete_on_the_phone_missing = models.NullBooleanField(blank=True, default=False)


    
    # * Ringer Mode
    discrete_ringer_mode_is_normal = models.NullBooleanField(blank=True, default=False)
    discrete_ringer_mode_is_silent_no_vibrate = models.NullBooleanField(blank=True, default=False)
    discrete_ringer_mode_is_silent_with_vibrate = models.NullBooleanField(blank=True, default=False)
    discrete_ringer_mode_missing = models.NullBooleanField(blank=True, default=False)



    # * Wifi State
    discrete_wifi_status_is_not_reachable = models.NullBooleanField(blank=True, default=False)
    discrete_wifi_status_is_reachable_via_wifi = models.NullBooleanField(blank=True, default=False)
    discrete_wifi_status_is_reachable_via_wwan = models.NullBooleanField(blank=True, default=False)
    discrete_wifi_status_missing = models.NullBooleanField(blank=True, default=False)



    # * Low Frequency Measurements
    lf_measurements_light = models.FloatField(null=True, blank=True)
    lf_measurements_pressure = models.FloatField(null=True, blank=True)
    lf_measurements_proximity_cm = models.FloatField(null=True, blank=True)
    lf_measurements_proximity = models.FloatField(null=True, blank=True)
    lf_measurements_relative_humidity = models.FloatField(null=True, blank=True)
    lf_measurements_battery_level = models.FloatField(null=True, blank=True)
    lf_measurements_screen_brightness = models.FloatField(null=True, blank=True)
    lf_measurements_temperature_ambient = models.FloatField(null=True, blank=True)



    # * Time of Day
    discrete_time_of_day_between0and6 = models.NullBooleanField(blank=True, default=False)
    discrete_time_of_day_between3and9 = models.NullBooleanField(blank=True, default=False)
    discrete_time_of_day_between6and12 = models.NullBooleanField(blank=True, default=False)
    discrete_time_of_day_between9and15 = models.NullBooleanField(blank=True, default=False)
    discrete_time_of_day_between12and18 = models.NullBooleanField(blank=True, default=False)
    discrete_time_of_day_between15and21 = models.NullBooleanField(blank=True, default=False)
    discrete_time_of_day_between18and24 = models.NullBooleanField(blank=True, default=False)
    discrete_time_of_day_between21and3 = models.NullBooleanField(blank=True, default=False)

    # ! Class Functions
    def __str__(self):
        returnText = ''
        returnText += self.id + '\t' + \
                        self.uuid + '\t' + \
                        self.timestamp + '\t' + \
                        self.raw_acc_magnitude_stats_mean + '\t' + \
                        self.proc_gyro_magnitude_stats_mean
        return returnText

class UserRoutine(models.Model):
    # * IDs
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(max_length=100, editable=False)
    data_record = models.ForeignKey(UserData, on_delete=models.CASCADE)

    # * Time
    day = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()



    # * Labels
    lying_down = models.FloatField()
    sitting = models.FloatField()
    walking = models.FloatField()
    running = models.FloatField()
    bicycling = models.FloatField()
    sleeping = models.FloatField()
    driving_driver = models.FloatField()
    driving_pass = models.FloatField()
    exercise = models.FloatField()
    shopping = models.FloatField()
    strolling = models.FloatField() 
    stairs_up = models.FloatField()
    stairs_down = models.FloatField()
    standing = models.FloatField()
    lab_work = models.FloatField()
    in_class = models.FloatField()
    in_meeting = models.FloatField()
    cooking = models.FloatField()
    drinking_alcohol = models.FloatField()
    shower = models.FloatField()
    cleaning = models.FloatField()
    laundry = models.FloatField()
    washing_dishes = models.FloatField()
    watch_tv = models.FloatField()
    surf_internet = models.FloatField()
    singing = models.FloatField()
    talking = models.FloatField()
    computer_work = models.FloatField()
    eating = models.FloatField()
    toilet = models.FloatField()
    grooming = models.FloatField()
    dressing = models.FloatField()
    with_coworker = models.FloatField()
    with_friends = models.FloatField()
    main_workplace = models.FloatField()
    indoors = models.FloatField()
    outdoors = models.FloatField()
    in_car = models.FloatField()
    on_bus = models.FloatField()
    home = models.FloatField()
    restaurant = models.FloatField()
    at_party = models.FloatField()
    at_bar = models.FloatField()
    beach = models.FloatField()
    at_gym = models.FloatField()
    elevator = models.FloatField()
    at_school = models.FloatField()
    anomaly = models.BooleanField()

    # ! Class Functions
    def __str__(self):
        return self.id + '\t' + \
                self.uuid + '\t' + \
                self.data_record + 't'