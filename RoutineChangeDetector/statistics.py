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
        H = H - (hist[x]/total)*np.log((hist[x]/total))

    return H

# working
def timeEntropy(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    total = np.sum(mag)
    S = 0
    for x in range(len(mag)):
        S = S - (mag[x]/total)*np.log(mag[x]/total)

    return S

# close enough
def spectral_entropy(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    _, PSD = scipy.signal.periodogram(mag, 40)
    total = np.sum(PSD)
    S = 0
    for x in range(len(PSD)):
        S = S - (PSD[x]/total)*np.log(PSD[x]/total)
    return S

# not working
def energyband0(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag, 40)
    #print(f)
    #print(PSD)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] >= 0 and f[x] <= 0.5):
            print(PSD[x])
            energy = energy + PSD[x]
    return np.log(energy)

# not working
def energyband1(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag, 40)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 0.5 and f[x] <= 1):
            energy = energy + PSD[x]
    return np.log(energy)

# not working
def energyband2(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag, 40)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 1 and f[x] <= 3):
            energy = energy + PSD[x]
    return np.log(energy)

# not working
def energyband3(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag, 40)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 3 and f[x] <= 5):
            energy = energy + PSD[x]
    return np.log(energy)

# not working
def energyband4(x, y, z):
    mag = np.sqrt(np.add(np.add(np.square(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag, 40)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 5):
            energy = energy + PSD[x]
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
    for x in range(len(autocorr)):
        autocorr[x] = autocorr[x]/lag0
    found = False
    index = 0
    previous = 1000
    maxVal = 0
    
    while (not found):
        if(previous > autocorr[index]):
            previous = autocorr[index]
            index += 1
        else:
            maxVal = np.argmax(autocorr[index:])
            found = True
    period = timesteps[index:][maxVal] - timesteps[0]
    return (period),(autocorr[index:][maxVal])

# working
def correlation_coeff(x, y, z):
    corr_coeff = np.corrcoef([x,y,z])
    return corr_coeff[1,0], corr_coeff[2, 0], corr_coeff[1,2]

# working
def cos_similarity_0(x, y, z, timesteps):
    sim = 0
    tot = 0
    while(tot < 1000):
        x1 = int(np.random.randint(low = 0, high = len(x)))
        x2 = int(np.random.randint(low = 0, high = len(x)))
        time = abs(timesteps[x1] - timesteps[x2])
        if(time >= 0 and time < 0.5):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[x1], y[x1], z[x1]],[x[x2], y[x2], z[x2]])
    print(tot)
    return 1 - sim/tot

def cos_similarity_1(x, y, z, timesteps):
    sim = 0
    tot = 0
    while(tot < 1000):
        x1 = int(np.random.randint(low = 0, high = len(x)))
        x2 = int(np.random.randint(low = 0, high = len(x)))
        time = abs(timesteps[x1] - timesteps[x2])
        if(time >= 0.5 and time < 1):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[x1], y[x1], z[x1]],[x[x2], y[x2], z[x2]])
    print(tot)
    return 1 - sim/tot

def cos_similarity_2(x, y, z, timesteps):
    sim = 0
    tot = 0
    while(tot < 1000):
        x1 = int(np.random.randint(low = 0, high = len(x)))
        x2 = int(np.random.randint(low = 0, high = len(x)))
        time = abs(timesteps[x1] - timesteps[x2])
        if(time >= 1 and time < 5):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[x1], y[x1], z[x1]],[x[x2], y[x2], z[x2]])
    print(tot)
    return 1 - sim/tot

def cos_similarity_3(x, y, z, timesteps):
    sim = 0
    tot = 0
    while(tot < 1000):
        x1 = int(np.random.randint(low = 0, high = len(x)))
        x2 = int(np.random.randint(low = 0, high = len(x)))
        time = abs(timesteps[x1] - timesteps[x2])
        if(time >= 5 and time < 10):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[x1], y[x1], z[x1]],[x[x2], y[x2], z[x2]])
    print(tot)
    return 1 - sim/tot

def cos_similarity_4(x, y, z, timesteps):
    sim = 0
    tot = 0
    while(tot < 1000):
        x1 = int(np.random.randint(low = 0, high = len(x)))
        x2 = int(np.random.randint(low = 0, high = len(x)))
        time = abs(timesteps[x1] - timesteps[x2])
        if(time < 10):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[x1], y[x1], z[x1]],[x[x2], y[x2], z[x2]])
    print(tot)
    return 1 - sim/tot



data = np.loadtxt("/mnt/c/Users/Anita/Documents/4thyear/labproject/00EABED2-271D-49D8-B599-1D4A09240601/1444079161.m_raw_magnet.dat")
timestamps = data[:, 0]
x = data[:, 1]
y = data[:, 2]
z = data[:, 3]

print(autocorr(x, y, z, timestamps))
