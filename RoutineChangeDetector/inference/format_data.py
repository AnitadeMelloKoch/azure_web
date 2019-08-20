import numpy as np

def estimate_standardization_params(X):
    mean = np.nanmean(X, axis=0)
    std_dev = np.nanstd(X, axis =0)
    
    return (mean, std_dev)

def standardize_features(_X):
    X = np.asarray(_X)
    (mean, std_dev) = estimate_standardization_params(X)
    # subtracting mean to centralize all features
    X_central = np.zeros((X.shape))
    for i in range(len(mean)):
        X_central[:,i] = np.subtract(X[:,i], mean[i])
    # Divide by standard deviation to get unit-variance for all features
    normalizer = np.where(std_dev > 0., std_dev, 1.).reshape((1,-1))
    X_standard = X_central / normalizer
    # X_standard = np.zeros((X.shape))
    # for i in range(len(X)):
    #     X_central[:,i] = np.divide(X[:,i], normalizer[i])
    nan_data = np.isnan(X_standard)
    X_standard[nan_data] = 0

    return X_standard