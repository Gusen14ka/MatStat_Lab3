import numpy as np

def calculate(sample, n):
    q1, q3 = np.quantile(sample, [0.25, 0.75])
    iqr = q3 - q1
    upper_outlier_lim = q3 + 1.5 * iqr
    lower_outlier_lim = q1 - 1.5 * iqr

    n_outliers = 0
    n_outliers += sample[sample > upper_outlier_lim].size
    n_outliers += sample[sample < lower_outlier_lim].size

    return n_outliers / n