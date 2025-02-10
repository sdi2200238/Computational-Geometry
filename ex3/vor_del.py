import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, Delaunay, voronoi_plot_2d # type: ignore
import random

def generate_points(n):
    # Set the random seed so the points are always the same for comparison
    random.seed(12)    
    # Create a list to store the points
    points = []
    
    # Generate n random points
    for _ in range(n):
        x = random.uniform(0, 1000)  # Random x-coordinate
        y = random.uniform(0, 1000)  # Random y-coordinate
        points.append((x, y))  # Add the point as a tuple to the list
    
    return points
def plot_voronoi_delaunay(points):
    # Compute Delaunay Triangulation
    delaunay_tri = Delaunay(points)
    
    # Compute Voronoi Diagram
    vor = Voronoi(points)
    
    # Plot both diagrams on the same figure
    plt.figure(figsize=(8, 8))
    
    # Convert points to a NumPy array
    points = np.array(points)
    
    # Plot Delaunay Triangulation
    plt.triplot(points[:, 0], points[:, 1], delaunay_tri.simplices, 'g-', alpha=0.6)
    
    # Plot Voronoi Diagram
    voronoi_plot_2d(vor, show_vertices=False, line_colors='b', line_width=1.5, point_size=5, ax=plt.gca())
    
    # Plot original points
    plt.plot(points[:, 0], points[:, 1], 'ro')
    plt.title("Delaunay Triangulation & Voronoi Diagram")
    plt.show()

# Example usage
n_points = 20
points = generate_points(n_points)
plot_voronoi_delaunay(points)
