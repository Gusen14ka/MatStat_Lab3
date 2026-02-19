import matplotlib.pyplot as plt
import numpy as np

def plot(sample, name, n, frac):
    plt.figure()

    plt.boxplot(sample, label=name)
    plt.title(f"Распределение {name}, n={n}, Доля выбросов {frac:.2%}")
    plt.ylabel("Значение")

    if name == "Cauchy":
        q1, q3 = np.quantile(sample, [0.25, 0.75])
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        plt.figure()
        plt.boxplot(sample, label=name)
        plt.title(f"Распределение {name} (центральная часть), n={n}\n Доля выбросов {frac:.2%}")
        plt.ylabel("Значение")
        plt.ylim(lower - abs(lower * 0.1), upper + upper * 0.1)

    
