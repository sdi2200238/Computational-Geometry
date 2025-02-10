import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, Delaunay
import time

def generate_points(n, seed=12):
    np.random.seed(seed)
    return np.random.uniform(0, 1000, (n, 2))

def measure_time(n_values):
    delaunay_times = []
    voronoi_times = []
    
    for n in n_values:
        points = generate_points(n)
        
        # Measure time for Delaunay Triangulation
        start_time = time.time()
        Delaunay(points)
        delaunay_times.append(time.time() - start_time)
        
        # Measure time for Voronoi Diagram
        start_time = time.time()
        Voronoi(points)
        voronoi_times.append(time.time() - start_time)
    
    return delaunay_times, voronoi_times

# Define different numbers of points to test
n_values = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
delaunay_times, voronoi_times = measure_time(n_values)

# Plot complexity growth
plt.figure(figsize=(10, 5))
plt.plot(n_values, delaunay_times, label="Delaunay Triangulation", marker='o')
plt.plot(n_values, voronoi_times, label="Voronoi Diagram", marker='s')
plt.xlabel("Number of Points")
plt.ylabel("Execution Time (seconds)")
plt.title("Computational Complexity of Delaunay & Voronoi")
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.show()
