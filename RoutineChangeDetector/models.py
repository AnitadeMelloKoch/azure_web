from django.db import models
from .statistics import * 
import numpy
from .locationMath import get_location_data, get_quick_location_data


# Create your models here.


class UserData(models.Model):

    # * Record ID Fields
    # id = models.BigAutoField(primary_key=True)
    record_id = models.CharField(max_length=100, primary_key=True)
    uuid = models.CharField(max_length=100, editable=False)
    timestamp = models.BigIntegerField(editable=False)
    classified = models.BooleanField()



    # * Accelerometer Fields
    raw_acc_magnitude_stats_mean = models.FloatField(blank=True)
    raw_acc_magnitude_stats_std = models.FloatField(blank=True)
    raw_acc_magnitude_stats_moment3 = models.FloatField(blank=True)
    raw_acc_magnitude_stats_moment4 = models.FloatField(blank=True)
    raw_acc_magnitude_stats_percentile25 = models.FloatField(blank=True)
    raw_acc_magnitude_stats_percentile50 = models.FloatField(blank=True)
    raw_acc_magnitude_stats_percentile75 = models.FloatField(blank=True)
    raw_acc_magnitude_stats_value_entropy = models.FloatField(blank=True)
    raw_acc_magnitude_stats_time_entropy = models.FloatField(blank=True)
    raw_acc_magnitude_spectrum_log_energy_band0 = models.FloatField(blank=True)
    raw_acc_magnitude_spectrum_log_energy_band1 = models.FloatField(blank=True)
    raw_acc_magnitude_spectrum_log_energy_band2 = models.FloatField(blank=True)
    raw_acc_magnitude_spectrum_log_energy_band3 = models.FloatField(blank=True)
    raw_acc_magnitude_spectrum_log_energy_band4 = models.FloatField(blank=True)
    raw_acc_magnitude_spectrum_spectral_entropy = models.FloatField(blank=True)
    raw_acc_magnitude_autocorrelation_period = models.FloatField(blank=True)
    raw_acc_magnitude_autocorrelation_normalized_ac = models.FloatField(blank=True)
    raw_acc_3d_mean_x = models.FloatField(blank=True)
    raw_acc_3d_mean_y = models.FloatField(blank=True)
    raw_acc_3d_mean_z = models.FloatField(blank=True)
    raw_acc_3d_std_x = models.FloatField(blank=True)
    raw_acc_3d_std_y = models.FloatField(blank=True)
    raw_acc_3d_std_z = models.FloatField(blank=True)
    raw_acc_3d_ro_xy = models.FloatField(blank=True)
    raw_acc_3d_ro_xz = models.FloatField(blank=True)
    raw_acc_3d_ro_yz = models.FloatField(blank=True)



    # * Gyroscope Fields
    proc_gyro_magnitude_stats_mean = models.FloatField(blank=True)
    proc_gyro_magnitude_stats_std = models.FloatField(blank=True)
    proc_gyro_magnitude_stats_moment3 = models.FloatField(blank=True)
    proc_gyro_magnitude_stats_moment4 = models.FloatField(blank=True)
    proc_gyro_magnitude_stats_percentile25 = models.FloatField(blank=True)
    proc_gyro_magnitude_stats_percentile50 = models.FloatField(blank=True)
    proc_gyro_magnitude_stats_percentile75 = models.FloatField(blank=True)
    proc_gyro_magnitude_stats_value_entropy = models.FloatField(blank=True)
    proc_gyro_magnitude_stats_time_entropy = models.FloatField(blank=True)
    proc_gyro_magnitude_spectrum_log_energy_band0 = models.FloatField(blank=True)
    proc_gyro_magnitude_spectrum_log_energy_band1 = models.FloatField(blank=True)
    proc_gyro_magnitude_spectrum_log_energy_band2 = models.FloatField(blank=True)
    proc_gyro_magnitude_spectrum_log_energy_band3 = models.FloatField(blank=True)
    proc_gyro_magnitude_spectrum_log_energy_band4 = models.FloatField(blank=True)
    proc_gyro_magnitude_spectrum_spectral_entropy = models.FloatField(blank=True)
    proc_gyro_magnitude_autocorrelation_period = models.FloatField(blank=True)
    proc_gyro_magnitude_autocorrelation_normalized_ac = models.FloatField(blank=True)
    proc_gyro_3d_mean_x = models.FloatField(blank=True)
    proc_gyro_3d_mean_y = models.FloatField(blank=True)
    proc_gyro_3d_mean_z = models.FloatField(blank=True)
    proc_gyro_3d_std_x = models.FloatField(blank=True)
    proc_gyro_3d_std_y = models.FloatField(blank=True)
    proc_gyro_3d_std_z = models.FloatField(blank=True)
    proc_gyro_3d_ro_xy = models.FloatField(blank=True)
    proc_gyro_3d_ro_xz = models.FloatField(blank=True)
    proc_gyro_3d_ro_yz = models.FloatField(blank=True)



    # * Magnetometer Fields
    raw_magnet_magnitude_stats_mean = models.FloatField(blank=True)
    raw_magnet_magnitude_stats_std = models.FloatField(blank=True)
    raw_magnet_magnitude_stats_moment3 = models.FloatField(blank=True)
    raw_magnet_magnitude_stats_moment4 = models.FloatField(blank=True)
    raw_magnet_magnitude_stats_percentile25 = models.FloatField(blank=True)
    raw_magnet_magnitude_stats_percentile50 = models.FloatField(blank=True)
    raw_magnet_magnitude_stats_percentile75 = models.FloatField(blank=True)
    raw_magnet_magnitude_stats_value_entropy = models.FloatField(blank=True)
    raw_magnet_magnitude_stats_time_entropy = models.FloatField(blank=True)
    raw_magnet_magnitude_spectrum_log_energy_band0 = models.FloatField(blank=True)
    raw_magnet_magnitude_spectrum_log_energy_band1 = models.FloatField(blank=True)
    raw_magnet_magnitude_spectrum_log_energy_band2 = models.FloatField(blank=True)
    raw_magnet_magnitude_spectrum_log_energy_band3 = models.FloatField(blank=True)
    raw_magnet_magnitude_spectrum_log_energy_band4 = models.FloatField(blank=True)
    raw_magnet_magnitude_spectrum_spectral_entropy = models.FloatField(blank=True)
    raw_magnet_magnitude_autocorrelation_period = models.FloatField(blank=True)
    raw_magnet_magnitude_autocorrelation_normalized_ac = models.FloatField(blank=True)
    raw_magnet_3d_mean_x = models.FloatField(blank=True)
    raw_magnet_3d_mean_y = models.FloatField(blank=True)
    raw_magnet_3d_mean_z = models.FloatField(blank=True)
    raw_magnet_3d_std_x = models.FloatField(blank=True)
    raw_magnet_3d_std_y = models.FloatField(blank=True)
    raw_magnet_3d_std_z = models.FloatField(blank=True)
    raw_magnet_3d_ro_xy = models.FloatField(blank=True)
    raw_magnet_3d_ro_xz = models.FloatField(blank=True)
    raw_magnet_3d_ro_yz = models.FloatField(blank=True)
    raw_magnet_avr_cosine_similarity_lag_range0 = models.FloatField(blank=True)
    raw_magnet_avr_cosine_similarity_lag_range1 = models.FloatField(blank=True)
    raw_magnet_avr_cosine_similarity_lag_range2 = models.FloatField(blank=True)
    raw_magnet_avr_cosine_similarity_lag_range3 = models.FloatField(blank=True)
    raw_magnet_avr_cosine_similarity_lag_range4 = models.FloatField(blank=True)



    # * Watch Fields
    watch_acc_magnitude_stats_mean = models.FloatField(blank=True)
    watch_acc_magnitude_stats_std = models.FloatField(blank=True)
    watch_acc_magnitude_stats_moment3 = models.FloatField(blank=True)
    watch_acc_magnitude_stats_moment4 = models.FloatField(blank=True)
    watch_acc_magnitude_stats_percentile25 = models.FloatField(blank=True)
    watch_acc_magnitude_stats_percentile50 = models.FloatField(blank=True)
    watch_acc_magnitude_stats_percentile75 = models.FloatField(blank=True)
    watch_acc_magnitude_stats_value_entropy = models.FloatField(blank=True)
    watch_acc_magnitude_stats_time_entropy = models.FloatField(blank=True)
    watch_acc_magnitude_spectrum_log_energy_band0 = models.FloatField(blank=True)
    watch_acc_magnitude_spectrum_log_energy_band1 = models.FloatField(blank=True)
    watch_acc_magnitude_spectrum_log_energy_band2 = models.FloatField(blank=True)
    watch_acc_magnitude_spectrum_log_energy_band3 = models.FloatField(blank=True)
    watch_acc_magnitude_spectrum_log_energy_band4 = models.FloatField(blank=True)
    watch_acc_magnitude_spectrum_spectral_entropy = models.FloatField(blank=True)
    watch_acc_magnitude_autocorrelation_period = models.FloatField(blank=True)
    watch_acc_magnitude_autocorrelation_normalized_ac = models.FloatField(blank=True)
    watch_acc_3d_mean_x = models.FloatField(blank=True)
    watch_acc_3d_mean_y = models.FloatField(blank=True)
    watch_acc_3d_mean_z = models.FloatField(blank=True)
    watch_acc_3d_std_x = models.FloatField(blank=True)
    watch_acc_3d_std_y = models.FloatField(blank=True)
    watch_acc_3d_std_z = models.FloatField(blank=True)
    watch_acc_3d_ro_xy = models.FloatField(blank=True)
    watch_acc_3d_ro_xz = models.FloatField(blank=True)
    watch_acc_3d_ro_yz = models.FloatField(blank=True)
    watch_acc_spectrum_x_log_energy_band0 = models.FloatField(blank=True)
    watch_acc_spectrum_x_log_energy_band1 = models.FloatField(blank=True)
    watch_acc_spectrum_x_log_energy_band2 = models.FloatField(blank=True)
    watch_acc_spectrum_x_log_energy_band3 = models.FloatField(blank=True)
    watch_acc_spectrum_x_log_energy_band4 = models.FloatField(blank=True)
    watch_acc_spectrum_y_log_energy_band0 = models.FloatField(blank=True)
    watch_acc_spectrum_y_log_energy_band1 = models.FloatField(blank=True)
    watch_acc_spectrum_y_log_energy_band2 = models.FloatField(blank=True)
    watch_acc_spectrum_y_log_energy_band3 = models.FloatField(blank=True)
    watch_acc_spectrum_y_log_energy_band4 = models.FloatField(blank=True)
    watch_acc_spectrum_z_log_energy_band0 = models.FloatField(blank=True)
    watch_acc_spectrum_z_log_energy_band1 = models.FloatField(blank=True)
    watch_acc_spectrum_z_log_energy_band2 = models.FloatField(blank=True)
    watch_acc_spectrum_z_log_energy_band3 = models.FloatField(blank=True)
    watch_acc_spectrum_z_log_energy_band4 = models.FloatField(blank=True)
    watch_acc_relative_directions_avr_cosine_similarity_lag_range0 = models.FloatField(blank=True)
    watch_acc_relative_directions_avr_cosine_similarity_lag_range1 = models.FloatField(blank=True)
    watch_acc_relative_directions_avr_cosine_similarity_lag_range2 = models.FloatField(blank=True)
    watch_acc_relative_directions_avr_cosine_similarity_lag_range3 = models.FloatField(blank=True)
    watch_acc_relative_directions_avr_cosine_similarity_lag_range4 = models.FloatField(blank=True)
    watch_heading_mean_cos = models.FloatField(blank=True)
    watch_heading_std_cos = models.FloatField(blank=True)
    watch_heading_mom3_cos = models.FloatField(blank=True)
    watch_heading_mom4_cos = models.FloatField(blank=True)
    watch_heading_mean_sin = models.FloatField(blank=True)
    watch_heading_std_sin = models.FloatField(blank=True)
    watch_heading_mom3_sin = models.FloatField(blank=True)
    watch_heading_mom4_sin = models.FloatField(blank=True)
    watch_heading_entropy_8bins = models.FloatField(blank=True)



    # * Location Fields
    location_num_valid_updates = models.FloatField(blank=True)
    location_log_latitude_range = models.FloatField(blank=True)
    location_log_longitude_range = models.FloatField(blank=True)
    location_min_altitude = models.FloatField(blank=True)
    location_max_altitude = models.FloatField(blank=True)
    location_min_speed = models.FloatField(blank=True)
    location_max_speed = models.FloatField(blank=True)
    location_best_horizontal_accuracy = models.FloatField(blank=True)
    location_best_vertical_accuracy = models.FloatField(blank=True)
    location_diameter = models.FloatField(blank=True)
    location_log_diameter = models.FloatField(blank=True)
    location_quick_features_std_lat = models.FloatField(blank=True)
    location_quick_features_std_long = models.FloatField(blank=True)
    location_quick_features_lat_change = models.FloatField(blank=True)
    location_quick_features_long_change = models.FloatField(blank=True)
    location_quick_features_mean_abs_lat_deriv = models.FloatField(blank=True)
    location_quick_features_mean_abs_long_deriv = models.FloatField(blank=True)



    # * Audio Fields
    audio_naive_mfcc0_mean = models.FloatField(blank=True)
    audio_naive_mfcc1_mean = models.FloatField(blank=True)
    audio_naive_mfcc2_mean = models.FloatField(blank=True)
    audio_naive_mfcc3_mean = models.FloatField(blank=True)
    audio_naive_mfcc4_mean = models.FloatField(blank=True)
    audio_naive_mfcc5_mean = models.FloatField(blank=True)
    audio_naive_mfcc6_mean = models.FloatField(blank=True)
    audio_naive_mfcc7_mean = models.FloatField(blank=True)
    audio_naive_mfcc8_mean = models.FloatField(blank=True)
    audio_naive_mfcc9_mean = models.FloatField(blank=True)
    audio_naive_mfcc10_mean = models.FloatField(blank=True)
    audio_naive_mfcc11_mean = models.FloatField(blank=True)
    audio_naive_mfcc12_mean = models.FloatField(blank=True)
    audio_naive_mfcc0_std = models.FloatField(blank=True)
    audio_naive_mfcc1_std = models.FloatField(blank=True)
    audio_naive_mfcc2_std = models.FloatField(blank=True)
    audio_naive_mfcc3_std = models.FloatField(blank=True)
    audio_naive_mfcc4_std = models.FloatField(blank=True)
    audio_naive_mfcc5_std = models.FloatField(blank=True)
    audio_naive_mfcc6_std = models.FloatField(blank=True)
    audio_naive_mfcc7_std = models.FloatField(blank=True)
    audio_naive_mfcc8_std = models.FloatField(blank=True)
    audio_naive_mfcc9_std = models.FloatField(blank=True)
    audio_naive_mfcc10_std = models.FloatField(blank=True)
    audio_naive_mfcc11_std = models.FloatField(blank=True)
    audio_naive_mfcc12_std = models.FloatField(blank=True)
    audio_properties_max_abs_value = models.FloatField(blank=True)
    audio_properties_normalization_multiplier = models.FloatField(blank=True)



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
    lf_measurements_light = models.FloatField(blank=True)
    lf_measurements_pressure = models.FloatField(blank=True)
    lf_measurements_proximity_cm = models.FloatField(blank=True)
    lf_measurements_proximity = models.FloatField(blank=True)
    lf_measurements_relative_humidity = models.FloatField(blank=True)
    lf_measurements_battery_level = models.FloatField(blank=True)
    lf_measurements_screen_brightness = models.FloatField(blank=True)
    lf_measurements_temperature_ambient = models.FloatField(blank=True)



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
    # def __init__(self):
    #     super(UserData, self).__init__()
    
    def setValues(self, dataDict):
        # super(UserData, self).__init__()
        
        acceleration = dataDict["acceleration"]
        mfcc = dataDict["mfcc"]
        gyroscope = dataDict["gyroscope"]
        location = dataDict["location"]
        magnetometer = dataDict["magnetometer"]
        battery_level = dataDict["batteryLevel"]
        battery_is_plugged = dataDict["batteryIsPlugged"]
        app_state = dataDict["appState"]
        network = dataDict["network"]
        phone_state = dataDict["phoneState"]
        ringer_mode = dataDict["ringerMode"]
        uuid = dataDict["uuid"]
        timestamp = dataDict["timestamp"]
        day = dataDict["day"]
        hour = dataDict["hour"]
        minute = dataDict["minute"]

        self.record_id = uuid + str(timestamp)
        self.classified = False

        # * Acceleration
        calc_acc = False
        for idx in range(len(acceleration)):
            if not acceleration["x"][idx] == 0 or not acceleration["y"][idx] == 0 or not acceleration["z"][idx] == 0:
                calc_acc = True
                break       
        if calc_acc:
            self.raw_acc_magnitude_stats_mean = mean_mag(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_stats_std = std_mag(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_stats_moment3 = moment3(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_stats_moment4 = moment4(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_stats_percentile25 = percentile25(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_stats_percentile50 = percentile50(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_stats_percentile75 = percentile75(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_stats_value_entropy = valueEntropy(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_stats_time_entropy = timeEntropy(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_spectrum_log_energy_band0 = energyband0(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_spectrum_log_energy_band1 = energyband1(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_spectrum_log_energy_band2 = energyband2(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_spectrum_log_energy_band3 = energyband3(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_spectrum_log_energy_band4 = energyband4(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_magnitude_spectrum_spectral_entropy = spectral_entropy(acceleration["x"], acceleration["y"], acceleration["z"])
            acc_period, acc_ac = autocorr(acceleration["x"], acceleration["y"], acceleration["z"], acceleration["timestamp"])
            self.raw_acc_magnitude_autocorrelation_period = acc_period
            self.raw_acc_magnitude_autocorrelation_normalized_ac = acc_ac
            acc_mean_x, acc_mean_y, acc_mean_z = mean_dir(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_3d_mean_x = acc_mean_x
            self.raw_acc_3d_mean_y = acc_mean_y
            self.raw_acc_3d_mean_z = acc_mean_z
            acc_std_x, acc_std_y, acc_std_z = std_dev_dir(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_3d_std_x = acc_std_x
            self.raw_acc_3d_std_y = acc_std_y
            self.raw_acc_3d_std_z = acc_std_z
            acc_xy, acc_xz, acc_yz = correlation_coeff(acceleration["x"], acceleration["y"], acceleration["z"])
            self.raw_acc_3d_ro_xy = acc_xy
            self.raw_acc_3d_ro_xz = acc_xz
            self.raw_acc_3d_ro_yz = acc_yz
        else:
            self.raw_acc_magnitude_stats_mean = 0
            self.raw_acc_magnitude_stats_std = 0
            self.raw_acc_magnitude_stats_moment3 = 0
            self.raw_acc_magnitude_stats_moment4 = 0
            self.raw_acc_magnitude_stats_percentile25 = 0
            self.raw_acc_magnitude_stats_percentile50 = 0
            self.raw_acc_magnitude_stats_percentile75 = 0
            self.raw_acc_magnitude_stats_value_entropy = 0
            self.raw_acc_magnitude_stats_time_entropy = 0
            self.raw_acc_magnitude_spectrum_log_energy_band0 = 0
            self.raw_acc_magnitude_spectrum_log_energy_band1 = 0
            self.raw_acc_magnitude_spectrum_log_energy_band2 = 0
            self.raw_acc_magnitude_spectrum_log_energy_band3 = 0
            self.raw_acc_magnitude_spectrum_log_energy_band4 = 0
            self.raw_acc_magnitude_spectrum_spectral_entropy = 0
            self.raw_acc_magnitude_autocorrelation_period = 0
            self.raw_acc_magnitude_autocorrelation_normalized_ac = 0
            self.raw_acc_3d_mean_x = 0
            self.raw_acc_3d_mean_y = 0
            self.raw_acc_3d_mean_z = 0
            self.raw_acc_3d_std_x = 0
            self.raw_acc_3d_std_y = 0
            self.raw_acc_3d_std_z = 0
            self.raw_acc_3d_ro_xy = 0
            self.raw_acc_3d_ro_xz = 0
            self.raw_acc_3d_ro_yz = 0



        # * Gyroscope
        calc_gyr = False
        for idx in range(len(gyroscope)):
            if not gyroscope["x"][idx] == 0 or not gyroscope["y"][idx] == 0 or not gyroscope["z"][idx] == 0:
                calc_gyr = True
                break       
        if calc_gyr:
            self.proc_gyro_magnitude_stats_mean = mean_mag(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_stats_std = std_mag(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_stats_moment3 = moment3(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_stats_moment4 = moment4(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_stats_percentile25 = percentile25(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_stats_percentile50 = percentile50(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_stats_percentile75 = percentile75(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_stats_value_entropy = valueEntropy(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_stats_time_entropy = timeEntropy(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_spectrum_log_energy_band0 = energyband0(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_spectrum_log_energy_band1 = energyband1(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_spectrum_log_energy_band2 = energyband2(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_spectrum_log_energy_band3 = energyband3(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_spectrum_log_energy_band4 = energyband4(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_magnitude_spectrum_spectral_entropy = spectral_entropy(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            gyr_period, gyr_ac = autocorr(gyroscope["x"], gyroscope["y"], gyroscope["z"], gyroscope["timestamp"])
            self.proc_gyro_magnitude_autocorrelation_period = gyr_period
            self.proc_gyro_magnitude_autocorrelation_normalized_ac = gyr_ac
            gyr_mean_x, gyr_mean_y, gyr_mean_z = mean_dir(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_3d_mean_x = gyr_mean_x
            self.proc_gyro_3d_mean_y = gyr_mean_y
            self.proc_gyro_3d_mean_z = gyr_mean_z
            gyr_std_x, gyr_std_y, gyr_std_z = std_dev_dir(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_3d_std_x = gyr_std_x
            self.proc_gyro_3d_std_y = gyr_std_y
            self.proc_gyro_3d_std_z = gyr_std_z
            gyr_xy, gyr_xz, gyr_yz = correlation_coeff(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            self.proc_gyro_3d_ro_xy = gyr_xy
            self.proc_gyro_3d_ro_xz = gyr_xz
            self.proc_gyro_3d_ro_yz = gyr_yz
        else:
            self.proc_gyro_magnitude_stats_mean = 0
            self.proc_gyro_magnitude_stats_std = 0
            self.proc_gyro_magnitude_stats_moment3 = 0
            self.proc_gyro_magnitude_stats_moment4 = 0
            self.proc_gyro_magnitude_stats_percentile25 = 0
            self.proc_gyro_magnitude_stats_percentile50 = 0
            self.proc_gyro_magnitude_stats_percentile75 = 0
            self.proc_gyro_magnitude_stats_value_entropy = 0
            self.proc_gyro_magnitude_stats_time_entropy = 0
            self.proc_gyro_magnitude_spectrum_log_energy_band0 = 0
            self.proc_gyro_magnitude_spectrum_log_energy_band1 = 0
            self.proc_gyro_magnitude_spectrum_log_energy_band2 = 0
            self.proc_gyro_magnitude_spectrum_log_energy_band3 = 0
            self.proc_gyro_magnitude_spectrum_log_energy_band4 = 0
            self.proc_gyro_magnitude_spectrum_spectral_entropy = 0
            self.proc_gyro_magnitude_autocorrelation_period = 0
            self.proc_gyro_magnitude_autocorrelation_normalized_ac = 0
            self.proc_gyro_3d_mean_x = 0
            self.proc_gyro_3d_mean_y = 0
            self.proc_gyro_3d_mean_z = 0
            self.proc_gyro_3d_std_x = 0
            self.proc_gyro_3d_std_y = 0
            self.proc_gyro_3d_std_z = 0
            self.proc_gyro_3d_ro_xy = 0
            self.proc_gyro_3d_ro_xz = 0
            self.proc_gyro_3d_ro_yz = 0



        # * Magnetometer Fields
        calc_mag = False
        for idx in range(len(magnetometer)):
            if not magnetometer["x"][idx] == 0 or not magnetometer["y"][idx] == 0 or not magnetometer["z"][idx] == 0:
                calc_mag = True
                break   
        if calc_mag:


            # ! Expanding the magnetometer to the same dimensions as the other two sensors.
            new_magn_dict = {
                "x": [],
                "y": [],
                "z": [],
                "timestamp": acceleration["timestamp"]
            }
            magn_x = magnetometer["x"][0]
            magn_y = magnetometer["y"][0]
            magn_z = magnetometer["z"][0]
            old_idx = 0
            for idx in range(len(new_magn_dict["timestamp"])):
                if old_idx < len(magnetometer["timestamp"]):
                    if new_magn_dict["timestamp"][idx] < magnetometer["timestamp"][old_idx]:
                        new_magn_dict["x"].append(magn_x)
                        new_magn_dict["y"].append(magn_y)
                        new_magn_dict["z"].append(magn_z)
                    else:
                        magn_x = magnetometer["x"][old_idx]
                        magn_y = magnetometer["y"][old_idx]
                        magn_z = magnetometer["z"][old_idx]
                        old_idx = old_idx + 1
                        new_magn_dict["x"].append(magn_x)
                        new_magn_dict["y"].append(magn_y)
                        new_magn_dict["z"].append(magn_z)
                else:
                    new_magn_dict["x"].append(magn_x)
                    new_magn_dict["y"].append(magn_y)
                    new_magn_dict["z"].append(magn_z)
            magnetometer = new_magn_dict

            self.raw_magnet_magnitude_stats_mean = mean_mag(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_stats_std = std_mag(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_stats_moment3 = moment3(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_stats_moment4 = moment4(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_stats_percentile25 = percentile25(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_stats_percentile50 = percentile50(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_stats_percentile75 = percentile75(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_stats_value_entropy = valueEntropy(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_stats_time_entropy = timeEntropy(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_spectrum_log_energy_band0 = energyband0(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_spectrum_log_energy_band1 = energyband1(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_spectrum_log_energy_band2 = energyband2(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_spectrum_log_energy_band3 = energyband3(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_spectrum_log_energy_band4 = energyband4(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_magnitude_spectrum_spectral_entropy = spectral_entropy(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            mag_period, mag_ac = autocorr(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
            self.raw_magnet_magnitude_autocorrelation_period = mag_period
            self.raw_magnet_magnitude_autocorrelation_normalized_ac = mag_ac
            mag_mean_x, mag_mean_y, mag_mean_z = mean_dir(magnetometer["x"], magnetometer["y"], magnetometer["z"])     
            self.raw_magnet_3d_mean_x = mag_mean_x
            self.raw_magnet_3d_mean_y = mag_mean_y
            self.raw_magnet_3d_mean_z = mag_mean_z
            mag_std_x, mag_std_y, mag_std_z = std_dev_dir(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_3d_std_x = mag_std_x
            self.raw_magnet_3d_std_y = mag_std_y
            self.raw_magnet_3d_std_z = mag_std_z
            mag_xy, mag_xz, mag_yz = correlation_coeff(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            self.raw_magnet_3d_ro_xy = mag_xy
            self.raw_magnet_3d_ro_xz = mag_xz
            self.raw_magnet_3d_ro_yz = mag_yz
            self.raw_magnet_avr_cosine_similarity_lag_range0 = cos_similarity_0(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
            self.raw_magnet_avr_cosine_similarity_lag_range1 = cos_similarity_1(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
            self.raw_magnet_avr_cosine_similarity_lag_range2 = cos_similarity_2(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
            self.raw_magnet_avr_cosine_similarity_lag_range3 = cos_similarity_3(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
            self.raw_magnet_avr_cosine_similarity_lag_range4 = cos_similarity_4(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
        else:
            self.raw_magnet_magnitude_stats_mean = 0
            self.raw_magnet_magnitude_stats_std = 0
            self.raw_magnet_magnitude_stats_moment3 = 0
            self.raw_magnet_magnitude_stats_moment4 = 0
            self.raw_magnet_magnitude_stats_percentile25 = 0
            self.raw_magnet_magnitude_stats_percentile50 = 0
            self.raw_magnet_magnitude_stats_percentile75 = 0
            self.raw_magnet_magnitude_stats_value_entropy = 0
            self.raw_magnet_magnitude_stats_time_entropy = 0
            self.raw_magnet_magnitude_spectrum_log_energy_band0 = 0
            self.raw_magnet_magnitude_spectrum_log_energy_band1 = 0
            self.raw_magnet_magnitude_spectrum_log_energy_band2 = 0
            self.raw_magnet_magnitude_spectrum_log_energy_band3 = 0
            self.raw_magnet_magnitude_spectrum_log_energy_band4 = 0
            self.raw_magnet_magnitude_spectrum_spectral_entropy = 0
            self.raw_magnet_magnitude_autocorrelation_period = 0
            self.raw_magnet_magnitude_autocorrelation_normalized_ac = 0
            self.raw_magnet_3d_mean_x = 0
            self.raw_magnet_3d_mean_y = 0
            self.raw_magnet_3d_mean_z = 0
            self.raw_magnet_3d_std_x = 0
            self.raw_magnet_3d_std_y = 0
            self.raw_magnet_3d_std_z = 0
            self.raw_magnet_3d_ro_xy = 0
            self.raw_magnet_3d_ro_xz = 0
            self.raw_magnet_3d_ro_yz = 0
            self.raw_magnet_avr_cosine_similarity_lag_range0 = 0
            self.raw_magnet_avr_cosine_similarity_lag_range1 = 0
            self.raw_magnet_avr_cosine_similarity_lag_range2 = 0
            self.raw_magnet_avr_cosine_similarity_lag_range3 = 0
            self.raw_magnet_avr_cosine_similarity_lag_range4 = 0



        # * Watch Fields
        self.watch_acc_magnitude_stats_mean = 0
        self.watch_acc_magnitude_stats_std = 0
        self.watch_acc_magnitude_stats_moment3 = 0
        self.watch_acc_magnitude_stats_moment4 = 0
        self.watch_acc_magnitude_stats_percentile25 = 0
        self.watch_acc_magnitude_stats_percentile50 = 0
        self.watch_acc_magnitude_stats_percentile75 = 0
        self.watch_acc_magnitude_stats_value_entropy = 0
        self.watch_acc_magnitude_stats_time_entropy = 0
        self.watch_acc_magnitude_spectrum_log_energy_band0 = 0
        self.watch_acc_magnitude_spectrum_log_energy_band1 = 0
        self.watch_acc_magnitude_spectrum_log_energy_band2 = 0
        self.watch_acc_magnitude_spectrum_log_energy_band3 = 0
        self.watch_acc_magnitude_spectrum_log_energy_band4 = 0
        self.watch_acc_magnitude_spectrum_spectral_entropy = 0
        self.watch_acc_magnitude_autocorrelation_period = 0
        self.watch_acc_magnitude_autocorrelation_normalized_ac = 0
        self.watch_acc_3d_mean_x = 0
        self.watch_acc_3d_mean_y = 0
        self.watch_acc_3d_mean_z = 0
        self.watch_acc_3d_std_x = 0
        self.watch_acc_3d_std_y = 0
        self.watch_acc_3d_std_z = 0
        self.watch_acc_3d_ro_xy = 0
        self.watch_acc_3d_ro_xz = 0
        self.watch_acc_3d_ro_yz = 0
        self.watch_acc_spectrum_x_log_energy_band0 = 0
        self.watch_acc_spectrum_x_log_energy_band1 = 0
        self.watch_acc_spectrum_x_log_energy_band2 = 0
        self.watch_acc_spectrum_x_log_energy_band3 = 0
        self.watch_acc_spectrum_x_log_energy_band4 = 0
        self.watch_acc_spectrum_y_log_energy_band0 = 0
        self.watch_acc_spectrum_y_log_energy_band1 = 0
        self.watch_acc_spectrum_y_log_energy_band2 = 0
        self.watch_acc_spectrum_y_log_energy_band3 = 0
        self.watch_acc_spectrum_y_log_energy_band4 = 0
        self.watch_acc_spectrum_z_log_energy_band0 = 0
        self.watch_acc_spectrum_z_log_energy_band1 = 0
        self.watch_acc_spectrum_z_log_energy_band2 = 0
        self.watch_acc_spectrum_z_log_energy_band3 = 0
        self.watch_acc_spectrum_z_log_energy_band4 = 0
        self.watch_acc_relative_directions_avr_cosine_similarity_lag_range0 = 0
        self.watch_acc_relative_directions_avr_cosine_similarity_lag_range1 = 0
        self.watch_acc_relative_directions_avr_cosine_similarity_lag_range2 = 0
        self.watch_acc_relative_directions_avr_cosine_similarity_lag_range3 = 0
        self.watch_acc_relative_directions_avr_cosine_similarity_lag_range4 = 0
        self.watch_heading_mean_cos = 0
        self.watch_heading_std_cos = 0
        self.watch_heading_mom3_cos = 0
        self.watch_heading_mom4_cos = 0
        self.watch_heading_mean_sin = 0
        self.watch_heading_std_sin = 0
        self.watch_heading_mom3_sin = 0
        self.watch_heading_mom4_sin = 0
        self.watch_heading_entropy_8bins = 0



        # * Location Fields
        if not len(location) < 2:
            num_updates, log_lat_range, log_long_range, \
                min_alt, max_alt, min_spd, max_spd, best_horiz_acc, \
                best_vert_acc, diameter, log_diameter = get_location_data(location)
            std_lat, std_long, lat_change, long_change, \
                mean_abs_lat_deriv, mean_abs_long_deriv = get_quick_location_data(location)
            self.location_num_valid_updates = num_updates
            self.location_log_latitude_range = log_lat_range
            self.location_log_longitude_range = log_long_range
            self.location_min_altitude = min_alt
            self.location_max_altitude = max_alt
            self.location_min_speed = min_spd
            self.location_max_speed = max_spd
            self.location_best_horizontal_accuracy = best_horiz_acc
            self.location_best_vertical_accuracy = best_vert_acc
            self.location_diameter = diameter
            self.location_log_diameter = log_diameter
            self.location_quick_features_std_lat = std_lat
            self.location_quick_features_std_long = std_long
            self.location_quick_features_lat_change = lat_change
            self.location_quick_features_long_change = long_change
            self.location_quick_features_mean_abs_lat_deriv = mean_abs_lat_deriv
            self.location_quick_features_mean_abs_long_deriv = mean_abs_long_deriv
        else:
            self.location_num_valid_updates = 0
            self.location_log_latitude_range = 0
            self.location_log_longitude_range = 0
            self.location_min_altitude = 0
            self.location_max_altitude = 0
            self.location_min_speed = 0
            self.location_max_speed = 0
            self.location_best_horizontal_accuracy = 0
            self.location_best_vertical_accuracy = 0
            self.location_diameter = 0
            self.location_log_diameter = 0
            self.location_quick_features_std_lat = 0
            self.location_quick_features_std_long = 0
            self.location_quick_features_lat_change = 0
            self.location_quick_features_long_change = 0
            self.location_quick_features_mean_abs_lat_deriv = 0
            self.location_quick_features_mean_abs_long_deriv = 0


        # * Audio Fields
        self.audio_naive_mfcc0_mean = numpy.nanmean(mfcc["mfcc0"])
        self.audio_naive_mfcc1_mean = numpy.nanmean(mfcc["mfcc1"])
        self.audio_naive_mfcc2_mean = numpy.nanmean(mfcc["mfcc2"])
        self.audio_naive_mfcc3_mean = numpy.nanmean(mfcc["mfcc3"])
        self.audio_naive_mfcc4_mean = numpy.nanmean(mfcc["mfcc4"])
        self.audio_naive_mfcc5_mean = numpy.nanmean(mfcc["mfcc5"])
        self.audio_naive_mfcc6_mean = numpy.nanmean(mfcc["mfcc6"])
        self.audio_naive_mfcc7_mean = numpy.nanmean(mfcc["mfcc7"])
        self.audio_naive_mfcc8_mean = numpy.nanmean(mfcc["mfcc8"])
        self.audio_naive_mfcc9_mean = numpy.nanmean(mfcc["mfcc9"])
        self.audio_naive_mfcc10_mean = numpy.nanmean(mfcc["mfcc10"])
        self.audio_naive_mfcc11_mean = numpy.nanmean(mfcc["mfcc11"])
        self.audio_naive_mfcc12_mean = numpy.nanmean(mfcc["mfcc12"])
        self.audio_naive_mfcc0_std = numpy.nanstd(mfcc["mfcc0"])
        self.audio_naive_mfcc1_std = numpy.nanstd(mfcc["mfcc1"])
        self.audio_naive_mfcc2_std = numpy.nanstd(mfcc["mfcc2"])
        self.audio_naive_mfcc3_std = numpy.nanstd(mfcc["mfcc3"])
        self.audio_naive_mfcc4_std = numpy.nanstd(mfcc["mfcc4"])
        self.audio_naive_mfcc5_std = numpy.nanstd(mfcc["mfcc5"])
        self.audio_naive_mfcc6_std = numpy.nanstd(mfcc["mfcc6"])
        self.audio_naive_mfcc7_std = numpy.nanstd(mfcc["mfcc7"])
        self.audio_naive_mfcc8_std = numpy.nanstd(mfcc["mfcc8"])
        self.audio_naive_mfcc9_std = numpy.nanstd(mfcc["mfcc9"])
        self.audio_naive_mfcc10_std = numpy.nanstd(mfcc["mfcc10"])
        self.audio_naive_mfcc11_std = numpy.nanstd(mfcc["mfcc11"])
        self.audio_naive_mfcc12_std = numpy.nanstd(mfcc["mfcc12"])
        self.audio_properties_max_abs_value = -mfcc["normalizationMult"]
        self.audio_properties_normalization_multiplier = mfcc["normalizationMult"]

        # * App State
        if app_state == "ACTIVE":
            self.discrete_app_state_is_active = True
        elif app_state == "BACKGROUND":
            self.discrete_app_state_is_background = True
        elif app_state == "INACTIVE":
            self.discrete_app_state_is_inactive = True
        else:
            self.discrete_app_state_missing = True

        # * Battery Plugged
        self.discrete_battery_plugged_missing = True

        # * Battery State
        if battery_is_plugged:      
            if battery_level == 100:
                self.discrete_battery_state_is_not_charging = True
                self.discrete_battery_state_is_full = True
            else: 
                self.discrete_battery_state_is_charging = True
        else:
            self.discrete_battery_state_is_unplugged = True
            self.discrete_battery_state_is_not_charging = True
            self.discrete_battery_state_is_discharging = True
            if battery_level == 100:
                self.discrete_battery_state_is_full = True

        # * Network State
        if network == "none":
            self.discrete_wifi_status_is_not_reachable = True
        elif network == "wifi":
            self.discrete_wifi_status_is_reachable_via_wifi = True
        elif network == "unknown":
            self.discrete_wifi_status_missing = True
        else: 
            self.discrete_wifi_status_is_reachable_via_wwan = True

        # * Phone State
        if phone_state == "IDLE":
            self.discrete_on_the_phone_is_False = True
        else:
            self.discrete_on_the_phone_is_True = True

        # * Ringer Mode
        if ringer_mode == "RINGER_MODE_NORMAL":
            self.discrete_ringer_mode_is_normal = True
        elif ringer_mode == "RINGER_MODE_VIBRATE":
            self.discrete_ringer_mode_is_silent_with_vibrate = True
        else:
            self.discrete_ringer_mode_is_silent_no_vibrate = True

        # * Misc
        self.uuid = uuid
        self.timestamp = timestamp

        # * Low Frequency Measurements
        self.lf_measurements_light = 0
        self.lf_measurements_pressure = 0
        self.lf_measurements_proximity_cm = 0
        self.lf_measurements_proximity = 0
        self.lf_measurements_relative_humidity = 0
        self.lf_measurements_battery_level = 0
        self.lf_measurements_screen_brightness = 0
        self.lf_measurements_temperature_ambient = 0

        # * Time
        if hour >= 0 and hour < 6:
            self.discrete_time_of_day_between0and6 = True
        elif hour >= 6 and hour < 12:
            self.discrete_time_of_day_between6and12 = True
        elif hour >= 12 and hour < 18:
            self.discrete_time_of_day_between12and18 = True
        elif hour >= 18 and hour < 24:
            self.discrete_time_of_day_between18and24 = True

        if hour >= 3 and hour < 9:
            self.discrete_time_of_day_between3and9 = True        
        elif hour >= 9 and hour < 15:
            self.discrete_time_of_day_between9and15 = True       
        elif hour >= 15 and hour < 21:
            self.discrete_time_of_day_between15and21 = True
        elif hour >= 21 and hour < 3:
            self.discrete_time_of_day_between21and3 = True

    def __str__(self):
        returnText = ''
        returnText += str(self.record_id) + '\t' + \
                        self.uuid + '\t' + \
                        str(self.timestamp) + '\t' + \
                        str(self.raw_acc_magnitude_stats_mean) + '\t' + \
                        str(self.proc_gyro_magnitude_stats_mean)
        return returnText

class UserRoutine(models.Model):
    # * IDs
    # id = models.BigAutoField(primary_key=True)
    routine_id = models.CharField(max_length=100, primary_key=True)
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
    anomaly = models.NullBooleanField()

    # ! Class Functions
    def initialise(self, uuid, timestamp, data_record, day, hour, minute):
        self.routine_id = uuid + str(timestamp)
        self.uuid = uuid
        self.data_record = data_record
        self.day = day
        self.hour = hour
        self.minute = minute

        self.lying_down = 0
        self.sitting = 0
        self.walking = 0
        self.running = 0
        self.bicycling = 0
        self.sleeping = 0
        self.driving_driver = 0
        self.driving_pass = 0
        self.exercise = 0
        self.shopping = 0
        self.strolling = 0
        self.stairs_up = 0
        self.stairs_down = 0
        self.standing = 0
        self.lab_work = 0
        self.in_class = 0
        self.in_meeting = 0
        self.cooking = 0
        self.drinking_alcohol = 0
        self.shower = 0
        self.cleaning = 0
        self.laundry = 0
        self.washing_dishes = 0
        self.watch_tv = 0
        self.surf_internet = 0
        self.singing = 0
        self.talking = 0
        self.computer_work = 0
        self.eating = 0
        self.toilet = 0
        self.grooming = 0
        self.dressing = 0
        self.with_coworker = 0
        self.with_friends = 0
        self.main_workplace = 0
        self.indoors = 0
        self.outdoors = 0
        self.in_car = 0
        self.on_bus = 0
        self.home = 0
        self.restaurant = 0
        self.at_party = 0
        self.at_bar = 0
        self.beach = 0
        self.at_gym = 0
        self.elevator = 0
        self.at_school = 0
        self.anomaly = None
        print("Created Routine Model")

    def updatePredictions(self, predictions_arr):
        self.lying_down = predictions_arr[0]
        self.sitting = predictions_arr[1]
        self.walking = predictions_arr[2]
        self.running = predictions_arr[3]
        self.bicycling = predictions_arr[4]
        self.sleeping = predictions_arr[5]
        self.driving_driver = predictions_arr[6]
        self.driving_pass = predictions_arr[7]
        self.exercise = predictions_arr[8]
        self.shopping = predictions_arr[9]
        self.strolling = predictions_arr[10]
        self.stairs_up = predictions_arr[11]
        self.stairs_down = predictions_arr[12]
        self.standing = predictions_arr[13]
        self.lab_work = predictions_arr[14]
        self.in_class = predictions_arr[15]
        self.in_meeting = predictions_arr[16]
        self.cooking = predictions_arr[17]
        self.drinking_alcohol = predictions_arr[18]
        self.shower = predictions_arr[19]
        self.cleaning = predictions_arr[20]
        self.laundry = predictions_arr[21]
        self.washing_dishes = predictions_arr[22]
        self.watch_tv = predictions_arr[23]
        self.surf_internet = predictions_arr[24]
        self.singing = predictions_arr[25]
        self.talking = predictions_arr[26]
        self.computer_work = predictions_arr[27]
        self.eating = predictions_arr[28]
        self.toilet = predictions_arr[29]
        self.grooming = predictions_arr[30]
        self.dressing = predictions_arr[31]
        self.with_coworker = predictions_arr[32]
        self.with_friends = predictions_arr[33]
        self.main_workplace = predictions_arr[34]
        self.indoors = predictions_arr[35]
        self.outdoors = predictions_arr[36]
        self.in_car = predictions_arr[37]
        self.on_bus = predictions_arr[38]
        self.home = predictions_arr[39]
        self.restaurant = predictions_arr[40]
        self.at_party = predictions_arr[41]
        self.at_bar = predictions_arr[42]
        self.beach = predictions_arr[43]
        self.at_gym = predictions_arr[44]
        self.elevator = predictions_arr[45]
        self.at_school = predictions_arr[46]

    def setAnomaly(self, b):
        self.anomaly = b

    def __str__(self):
        return str(self.record_id) + '\t' + \
                self.uuid + '\t' + \
                str(self.data_record) + 't'