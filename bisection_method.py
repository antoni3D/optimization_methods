import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return (100 - x) ** 2

# Function to find the minimum
def min_func(a, b, eps):
    xsr = (a + b) / 2
    l = b - a
    fxsr = f(xsr)

    iterations = 0
    intermediate_results = [(xsr, fxsr)]

    # Plot the initial function
    plt.figure()
    x_values = np.linspace(a, b, 400)
    y_values = f(x_values)
    plt.plot(x_values, y_values, label='Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Initial Function Plot for Minimum')
    plt.grid(True)
    plt.show()

    # Iterate until the desired precision is achieved
    while (b - a) > eps:
        x1 = a + l / 4
        x2 = b - l / 4

        fx1 = f(x1)
        fx2 = f(x2)

        if fx1 < fxsr:
            b = xsr
            xsr = x1
        else:
            if fx2 < fxsr:
                a = xsr
                xsr = x2
            else:
                a = x1
                b = x2

        l = b - a
        fxsr = f(xsr)

        iterations += 1
        intermediate_results.append((xsr, fxsr))

        # Plot at each iteration with annotations
        plt.figure()
        plt.plot(x_values, y_values, label='Function')
        plt.scatter([xsr], [fxsr], color='red', marker='x', label='Current Iteration')
        plt.annotate(f"Iter {iterations}\n(x={xsr:.2f}, y={fxsr:.2f})", (xsr, fxsr), textcoords="offset points", xytext=(-10,10), ha='center')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Iteration {iterations} for Minimum')
        plt.legend()
        plt.grid(True)
        plt.show()

    # Plot final result with annotation
    plt.figure()
    plt.plot(x_values, y_values, label='Function')
    plt.scatter([xsr], [fxsr], color='red', marker='o', label='Minimum')
    plt.annotate(f"Minimum at x={xsr:.2f}, y={fxsr:.2f}\nIterations: {iterations}", (xsr, fxsr), textcoords="offset points", xytext=(-10,10), ha='center')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Final Result for Minimum')
    plt.legend()
    plt.grid(True)
    plt.show()

    return xsr, iterations, intermediate_results


# Function to find the maximum
def max_func(a, b, eps):
    xsr = (a + b) / 2
    l = b - a
    fxsr = f(xsr)

    iterations = 0
    intermediate_results = [(xsr, fxsr)]

    # Plot the initial function
    plt.figure()
    x_values = np.linspace(a, b, 400)
    y_values = f(x_values)
    plt.plot(x_values, y_values, label='Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Initial Function Plot for Maximum')
    plt.grid(True)
    plt.show()

    # Iterate until the desired precision is achieved
    while (b - a) > eps:
        x1 = a + l / 4
        x2 = b - l / 4

        fx1 = f(x1)
        fx2 = f(x2)

        if fx1 > fxsr:
            b = xsr
            xsr = x1
        else:
            if fx2 > fxsr:
                a = xsr
                xsr = x2
            else:
                a = x1
                b = x2

        l = b - a
        fxsr = f(xsr)

        iterations += 1
        intermediate_results.append((xsr, fxsr))

        # Plot at each iteration with annotations
        plt.figure()
        plt.plot(x_values, y_values, label='Function')
        plt.scatter([xsr], [fxsr], color='red', marker='x', label='Current Iteration')
        plt.annotate(f"Iter {iterations}\n(x={xsr:.2f}, y={fxsr:.2f})", (xsr, fxsr), textcoords="offset points", xytext=(-10,10), ha='center')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Iteration {iterations} for Maximum')
        plt.legend()
        plt.grid(True)
        plt.show()

    # Plot final result with annotation
    plt.figure()
    plt.plot(x_values, y_values, label='Function')
    plt.scatter([xsr], [fxsr], color='green', marker='o', label='Maximum')
    plt.annotate(f"Maximum at x={xsr:.2f}, y={fxsr:.2f}\nIterations: {iterations}", (xsr, fxsr), textcoords="offset points", xytext=(-10,10), ha='center')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Final Result for Maximum')
    plt.legend()
    plt.grid(True)
    plt.show()

    return xsr, iterations, intermediate_results

# Define the range and precision
a = 60
b = 150
eps = 12

# Find the minimum and maximum
min_x, min_iterations, min_intermediate_results = min_func(a, b, eps)
max_x, max_iterations, max_intermediate_results = max_func(a, b, eps)

# Display the results
print("Minimum of the function at x={} with y={}, with precision epsilon={}, found in {} iterations".format(min_x,
                                                                                                            round(
                                                                                                                f(min_x),
                                                                                                                6), eps,
                                                                                                            min_iterations))
print("Maximum of the function at x={} with y={}, with precision epsilon={}, found in {} iterations".format(max_x,
                                                                                                            round(
                                                                                                                f(max_x),
                                                                                                                6), eps,
                                                                                                            max_iterations))
