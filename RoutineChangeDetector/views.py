from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserData, UserRoutine
from .serializers import UserDataSerializer, UserRoutineSerializer #, RecieveDataSerialiser

import json
from .locationMath import get_location_data, get_quick_location_data

@api_view(['GET', 'POST'])
def user_data_list(request):
    """
    GET: List all UserData entries.

    POST: Prints the posted data.
    """
    if request.method == 'GET':
        user_data = UserData.objects.all()
        serializer = UserDataSerializer(user_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        acceleration = request.data["acceleration"]
        audio = request.data["audio"]
        gyroscope = request.data["gyroscope"]
        location = request.data["location"]
        magnetometer = request.data["magnetometer"]
        battery_level = request.data["batteryLevel"]
        battery_is_plugged = request.data["batteryIsPlugged"]
        app_state = request.data["appState"]
        network = request.data["network"]
        phone_state = request.data["phoneState"]
        ringer_mode = request.data["ringerMode"]
        uuid = request.data["uuid"]
        timestamp = request.data["timestamp"]
        day = request.data["day"]
        hour = request.data["hour"]
        minute = request.data["minute"]

        # * Model
        model = UserData()

        # * Acceleration
        model.raw_acc_magnitude_stats_mean = 0
        model.raw_acc_magnitude_stats_std = 0
        model.raw_acc_magnitude_stats_moment3 = 0
        model.raw_acc_magnitude_stats_moment4 = 0
        model.raw_acc_magnitude_stats_percentile25 = 0
        model.raw_acc_magnitude_stats_percentile50 = 0
        model.raw_acc_magnitude_stats_percentile75 = 0
        model.raw_acc_magnitude_stats_value_entropy = 0
        model.raw_acc_magnitude_stats_time_entropy = 0
        model.raw_acc_magnitude_spectrum_log_energy_band0 = 0
        model.raw_acc_magnitude_spectrum_log_energy_band1 = 0
        model.raw_acc_magnitude_spectrum_log_energy_band2 = 0
        model.raw_acc_magnitude_spectrum_log_energy_band3 = 0
        model.raw_acc_magnitude_spectrum_log_energy_band4 = 0
        model.raw_acc_magnitude_spectrum_spectral_entropy = 0
        model.raw_acc_magnitude_autocorrelation_period = 0
        model.raw_acc_magnitude_autocorrelation_normalized_ac = 0
        model.raw_acc_3d_mean_x = 0
        model.raw_acc_3d_mean_y = 0
        model.raw_acc_3d_mean_z = 0
        model.raw_acc_3d_std_x = 0
        model.raw_acc_3d_std_y = 0
        model.raw_acc_3d_std_z = 0
        model.raw_acc_3d_ro_xy = 0
        model.raw_acc_3d_ro_xz = 0
        model.raw_acc_3d_ro_yz = 0

        # * Gyroscope
        model.proc_gyro_magnitude_stats_mean = 0
        model.proc_gyro_magnitude_stats_std = 0
        model.proc_gyro_magnitude_stats_moment3 = 0
        model.proc_gyro_magnitude_stats_moment4 = 0
        model.proc_gyro_magnitude_stats_percentile25 = 0
        model.proc_gyro_magnitude_stats_percentile50 = 0
        model.proc_gyro_magnitude_stats_percentile75 = 0
        model.proc_gyro_magnitude_stats_value_entropy = 0
        model.proc_gyro_magnitude_stats_time_entropy = 0
        model.proc_gyro_magnitude_spectrum_log_energy_band0 = 0
        model.proc_gyro_magnitude_spectrum_log_energy_band1 = 0
        model.proc_gyro_magnitude_spectrum_log_energy_band2 = 0
        model.proc_gyro_magnitude_spectrum_log_energy_band3 = 0
        model.proc_gyro_magnitude_spectrum_log_energy_band4 = 0
        model.proc_gyro_magnitude_spectrum_spectral_entropy = 0
        model.proc_gyro_magnitude_autocorrelation_period = 0
        model.proc_gyro_magnitude_autocorrelation_normalized_ac = 0
        model.proc_gyro_3d_mean_x = 0
        model.proc_gyro_3d_mean_y = 0
        model.proc_gyro_3d_mean_z = 0
        model.proc_gyro_3d_std_x = 0
        model.proc_gyro_3d_std_y = 0
        model.proc_gyro_3d_std_z = 0
        model.proc_gyro_3d_ro_xy = 0
        model.proc_gyro_3d_ro_xz = 0
        model.proc_gyro_3d_ro_yz = 0

        # * Magnetometer Fields
        model.raw_magnet_magnitude_stats_mean = 0
        model.raw_magnet_magnitude_stats_std = 0
        model.raw_magnet_magnitude_stats_moment3 = 0
        model.raw_magnet_magnitude_stats_moment4 = 0
        model.raw_magnet_magnitude_stats_percentile25 = 0
        model.raw_magnet_magnitude_stats_percentile50 = 0
        model.raw_magnet_magnitude_stats_percentile75 = 0
        model.raw_magnet_magnitude_stats_value_entropy = 0
        model.raw_magnet_magnitude_stats_time_entropy = 0
        model.raw_magnet_magnitude_spectrum_log_energy_band0 = 0
        model.raw_magnet_magnitude_spectrum_log_energy_band1 = 0
        model.raw_magnet_magnitude_spectrum_log_energy_band2 = 0
        model.raw_magnet_magnitude_spectrum_log_energy_band3 = 0
        model.raw_magnet_magnitude_spectrum_log_energy_band4 = 0
        model.raw_magnet_magnitude_spectrum_spectral_entropy = 0
        model.raw_magnet_magnitude_autocorrelation_period = 0
        model.raw_magnet_magnitude_autocorrelation_normalized_ac = 0
        model.raw_magnet_3d_mean_x = 0
        model.raw_magnet_3d_mean_y = 0
        model.raw_magnet_3d_mean_z = 0
        model.raw_magnet_3d_std_x = 0
        model.raw_magnet_3d_std_y = 0
        model.raw_magnet_3d_std_z = 0
        model.raw_magnet_3d_ro_xy = 0
        model.raw_magnet_3d_ro_xz = 0
        model.raw_magnet_3d_ro_yz = 0
        model.raw_magnet_avr_cosine_similarity_lag_range0 = 0
        model.raw_magnet_avr_cosine_similarity_lag_range1 = 0
        model.raw_magnet_avr_cosine_similarity_lag_range2 = 0
        model.raw_magnet_avr_cosine_similarity_lag_range3 = 0
        model.raw_magnet_avr_cosine_similarity_lag_range4 = 0

        # * Watch Fields
        model.watch_acc_magnitude_stats_mean = 0
        model.watch_acc_magnitude_stats_std = 0
        model.watch_acc_magnitude_stats_moment3 = 0
        model.watch_acc_magnitude_stats_moment4 = 0
        model.watch_acc_magnitude_stats_percentile25 = 0
        model.watch_acc_magnitude_stats_percentile50 = 0
        model.watch_acc_magnitude_stats_percentile75 = 0
        model.watch_acc_magnitude_stats_value_entropy = 0
        model.watch_acc_magnitude_stats_time_entropy = 0
        model.watch_acc_magnitude_spectrum_log_energy_band0 = 0
        model.watch_acc_magnitude_spectrum_log_energy_band1 = 0
        model.watch_acc_magnitude_spectrum_log_energy_band2 = 0
        model.watch_acc_magnitude_spectrum_log_energy_band3 = 0
        model.watch_acc_magnitude_spectrum_log_energy_band4 = 0
        model.watch_acc_magnitude_spectrum_spectral_entropy = 0
        model.watch_acc_magnitude_autocorrelation_period = 0
        model.watch_acc_magnitude_autocorrelation_normalized_ac = 0
        model.watch_acc_3d_mean_x = 0
        model.watch_acc_3d_mean_y = 0
        model.watch_acc_3d_mean_z = 0
        model.watch_acc_3d_std_x = 0
        model.watch_acc_3d_std_y = 0
        model.watch_acc_3d_std_z = 0
        model.watch_acc_3d_ro_xy = 0
        model.watch_acc_3d_ro_xz = 0
        model.watch_acc_3d_ro_yz = 0
        model.watch_acc_spectrum_x_log_energy_band0 = 0
        model.watch_acc_spectrum_x_log_energy_band1 = 0
        model.watch_acc_spectrum_x_log_energy_band2 = 0
        model.watch_acc_spectrum_x_log_energy_band3 = 0
        model.watch_acc_spectrum_x_log_energy_band4 = 0
        model.watch_acc_spectrum_y_log_energy_band0 = 0
        model.watch_acc_spectrum_y_log_energy_band1 = 0
        model.watch_acc_spectrum_y_log_energy_band2 = 0
        model.watch_acc_spectrum_y_log_energy_band3 = 0
        model.watch_acc_spectrum_y_log_energy_band4 = 0
        model.watch_acc_spectrum_z_log_energy_band0 = 0
        model.watch_acc_spectrum_z_log_energy_band1 = 0
        model.watch_acc_spectrum_z_log_energy_band2 = 0
        model.watch_acc_spectrum_z_log_energy_band3 = 0
        model.watch_acc_spectrum_z_log_energy_band4 = 0
        model.watch_acc_relative_directions_avr_cosine_similarity_lag_range0 = 0
        model.watch_acc_relative_directions_avr_cosine_similarity_lag_range1 = 0
        model.watch_acc_relative_directions_avr_cosine_similarity_lag_range2 = 0
        model.watch_acc_relative_directions_avr_cosine_similarity_lag_range3 = 0
        model.watch_acc_relative_directions_avr_cosine_similarity_lag_range4 = 0
        model.watch_heading_mean_cos = 0
        model.watch_heading_std_cos = 0
        model.watch_heading_mom3_cos = 0
        model.watch_heading_mom4_cos = 0
        model.watch_heading_mean_sin = 0
        model.watch_heading_std_sin = 0
        model.watch_heading_mom3_sin = 0
        model.watch_heading_mom4_sin = 0
        model.watch_heading_entropy_8bins = 0

        # * Location Fields

        num_updates, log_lat_range, log_long_range, \
            min_alt, max_alt, min_spd, max_spd, best_horiz_acc, \
            best_vert_acc, diameter, log_diameter = get_location_data(location)

        std_lat, std_long, lat_change, long_change, \
            mean_abs_lat_deriv, mean_abs_long_deriv = get_quick_location_data(location)

        model.location_num_valid_updates = num_updates
        model.location_log_latitude_range = log_lat_range
        model.location_log_longitude_range = log_long_range
        model.location_min_altitude = min_alt
        model.location_max_altitude = max_alt
        model.location_min_speed = min_spd
        model.location_max_speed = max_spd
        model.location_best_horizontal_accuracy = best_horiz_acc
        model.location_best_vertical_accuracy = best_vert_acc
        model.location_diameter = diameter
        model.location_log_diameter = log_diameter
        model.location_quick_features_std_lat = std_lat
        model.location_quick_features_std_long = std_long
        model.location_quick_features_lat_change = lat_change
        model.location_quick_features_long_change = long_change
        model.location_quick_features_mean_abs_lat_deriv = mean_abs_lat_deriv
        model.location_quick_features_mean_abs_long_deriv = mean_abs_long_deriv

        # * Audio Fields
        model.audio_naive_mfcc0_mean = 0
        model.audio_naive_mfcc1_mean = 0
        model.audio_naive_mfcc2_mean = 0
        model.audio_naive_mfcc3_mean = 0
        model.audio_naive_mfcc4_mean = 0
        model.audio_naive_mfcc5_mean = 0
        model.audio_naive_mfcc6_mean = 0
        model.audio_naive_mfcc7_mean = 0
        model.audio_naive_mfcc8_mean = 0
        model.audio_naive_mfcc9_mean = 0
        model.audio_naive_mfcc10_mean = 0
        model.audio_naive_mfcc11_mean = 0
        model.audio_naive_mfcc12_mean = 0
        model.audio_naive_mfcc0_std = 0
        model.audio_naive_mfcc1_std = 0
        model.audio_naive_mfcc2_std = 0
        model.audio_naive_mfcc3_std = 0
        model.audio_naive_mfcc4_std = 0
        model.audio_naive_mfcc5_std = 0
        model.audio_naive_mfcc6_std = 0
        model.audio_naive_mfcc7_std = 0
        model.audio_naive_mfcc8_std = 0
        model.audio_naive_mfcc9_std = 0
        model.audio_naive_mfcc10_std = 0
        model.audio_naive_mfcc11_std = 0
        model.audio_naive_mfcc12_std = 0
        model.audio_properties_max_abs_value = 0
        model.audio_properties_normalization_multiplier = 0

        # * App State
        if app_state == "ACTIVE":
            model.discrete_app_state_is_active = True
        elif app_state == "BACKGROUND":
            model.discrete_app_state_is_background = True
        elif app_state == "INACTIVE":
            model.discrete_app_state_is_inactive = True
        else:
            model.discrete_app_state_missing = True

        # * Battery Plugged
        model.discrete_battery_plugged_missing = True

        # * Battery State
        if battery_is_plugged:      
            if battery_level == 100:
                model.discrete_battery_state_is_not_charging = True
                model.discrete_battery_state_is_full = True
            else: 
                model.discrete_battery_state_is_charging = True
        else:
            model.discrete_battery_state_is_unplugged = True
            model.discrete_battery_state_is_not_charging = True
            model.discrete_battery_state_is_discharging = True
            if battery_level == 100:
                model.discrete_battery_state_is_full = True

        # * Network State
        if network == "none":
            model.discrete_wifi_status_is_not_reachable = True
        elif network == "wifi":
            model.discrete_wifi_status_is_reachable_via_wifi = True
        elif network == "unknown":
            model.discrete_wifi_status_missing = True
        else: 
            model.discrete_wifi_status_is_reachable_via_wwan = True

        # * Phone State
        if phone_state == "IDLE":
            model.discrete_on_the_phone_is_False = True
        else:
            model.discrete_on_the_phone_is_True = True

        # * Ringer Mode
        if ringer_mode == "RINGER_MODE_NORMAL":
            model.discrete_ringer_mode_is_normal = True
        elif ringer_mode == "RINGER_MODE_VIBRATE":
            model.discrete_ringer_mode_is_silent_with_vibrate = True
        else:
            model.discrete_ringer_mode_is_silent_no_vibrate = True

        # * Misc
        model.uuid = uuid
        model.timestamp = timestamp

        # * Low Frequency Measurements
        model.lf_measurements_light = 0
        model.lf_measurements_pressure = 0
        model.lf_measurements_proximity_cm = 0
        model.lf_measurements_proximity = 0
        model.lf_measurements_relative_humidity = 0
        model.lf_measurements_battery_level = 0
        model.lf_measurements_screen_brightness = 0
        model.lf_measurements_temperature_ambient = 0

        # * Time
        if hour >= 0 and hour < 6:
            model.discrete_time_of_day_between0and6 = True
        elif hour >= 6 and hour < 12:
            model.discrete_time_of_day_between6and12 = True
        elif hour >= 12 and hour < 18:
            model.discrete_time_of_day_between12and18 = True
        elif hour >= 18 and hour < 24:
            model.discrete_time_of_day_between18and24 = True

        if hour >= 3 and hour < 9:
            model.discrete_time_of_day_between3and9 = True        
        elif hour >= 9 and hour < 15:
            model.discrete_time_of_day_between9and15 = True       
        elif hour >= 15 and hour < 21:
            model.discrete_time_of_day_between15and21 = True
        elif hour >= 21 and hour < 3:
            model.discrete_time_of_day_between21and3 = True

        # * Done
        serializer = UserDataSerializer(model)
        if serializer.is_valid:
            model.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
       
