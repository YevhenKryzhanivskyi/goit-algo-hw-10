import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def f(x):
    """Функція для інтегрування."""
    return x ** 2


def monte_carlo_integration(func, a, b, n_points=1_000_000):
    """Обчислення інтеграла методом Монте-Карло."""
    x_rand = np.random.uniform(a, b, n_points)
    y_rand = func(x_rand)
    return (b - a) * np.mean(y_rand)


def analytic_integration(a, b):
    """Аналітичне обчислення інтеграла f(x) = x^2."""
    return (b ** 3) / 3 - (a ** 3) / 3


def main():
    # Межі інтегрування
    a, b = 0, 2

    # Обчислення інтеграла різними методами
    monte_carlo_result = monte_carlo_integration(f, a, b)
    analytic_result = analytic_integration(a, b)
    quad_result, _ = quad(f, a, b)

    # Вивід результатів
    print("Метод Монте-Карло:", monte_carlo_result)
    print("Аналітичний розрахунок:", analytic_result)
    print("Quad (SciPy):", quad_result)

    # Побудова графіка
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b, 100)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(
        f'Інтеграл f(x)=x^2 від {a} до {b}\n'
        f'Monte Carlo={monte_carlo_result:.4f}, Quad={quad_result:.4f}'
    )

    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()