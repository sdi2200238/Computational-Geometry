import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.animation as animation

def generate_random_points(n=80, lower=-10, upper=10):
    """Generate n random points in 3D space within a given range."""
    return np.random.uniform(lower, upper, (n, 3))

def compute_convex_hull(points):
    """Compute the convex hull of a given set of 3D points using Quickhull."""
    hull = ConvexHull(points)
    return hull

def plot_convex_hull_animated(points, hull):
    """Plot the convex hull in 3D with rotation."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(points[:, 0], points[:, 1], points[:, 2], marker='o')

    # Draw the triangular faces
    for simplex in hull.simplices:
        tri = [points[simplex[i]] for i in range(3)]
        ax.add_collection3d(Poly3DCollection([tri], alpha=0.5, edgecolor='k'))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Convex Hull of 80 Random Points in 3D (Rotating)')

    def update(frame):
        ax.view_init(elev=20, azim=frame)

    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
    plt.show()

# Generate random points in 3D
points = generate_random_points()

# Compute the convex hull
hull = compute_convex_hull(points)

# Plot the convex hull with rotation
plot_convex_hull_animated(points, hull)
