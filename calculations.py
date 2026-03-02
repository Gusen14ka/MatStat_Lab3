import numpy as np
import scipy.stats as st

def calculate(sample, n):
    q1, q3 = np.quantile(sample, [0.25, 0.75])
    iqr = q3 - q1
    upper_outlier_lim = q3 + 1.5 * iqr
    lower_outlier_lim = q1 - 1.5 * iqr

    n_outliers = 0
    n_outliers += sample[sample > upper_outlier_lim].size
    n_outliers += sample[sample < lower_outlier_lim].size

    return n_outliers / n

def calculate_teor(name):
    sample = {
        "Normal": st.norm(),
        "Cauchy": st.cauchy(),
        "Laplace": st.laplace(0, 1 / np.sqrt(2)),
        "Poisson": st.poisson(5),
        "Uniform": st.uniform(-np.sqrt(3), 2 * np.sqrt(3))
    }

    dist = sample[name]
    Q1 = dist.ppf(0.25)
    Q3 = dist.ppf(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    if name == "Poisson":
        lower = np.floor(lower)
        upper = np.ceil(upper) - 1

    p = dist.cdf(lower) + (1 - dist.cdf(upper))
    return p
