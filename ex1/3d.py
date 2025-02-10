import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.animation as animation

def generate_random_points(n=80, lower=-10, upper=10):
    """
    Δημιουργία n τυχαίων σημείων στον 3D χώρο εντός ενός δεδομένου εύρους.
    
    Είσοδος: Αριθμός σημείων, κατώτερο και ανώτερο όριο.
    Έξοδος: Πίνακας με τυχαία σημεία.
    """
    return np.random.uniform(lower, upper, (n, 3))

def compute_convex_hull(points):
    """
    Υπολογισμός του κυρτού περιβλήματος για ένα σύνολο 3D σημείων χρησιμοποιώντας τον αλγόριθμο Quickhull.
    
    Είσοδος: Πίνακας με σημεία.
    Έξοδος: Το κυρτό περίβλημα.
    """
    hull = ConvexHull(points)
    return hull

def plot_convex_hull_animated(points, hull):
    """
    Οπτικοποίηση του κυρτού περιβλήματος σε 3D με περιστροφή.
    
    Είσοδος: Πίνακας με σημεία και το κυρτό περίβλημα.
    Έξοδος: Οπτικοποίηση με περιστροφή.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(points[:, 0], points[:, 1], points[:, 2], marker='o')

    # Σχεδίαση των τριγωνικών επιφανειών
    for simplex in hull.simplices:
        tri = [points[simplex[i]] for i in range(3)]
        ax.add_collection3d(Poly3DCollection([tri], alpha=0.5, edgecolor='k'))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Κυρτό Περίβλημα 80 Τυχαίων Σημείων σε 3D')

    def update(frame):
        ax.view_init(elev=20, azim=frame)

    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
    plt.show()

if __name__ == "__main__":
    # Δημιουργία τυχαίων σημείων στον 3D χώρο
    points = generate_random_points()

    # Υπολογισμός του κυρτού περιβλήματος
    hull = compute_convex_hull(points)

    # Οπτικοποίηση του κυρτού περιβλήματος με περιστροφή
    plot_convex_hull_animated(points, hull)
