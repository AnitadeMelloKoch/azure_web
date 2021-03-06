import scipy as scipy
import numpy as np
from scipy import stats, signal

# working
def mean_dir(x, y, z):
    x_mean = np.nanmean(x)
    y_mean = np.nanmean(y)
    z_mean = np.nanmean(z)
    return (x_mean, y_mean, z_mean)

# working
def std_dev_dir(x, y, z):
    x_std = np.nanstd(x)
    y_std = np.nanstd(y)
    z_std = np.nanstd(z)
    return (x_std, y_std, z_std)

# working
def mean_mag(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    mean_mag = np.mean(mag)

    return mean_mag

# working
def std_mag(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    std_mag = np.std(mag)

    return std_mag

# close enough
def moment3(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    return scipy.stats.moment(mag, 3)

# close enough
def moment4(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    return scipy.stats.moment(mag, 4)

# working
def percentile25(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    return np.percentile(mag, 25)

# working
def percentile50(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    return np.percentile(mag, 50)

# working
def percentile75(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    return np.percentile(mag, 75)

# working
def valueEntropy(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    hist, _ = np.histogram(mag, bins=20, density=True)
    total = np.sum(hist)
    H = 0
    for x in range(len(hist)):
        if not hist[x] == 0 and not total == 0: 
            H = H - (hist[x]/total)*np.log((hist[x]/total))
    return H

# working
def timeEntropy(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    total = np.sum(mag)
    S = 0
    for x in range(len(mag)):
        if not mag[x] == 0 and not total == 0: 
            S = S - (mag[x]/total)*np.log(mag[x]/total)

    return S

# close enough
def spectral_entropy(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    _, PSD = scipy.signal.periodogram(mag, 40)
    total = np.sum(PSD)
    S = 0
    for x in range(len(PSD)):
        if not PSD[x] == 0 and not total == 0:
            S = S - (PSD[x]/total)*np.log(PSD[x]/total)
    return S

# not working
def energyband0(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag, 40)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] >= 0 and f[x] <= 0.5):
            energy = energy + PSD[x]
    if energy == 0:
        return 0
    return np.log(energy)

# not working
def energyband1(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag, 40)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 0.5 and f[x] <= 1):
            energy = energy + PSD[x]
    if energy == 0:
        return 0
    return np.log(energy)

# not working
def energyband2(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag, 40)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 1 and f[x] <= 3):
            energy = energy + PSD[x]
    if energy == 0:
        return 0
    return np.log(energy)

# not working
def energyband3(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag, 40)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 3 and f[x] <= 5):
            energy = energy + PSD[x]
    if energy == 0:
        return 0
    return np.log(energy)

# not working
def energyband4(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag, 40)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 5):
            energy = energy + PSD[x]
    if energy == 0:
        return 0
    return np.log(energy)

# not working
def autocorr(x, y, z, timesteps):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    mean = np.mean(mag)
    for x in range(len(mag)):
        mag[x] = mag[x] - mean

    corr = np.correlate(mag, mag, mode='full')
    autocorr = corr[corr.size // 2:]
    lag0 = autocorr[0]
    if lag0 == 0:
        lag0 = 1
    for x in range(len(autocorr)):
        autocorr[x] = autocorr[x]/lag0
    found = False
    index = 0
    previous = 1000
    maxVal = 0
    
    try:
        while ((not found) and (index < len(autocorr))):
            if(previous > autocorr[index]):
                previous = autocorr[index]
                index += 1
            else:
                maxVal = np.argmax(autocorr[index:])
                found = True
        if ((not found) and (index == len(autocorr - 1))):
            return 0, 0
        period = (timesteps[index:][maxVal] - timesteps[0]) / 1000 # To convert to seconds from milliseconds
        return (period),(autocorr[index:][maxVal])
    except:
        return 0,0

# working
def correlation_coeff(x, y, z):
    corr_coeff = np.corrcoef([x,y,z])
    if np.isnan(corr_coeff[1,0]):
        corr_coeff[1,0] = 0
    if np.isnan(corr_coeff[2,0]):
        corr_coeff[2,0] = 0
    if np.isnan(corr_coeff[1,2]):
        corr_coeff[1,2] = 0
    return corr_coeff[1,0], corr_coeff[2, 0], corr_coeff[1,2]

# working
def cos_similarity_0(x, y, z, timesteps):
    sim = 0
    tot = 0
    while(tot < 1000):
        x1 = int(np.random.randint(low = 0, high = len(x)))
        x2 = int(np.random.randint(low = 0, high = len(x)))
        time = abs(timesteps[x1] - timesteps[x2])
        if(time >= 0 and time < 500):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[x1], y[x1], z[x1]],[x[x2], y[x2], z[x2]])
    if tot == 0:
        return 0
    return 1 - sim/tot

def cos_similarity_1(x, y, z, timesteps):
    sim = 0
    tot = 0
    count = 0
    while(tot < 1000 and count < 7000):
        count += 1
        x1 = int(np.random.randint(low = 0, high = len(x)))
        x2 = int(np.random.randint(low = 0, high = len(x)))
        time = abs(timesteps[x1] - timesteps[x2])
        if(time >= 500 and time < 1000):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[x1], y[x1], z[x1]],[x[x2], y[x2], z[x2]])
    if tot == 0:
        return 0
    return 1 - sim/tot

def cos_similarity_2(x, y, z, timesteps):
    sim = 0
    tot = 0
    count = 0
    while(tot < 1000 and count < 7000):
        count += 1
        x1 = int(np.random.randint(low = 0, high = len(x)))
        x2 = int(np.random.randint(low = 0, high = len(x)))
        time = abs(timesteps[x1] - timesteps[x2])
        if(time >= 1000 and time < 5000):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[x1], y[x1], z[x1]],[x[x2], y[x2], z[x2]])
    if tot == 0:
        return 0
    return 1 - sim/tot

def cos_similarity_3(x, y, z, timesteps):
    sim = 0
    tot = 0
    count = 0
    while(tot < 1000 and count < 7000):
        count += 1
        x1 = int(np.random.randint(low = 0, high = len(x)))
        x2 = int(np.random.randint(low = 0, high = len(x)))
        time = abs(timesteps[x1] - timesteps[x2])
        if(time >= 5000 and time < 10000):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[x1], y[x1], z[x1]],[x[x2], y[x2], z[x2]])
    if tot == 0:
        return 0
    return 1 - sim/tot

def cos_similarity_4(x, y, z, timesteps):
    sim = 0
    tot = 0
    count = 0
    while(tot < 1000 and count < 7000):
        count += 1
        x1 = int(np.random.randint(low = 0, high = len(x)))
        x2 = int(np.random.randint(low = 0, high = len(x)))
        time = abs(timesteps[x1] - timesteps[x2])
        if(time < 10000):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[x1], y[x1], z[x1]],[x[x2], y[x2], z[x2]])
    if tot == 0:
        return 0
    return 1 - sim/tot