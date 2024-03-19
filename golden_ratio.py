import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 3 + 15 * x ** 2 + 27 * x + 11


def golden_ratio_method(f, a, b, epsilon, is_maximum=True):
    k = (math.sqrt(5) - 1) / 2
    x1 = b - k * (b - a)
    x2 = a + k * (b - a)

    iterations = [(x1, x2)]

    while abs(x2 - x1) > epsilon:
        if is_maximum:
            if f(x1) > f(x2):
                b = x2
                x2 = x1
                x1 = b - k * (b - a)
            else:
                a = x1
                x1 = x2
                x2 = a + k * (b - a)
        else:
            if f(x1) < f(x2):
                b = x2
                x2 = x1
                x1 = b - k * (b - a)
            else:
                a = x1
                x1 = x2
                x2 = a + k * (b - a)

        iterations.append((x1, x2))

    x_optimal = (a + b) / 2
    return x_optimal, iterations


a = -8.0
b = 5.0
epsilon = 0.001

maximum, iterations_max = golden_ratio_method(f, a, b, epsilon, is_maximum=True)
minimum, iterations_min = golden_ratio_method(f, a, b, epsilon, is_maximum=False)

# Plotting the function
x_values = np.linspace(a, b, 1000)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x)')
plt.scatter([maximum], [f(maximum)], color='red', label='Maximum')
plt.scatter([minimum], [f(minimum)], color='green', label='Minimum')

# Plotting iterations
for x1, x2 in iterations_max:
    plt.scatter([x1, x2], [f(x1), f(x2)], color='blue', alpha=0.3)

for x1, x2 in iterations_min:
    plt.scatter([x1, x2], [f(x1), f(x2)], color='orange', alpha=0.3)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function Plot with Maximum and Minimum (with Iterations)')
plt.legend()
plt.grid(True)
plt.show()

print("Maksimum funkcji znajduje się w punkcie:", maximum)
print("Minimum funkcji znajduje się w punkcie:", minimum)
