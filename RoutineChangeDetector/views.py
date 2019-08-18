from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserData, UserRoutine
from .serializers import UserDataSerializer, UserRoutineSerializer #, RecieveDataSerialiser

import json
from .locationMath import get_location_data, get_quick_location_data
from .statistics import *
import numpy

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
        mfcc = request.data["mfcc"]
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
        calc_acc = False
        for idx in range(len(acceleration)):
            if not acceleration["x"][idx] == 0 or not acceleration["y"][idx] == 0 or not acceleration["z"][idx] == 0:
                calc_acc = True
                break       
        if calc_acc:
            model.raw_acc_magnitude_stats_mean = mean_mag(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_stats_std = std_mag(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_stats_moment3 = moment3(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_stats_moment4 = moment4(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_stats_percentile25 = percentile25(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_stats_percentile50 = percentile50(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_stats_percentile75 = percentile75(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_stats_value_entropy = valueEntropy(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_stats_time_entropy = timeEntropy(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_spectrum_log_energy_band0 = energyband0(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_spectrum_log_energy_band1 = energyband1(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_spectrum_log_energy_band2 = energyband2(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_spectrum_log_energy_band3 = energyband3(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_spectrum_log_energy_band4 = energyband4(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_magnitude_spectrum_spectral_entropy = spectral_entropy(acceleration["x"], acceleration["y"], acceleration["z"])
            acc_period, acc_ac = autocorr(acceleration["x"], acceleration["y"], acceleration["z"], acceleration["timestamp"])
            model.raw_acc_magnitude_autocorrelation_period = acc_period
            model.raw_acc_magnitude_autocorrelation_normalized_ac = acc_ac
            acc_mean_x, acc_mean_y, acc_mean_z = mean_dir(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_3d_mean_x = acc_mean_x
            model.raw_acc_3d_mean_y = acc_mean_y
            model.raw_acc_3d_mean_z = acc_mean_z
            acc_std_x, acc_std_y, acc_std_z = std_dev_dir(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_3d_std_x = acc_std_x
            model.raw_acc_3d_std_y = acc_std_y
            model.raw_acc_3d_std_z = acc_std_z
            acc_xy, acc_xz, acc_yz = correlation_coeff(acceleration["x"], acceleration["y"], acceleration["z"])
            model.raw_acc_3d_ro_xy = acc_xy
            model.raw_acc_3d_ro_xz = acc_xz
            model.raw_acc_3d_ro_yz = acc_yz
        else:
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
        calc_gyr = False
        for idx in range(len(gyroscope)):
            if not gyroscope["x"][idx] == 0 or not gyroscope["y"][idx] == 0 or not gyroscope["z"][idx] == 0:
                calc_gyr = True
                break       
        if calc_gyr:
            model.proc_gyro_magnitude_stats_mean = mean_mag(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_stats_std = std_mag(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_stats_moment3 = moment3(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_stats_moment4 = moment4(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_stats_percentile25 = percentile25(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_stats_percentile50 = percentile50(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_stats_percentile75 = percentile75(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_stats_value_entropy = valueEntropy(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_stats_time_entropy = timeEntropy(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_spectrum_log_energy_band0 = energyband0(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_spectrum_log_energy_band1 = energyband1(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_spectrum_log_energy_band2 = energyband2(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_spectrum_log_energy_band3 = energyband3(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_spectrum_log_energy_band4 = energyband4(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_magnitude_spectrum_spectral_entropy = spectral_entropy(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            gyr_period, gyr_ac = autocorr(gyroscope["x"], gyroscope["y"], gyroscope["z"], gyroscope["timestamp"])
            model.proc_gyro_magnitude_autocorrelation_period = gyr_period
            model.proc_gyro_magnitude_autocorrelation_normalized_ac = gyr_ac
            gyr_mean_x, gyr_mean_y, gyr_mean_z = mean_dir(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_3d_mean_x = gyr_mean_x
            model.proc_gyro_3d_mean_y = gyr_mean_y
            model.proc_gyro_3d_mean_z = gyr_mean_z
            gyr_std_x, gyr_std_y, gyr_std_z = std_dev_dir(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_3d_std_x = gyr_std_x
            model.proc_gyro_3d_std_y = gyr_std_y
            model.proc_gyro_3d_std_z = gyr_std_z
            gyr_xy, gyr_xz, gyr_yz = correlation_coeff(gyroscope["x"], gyroscope["y"], gyroscope["z"])
            model.proc_gyro_3d_ro_xy = gyr_xy
            model.proc_gyro_3d_ro_xz = gyr_xz
            model.proc_gyro_3d_ro_yz = gyr_yz
        else:
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

            model.raw_magnet_magnitude_stats_mean = mean_mag(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_stats_std = std_mag(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_stats_moment3 = moment3(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_stats_moment4 = moment4(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_stats_percentile25 = percentile25(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_stats_percentile50 = percentile50(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_stats_percentile75 = percentile75(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_stats_value_entropy = valueEntropy(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_stats_time_entropy = timeEntropy(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_spectrum_log_energy_band0 = energyband0(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_spectrum_log_energy_band1 = energyband1(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_spectrum_log_energy_band2 = energyband2(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_spectrum_log_energy_band3 = energyband3(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_spectrum_log_energy_band4 = energyband4(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_magnitude_spectrum_spectral_entropy = spectral_entropy(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            mag_period, mag_ac = autocorr(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
            model.raw_magnet_magnitude_autocorrelation_period = mag_period
            model.raw_magnet_magnitude_autocorrelation_normalized_ac = mag_ac
            mag_mean_x, mag_mean_y, mag_mean_z = mean_dir(magnetometer["x"], magnetometer["y"], magnetometer["z"])     
            model.raw_magnet_3d_mean_x = mag_mean_x
            model.raw_magnet_3d_mean_y = mag_mean_y
            model.raw_magnet_3d_mean_z = mag_mean_z
            mag_std_x, mag_std_y, mag_std_z = std_dev_dir(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_3d_std_x = mag_std_x
            model.raw_magnet_3d_std_y = mag_std_y
            model.raw_magnet_3d_std_z = mag_std_z
            mag_xy, mag_xz, mag_yz = correlation_coeff(magnetometer["x"], magnetometer["y"], magnetometer["z"])
            model.raw_magnet_3d_ro_xy = mag_xy
            model.raw_magnet_3d_ro_xz = mag_xz
            model.raw_magnet_3d_ro_yz = mag_yz
            model.raw_magnet_avr_cosine_similarity_lag_range0 = cos_similarity_0(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
            model.raw_magnet_avr_cosine_similarity_lag_range1 = cos_similarity_1(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
            model.raw_magnet_avr_cosine_similarity_lag_range2 = cos_similarity_2(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
            model.raw_magnet_avr_cosine_similarity_lag_range3 = cos_similarity_3(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
            model.raw_magnet_avr_cosine_similarity_lag_range4 = cos_similarity_4(magnetometer["x"], magnetometer["y"], magnetometer["z"], magnetometer["timestamp"])
        else:
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
        print(mfcc)
        model.audio_naive_mfcc0_mean = numpy.nanmean(mfcc["mfcc0"])
        model.audio_naive_mfcc1_mean = numpy.nanmean(mfcc["mfcc1"])
        model.audio_naive_mfcc2_mean = numpy.nanmean(mfcc["mfcc2"])
        model.audio_naive_mfcc3_mean = numpy.nanmean(mfcc["mfcc3"])
        model.audio_naive_mfcc4_mean = numpy.nanmean(mfcc["mfcc4"])
        model.audio_naive_mfcc5_mean = numpy.nanmean(mfcc["mfcc5"])
        model.audio_naive_mfcc6_mean = numpy.nanmean(mfcc["mfcc6"])
        model.audio_naive_mfcc7_mean = numpy.nanmean(mfcc["mfcc7"])
        model.audio_naive_mfcc8_mean = numpy.nanmean(mfcc["mfcc8"])
        model.audio_naive_mfcc9_mean = numpy.nanmean(mfcc["mfcc9"])
        model.audio_naive_mfcc10_mean = numpy.nanmean(mfcc["mfcc10"])
        model.audio_naive_mfcc11_mean = numpy.nanmean(mfcc["mfcc11"])
        model.audio_naive_mfcc12_mean = numpy.nanmean(mfcc["mfcc12"])
        model.audio_naive_mfcc0_std = numpy.nanstd(mfcc["mfcc0"])
        model.audio_naive_mfcc1_std = numpy.nanstd(mfcc["mfcc1"])
        model.audio_naive_mfcc2_std = numpy.nanstd(mfcc["mfcc2"])
        model.audio_naive_mfcc3_std = numpy.nanstd(mfcc["mfcc3"])
        model.audio_naive_mfcc4_std = numpy.nanstd(mfcc["mfcc4"])
        model.audio_naive_mfcc5_std = numpy.nanstd(mfcc["mfcc5"])
        model.audio_naive_mfcc6_std = numpy.nanstd(mfcc["mfcc6"])
        model.audio_naive_mfcc7_std = numpy.nanstd(mfcc["mfcc7"])
        model.audio_naive_mfcc8_std = numpy.nanstd(mfcc["mfcc8"])
        model.audio_naive_mfcc9_std = numpy.nanstd(mfcc["mfcc9"])
        model.audio_naive_mfcc10_std = numpy.nanstd(mfcc["mfcc10"])
        model.audio_naive_mfcc11_std = numpy.nanstd(mfcc["mfcc11"])
        model.audio_naive_mfcc12_std = numpy.nanstd(mfcc["mfcc12"])
        model.audio_properties_max_abs_value = -mfcc["normalizationMult"]
        model.audio_properties_normalization_multiplier = mfcc["normalizationMult"]

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
            # model.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
