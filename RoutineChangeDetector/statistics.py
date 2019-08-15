import scipy as scipy
import numpy as np

def mean_dir(x, y, z):
    x_mean = np.nanmean(x)
    y_mean = np.nanmean(y)
    z_mean = np.nanmean(z)

    return (x_mean, y_mean, z_mean)

def std_dev_dir(x, y, z):
    x_std = np.nanstd(x)
    y_std = np.nanstd(y)
    z_std = np.nanstd(z)

    return (x_std, y_std, z_std)

def mean_mag(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    mean_mag = np.mean(mag)

    return mean_mag

def std_mag(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    std_mag = np.std(mag)

    return std_mag

def moment3(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    return scipy.stats.moment(mag, 3)

def moment4(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    return scipy.stats.moment(mag, 4)

def percentile25(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    return np.percentile(mag, 25)

def percentile50(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    return np.percentile(mag, 50)

def percentile75(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    return np.percentile(mag, 75)

def valueEntropy(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    rng = np.amax(mag) - np.amin(mag)
    binWidth = rng/20
    H = 0
    for x in range(len(mag)):
        H = H - mag[x]*np.log(mag[x]/binWidth)

    return H

def timeEntropy(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    total = np.sum(mag)
    S = 0
    for x in range(len(mag)):
        S = S - (mag[x]/total)*np.log(mag[x]/total)

    return S

def spectral_entropy(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag)
    total = np.sum(PSD)
    S = 0
    for x in range(len(PSD)):
        S = S - (PSD[x]/total)*np.log(PSD[x]/total)

def energyband0(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 0 and f[x] <= 0.5):
            energy = energy + PSD[x]
    return np.log(energy)

def energyband1(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 0.5 and f[x] <= 1):
            energy = energy + PSD[x]
    return np.log(energy)

def energyband2(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 1 and f[x] <= 3):
            energy = energy + PSD[x]
    return np.log(energy)

def energyband3(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 3 and f[x] <= 5):
            energy = energy + PSD[x]
    return np.log(energy)

def energyband4(x, y, z):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    f, PSD = scipy.signal.periodogram(mag)
    energy = 0
    for x in range(len(PSD)):
        if(f[x] > 5):
            energy = energy + PSD[x]
    return np.log(energy)

def autocorr(x, y, z, timesteps):
    mag = np.sqrt(np.add(np.add(np.aquare(x), np.square(y)), np.square(z)))
    mean = np.mean(mag)
    for x in range(len(mag)):
        mag[x] = mag[x] - mean

    corr = np.correlate(mag, mag, mode='full')
    autocorr = corr[corr.size // 2:]
    lag0 = autocorr[0]
    for x in range(len(autocorr)):
        autocorr[x] = autocorr[0]/lag0

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

    return (maxVal*timesteps),(autocorr[maxVal])

def correlation_coeff(x, y, z):
    corr_coeff = np.corrcoef([x,y,z])
    return corr_coeff[1,0], corr_coeff[2, 0], corr_coeff[1,2]

def cos_similarity_0(x, y, z, timesteps):
    sim = 0
    tot = 0
    for index in range(len(x)):
        if(index*timesteps > 0 and index*timesteps < 0.5):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[index], y[index], z[index]],[x[index + 1], y[index + 1], z[index + 1]])

    return sim/tot

def cos_similarity_1(x, y, z, timesteps):
    sim = 0
    tot = 0
    for index in range(len(x)):
        if(index*timesteps > 0.5 and index*timesteps < 1):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[index], y[index], z[index]],[x[index + 1], y[index + 1], z[index + 1]])

    return sim/tot

def cos_similarity_2(x, y, z, timesteps):
    sim = 0
    tot = 0
    for index in range(len(x)):
        if(index*timesteps > 1 and index*timesteps < 5):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[index], y[index], z[index]],[x[index + 1], y[index + 1], z[index + 1]])

    return sim/tot

def cos_similarity_3(x, y, z, timesteps):
    sim = 0
    tot = 0
    for index in range(len(x)):
        if(index*timesteps > 5 and index*timesteps < 10):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[index], y[index], z[index]],[x[index + 1], y[index + 1], z[index + 1]])

    return sim/tot

def cos_similarity_4(x, y, z, timesteps):
    sim = 0
    tot = 0
    for index in range(len(x)):
        if(index*timesteps > 10):
            tot = tot + 1
            sim = sim + scipy.spatial.distance.cosine([x[index], y[index], z[index]],[x[index + 1], y[index + 1], z[index + 1]])

    return sim/tot