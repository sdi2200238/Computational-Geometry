import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, Delaunay
import time

def generate_points(n, seed=12):
    """
    Δημιουργία τυχαίων σημείων.
    
    Είσοδος: Αριθμός σημείων, σπόρος για την τυχαιότητα.
    Έξοδος: Πίνακας με τυχαία σημεία.
    """
    np.random.seed(seed)
    return np.random.uniform(0, 1000, (n, 2))

def measure_performance(sizes):
    """
    Μέτρηση της απόδοσης των αλγορίθμων Delaunay και Voronoi για διάφορα μεγέθη εισόδου.
    
    Είσοδος: Λίστα μεγεθών εισόδου για τη μέτρηση.
    Έξοδος: Δύο λίστες με τους χρόνους εκτέλεσης για κάθε αλγόριθμο.
    """
    delaunay_times = []
    voronoi_times = []
    
    for size in sizes:
        points = generate_points(size)  # Δημιουργία τυχαίων σημείων
        
        # Μέτρηση απόδοσης του αλγορίθμου Delaunay Triangulation
        start_time = time.time()
        Delaunay(points)
        delaunay_times.append(time.time() - start_time)
        
        # Μέτρηση απόδοσης του αλγορίθμου Voronoi Diagram
        start_time = time.time()
        Voronoi(points)
        voronoi_times.append(time.time() - start_time)
    
    return delaunay_times, voronoi_times

if __name__ == "__main__":
    # Ορισμός μεγεθών συνόλων σημείων για τη μέτρηση
    sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
    
    # Εκτέλεση της μέτρησης
    delaunay_times, voronoi_times = measure_performance(sizes)
    
    # Απεικόνιση της πολυπλοκότητας
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, delaunay_times, label="Delaunay Triangulation", marker='o')
    plt.plot(sizes, voronoi_times, label="Voronoi Diagram", marker='s')
    
    # Προσθήκη ετικετών και τίτλου
    plt.xlabel("Number of Points", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.title("Computational Complexity of Delaunay & Voronoi", fontsize=14)
    plt.legend()
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True)
    plt.show()
