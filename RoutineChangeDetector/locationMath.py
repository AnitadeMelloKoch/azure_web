import math
import numpy
from geopy.distance import great_circle
import sys
#  Set of methods to get data from the location array

def num_valid_updates(arr):
    return len(arr)

def get_location_data(arr):
    num_updates = num_valid_updates(arr)
    lat_arr = []
    long_arr = []
    alt_arr = []
    speed_arr = []
    acc_arr = []
    alt_acc_arr = []
    for coords in arr:
        lat_arr.append(coords["latitude"])
        long_arr.append(coords["longitude"])
        alt_arr.append(coords["altitude"])
        speed_arr.append(coords["speed"])
        acc_arr.append(coords["accuracy"])
        alt_acc_arr.append(coords["altitudeAccuracy"])
    log_lat_range = (_range(lat_arr)) * 1000 # ? The data looks like this, not a log
    log_long_range = (_range(long_arr)) * 1000 # ? The data looks like this, not a log
    min_alt = min(alt_arr)
    max_alt = max(alt_arr)
    min_spd = min(speed_arr)
    max_spd = max(speed_arr)
    best_horiz_acc = min(acc_arr)
    best_vert_acc = min(alt_acc_arr)
    diameter = calcDiameter(lat_arr, long_arr)
    log_diameter = 0
    if not diameter == 0:
        log_diameter = math.log(diameter)
    else:
        log_diameter = math.log(sys.float_info.min)

    return (num_updates, log_lat_range, log_long_range, \
            min_alt, max_alt, min_spd, max_spd, best_horiz_acc, \
            best_vert_acc, diameter, log_diameter)

def _range(arr):
    return (max(arr) - min(arr))

def calcDiameter(lat_arr, long_arr):
    diam_arr = []
    for i in range(len(lat_arr)):
        for j in range(len(lat_arr)):
            d = great_circle((lat_arr[i], long_arr[i]), (lat_arr[j], long_arr[j])).m
            diam_arr.append(d)
    return max(diam_arr)

def get_quick_location_data(arr):
    lat_arr = []
    long_arr = []
    t_arr = []
    for coords in arr:
        lat_arr.append(coords["latitude"])
        long_arr.append(coords["longitude"])
        t_arr.append(coords["timestamp"])
    std_lat = numpy.std(lat_arr)
    std_long = numpy.std(long_arr)
    lat_change = lat_arr[-1] - lat_arr[0]
    long_change = long_arr[-1] - long_arr[0]
    mean_abs_lat_deriv = calcDeriv(lat_arr, t_arr)
    mean_abs_long_deriv = calcDeriv(long_arr, t_arr)
    return (std_lat, std_long, lat_change, long_change, \
            mean_abs_lat_deriv, mean_abs_long_deriv)

def calcDeriv(arr, t_arr):
    derivs = []
    for i in range(len(arr)-1):
        t_diff = t_arr[i+1] - t_arr[i]
        if t_diff == 0:
            return 0
        d = abs((arr[i+1] - arr[i])/((t_diff)/1000))
        derivs.append(d)
    return numpy.average(derivs)