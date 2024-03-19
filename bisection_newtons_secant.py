import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 3 + 15 * x ** 2 + 27 * x + 11


def f_prime(x):
    return 3 * x ** 2 + 30 * x + 27


def f_second_prime(x):
    return 6 * x + 30


def f_third_prime():
    return 6.0


def check_req(a, b):
    return f_prime(a) * f_prime(b) < 0


def check_newtons_req(a, b):
    return (f_second_prime(a) * f_second_prime(b) >= 0) and (f_third_prime() * f_third_prime() >= 0)


def x_sr_cal(a, b):
    return (a + b) * 0.5


def plot_function_and_iterations(method, a, b, epsilon, is_maximum=True):
    x_values = np.linspace(a - 1, b + 1, 400)
    y_values = f(x_values)

    plt.plot(x_values, y_values, label='Function')

    iterations = method(a, b, epsilon)
    num_iterations = len(iterations)
    for i, x in enumerate(iterations):
        y = f(x)
        color_ratio = i / (num_iterations - 1)  # Normalize to [0, 1]
        color = (1 - color_ratio, color_ratio, 0) if is_maximum else (0, color_ratio, 1 - color_ratio)
        plt.scatter(x, y, color=color, label='Iteration' if i == 0 else None)

    if num_iterations > 0:
        final_x, final_y = iterations[-1], f(iterations[-1])
        plt.text(final_x, final_y, str(num_iterations), fontsize=12, ha='right', va='bottom')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    title = 'Maximum' if is_maximum else 'Minimum'
    plt.title(title + ' iterations using ' + method.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()




def bisection_method(a, b, epsilon):
    if check_req(a, b):
        x_values = []
        while True:
            x_sr = x_sr_cal(a, b)
            x_values.append(x_sr)
            if f_prime(x_sr) == 0:
                return x_values
            if f_prime(x_sr) * f_prime(a) < 0:
                b = x_sr
            else:
                a = x_sr
            if abs(f_prime(x_sr)) < epsilon:
                return x_values
    else:
        print("Requirement not met")


def newtons_method(a, b, epsilon):
    if check_req(a, b):
        x_values = []
        x_n_1 = 0
        if f_third_prime() == f_prime(a):
            x_n = a
        else:
            x_n = b

        while not (abs(f_prime(x_n_1)) < epsilon or abs(x_n_1 - x_n) < epsilon):
            x_values.append(x_n)
            x_n_1 = x_n
            x_n = x_n - (f_prime(x_n) / f_second_prime(x_n))

        return x_values
    else:
        print("Necessary condition or convergence criterion not met")


def secant_method(a, b, epsilon):
    if check_req(a, b):
        x_values = []
        x_n_1 = 0
        formula = True
        if f_third_prime() == f_prime(a):
            x_n = b
        else:
            x_n = a
            formula = False

        while not (abs(f_prime(x_n_1)) < epsilon or abs(x_n_1 - x_n) < epsilon):
            x_values.append(x_n)
            x_n_1 = x_n
            if formula:
                x_n = x_n - (f_prime(x_n) / (f_prime(x_n) - f_prime(a))) * (x_n - a)
            else:
                x_n = x_n - (f_prime(x_n) / (f_prime(b) - f_prime(x_n))) * (b - x_n)

        return x_values
    else:
        print("Necessary condition or convergence criterion not met")


a = -8.0
b = 5.0
epsilon = 0.05

plot_function_and_iterations(bisection_method, a, b, epsilon)
plot_function_and_iterations(newtons_method, a, b, epsilon)
plot_function_and_iterations(secant_method, a, b, epsilon)
