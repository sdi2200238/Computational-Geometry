import time
import matplotlib.pyplot as plt
import numpy as np
from incremental import incremental_hull
from divide import divide_and_conquer
from wrap import gift_wrapping
from quickHull import quickhull
from point import generate_points

# Benchmarking Function
def benchmark_algorithms(sizes):
    """
    Benchmarks the convex hull algorithms for various input sizes.
    :param sizes: List of input sizes to benchmark.
    :return: A list of dictionaries containing execution times for each algorithm.
    """
    results = []
    for size in sizes:
        points = generate_points(size)  # Generate random points

        # Benchmark Incremental Algorithm
        start_time = time.time()
        incremental_hull(points)
        incremental_time = time.time() - start_time

        # Benchmark Gift Wrapping Algorithm
        start_time = time.time()
        gift_wrapping(points)
        gift_wrapping_time = time.time() - start_time

        # Benchmark Divide and Conquer Algorithm
        start_time = time.time()
        divide_and_conquer(points)
        divide_and_conquer_time = time.time() - start_time

        # Benchmark QuickHull Algorithm
        start_time = time.time()
        quickhull(points)
        quickhull_time = time.time() - start_time

        # Store results for this input size
        results.append((size, incremental_time, gift_wrapping_time, divide_and_conquer_time, quickhull_time))

    return results

def fit_polynomial(x, y, degree=3):
    """
    Fits a polynomial of the given degree to the data.
    :param x: List of x-values (independent variable).
    :param y: List of y-values (dependent variable).
    :param degree: Degree of the polynomial to fit.
    :return: Fitted y-values.
    """
    coefficients = np.polyfit(x, y, degree)
    polynomial = np.poly1d(coefficients)
    return polynomial(x)

if __name__ == "__main__":
    # Define point set sizes for benchmarking
    

    sizes = np.linspace(10, 1000000, num=5).astype(int)

    # Run the benchmark
    results = benchmark_algorithms(sizes)

    # Extract results for plotting
    sizes = [result[0] for result in results]
    incremental_times = [result[1] for result in results]
    gift_wrapping_times = [result[2] for result in results]
    divide_and_conquer_times = [result[3] for result in results]
    quickhull_times = [result[4] for result in results]
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, incremental_times, label="Incremental", marker='o')
    plt.plot(sizes, gift_wrapping_times, label="Gift Wrapping", marker='o')
    plt.plot(sizes, divide_and_conquer_times, label="Divide & Conquer", marker='o')
    plt.plot(sizes, quickhull_times, label="QuickHull", marker='o')

    # Add labels and title
    plt.xlabel("Number of Points", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.title("Comparison of Convex Hull Algorithms", fontsize=14)
    plt.legend()
    plt.grid()
    plt.show()
