from distributions import *
from calculations import calculate
from plotting import plot
import matplotlib.pyplot as plt

def main():
    sample_size = [20, 100]

    distribustions = {
        "Normal": generate_normal,
        "Cauchy": generate_cauchy,
        "Laplace": generate_laplace,
        "Poisson": generate_poisson,
        "Uniform": generate_uniform
    }

    n_exp = 1000

    for n in sample_size:
        for name, gen in distribustions.items():
            frac_outliers = np.zeros(n_exp)
            for i in range(n_exp):
                sample = gen(n)
                frac_outliers[i] = calculate(sample, n)
                if i == 0:
                    plot(sample, name, n, frac_outliers[i])
            
            E_frac = np.mean(frac_outliers)
            std_frac = np.std(frac_outliers)
            print(f"{name} n={n}:")
            print(f"frac={round(E_frac, 2)}, std={round(std_frac, 2)}")

    plt.show()


if __name__ == "__main__":
    main()