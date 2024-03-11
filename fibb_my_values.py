import numpy as np
import matplotlib.pyplot as plt

# Function definition for the cubic function
def f(x):
    return x**3 + 15*x**2 + 27*x + 11

# Fibonacci sequence calculation
def fibonacci(n):
    n -= 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_prev, fib_curr = 0, 1
        for _ in range(2, n + 1):
            fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
        return fib_curr

def golden_section_max_min(f, a, b, epsilon, is_max=True):
    n = 2

    while (b - a) / fibonacci(n) >= 2 * epsilon:
        n += 1

    n -= 1

    x1 = b - (fibonacci(n - 1) / fibonacci(n)) * (b - a)
    x2 = a + (fibonacci(n - 1) / fibonacci(n)) * (b - a)

    iteration = 1
    iterations_data = [(x1, x2)]
    while abs(x2 - x1) >= epsilon and n > 1:
        if is_max:
            if f(x1) > f(x2):
                b = x2
                x2 = x1
                n -= 1
                x1 = b - (fibonacci(n - 1) / fibonacci(n)) * (b - a)
            else:
                a = x1
                x1 = x2
                n -= 1
                x2 = a + (fibonacci(n - 1) / fibonacci(n)) * (b - a)
        else:
            if f(x1) < f(x2):
                b = x2
                x2 = x1
                n -= 1
                x1 = b - (fibonacci(n - 1) / fibonacci(n)) * (b - a)
            else:
                a = x1
                x1 = x2
                n -= 1
                x2 = a + (fibonacci(n - 1) / fibonacci(n)) * (b - a)

        iterations_data.append((x1, x2))
        print("Iteration:", iteration, "x1:", x1, "x2:", x2, "f(x1):", f(x1), "f(x2):", f(x2))
        iteration += 1

        # Plot at each iteration with annotations
        plt.figure(figsize=(10, 6))
        x = np.linspace(-8, 5, 1000) # WAZNE TUTAJ USTAWIC A I B
        y = f(x)
        plt.plot(x, y, label='Function')
        plt.scatter([x1, x2], [f(x1), f(x2)], color='blue', label='Current Iteration')
        plt.annotate(f"Iter {iteration-1}\n({x1:.2f}, {f(x1):.2f})", (x1, f(x1)), textcoords="offset points", xytext=(-10,10), ha='center')
        plt.annotate(f"Iter {iteration-1}\n({x2:.2f}, {f(x2):.2f})", (x2, f(x2)), textcoords="offset points", xytext=(-10,10), ha='center')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Golden Section Search - Iteration {iteration-1}')
        plt.legend()
        plt.grid(True)
        plt.show()

    x_opt = (a + b) / 2
    return x_opt, iterations_data

# Define the given variables for the cubic function
a_cubic = -8
b_cubic = 5
epsilon_cubic = 0.01

# Find the maximum
max_value_cubic, max_iterations_cubic = golden_section_max_min(f, a_cubic, b_cubic, epsilon_cubic, is_max=True)
print("Maximum:", max_value_cubic, "Function value:", f(max_value_cubic))

# Find the minimum
min_value_cubic, min_iterations_cubic = golden_section_max_min(f, a_cubic, b_cubic, epsilon_cubic, is_max=False)
print("Minimum:", min_value_cubic, "Function value:", f(min_value_cubic))
