import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, Delaunay, voronoi_plot_2d  # type: ignore
import random

def generate_random_points(n):
    """
    Δημιουργία n τυχαίων σημείων σε ένα δισδιάστατο χώρο.
    
    Είσοδος: Αριθμός σημείων προς δημιουργία.
    Έξοδος: Λίστα με τα σημεία ως tuples (x, y).
    """
    random.seed(12)  # Ορισμός seed για αναπαραγωγιμότητα
    points = [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(n)]
    return points

def plot_voronoi_delaunay(points):
    """
    Απεικόνιση του διαγράμματος Voronoi και της τριγωνοποίησης Delaunay για ένα σύνολο σημείων.
    
    Είσοδος: Λίστα σημείων ως tuples (x, y).
    Έξοδος: Καμία (η συνάρτηση εμφανίζει το διάγραμμα).
    """
    # Υπολογισμός της τριγωνοποίησης Delaunay
    delaunay_tri = Delaunay(points)
    
    # Υπολογισμός του διαγράμματος Voronoi
    vor = Voronoi(points)
    
    # Απεικόνιση και των δύο διαγραμμάτων στην ίδια εικόνα
    plt.figure(figsize=(8, 8))
    
    # Μετατροπή των σημείων σε πίνακα NumPy
    points = np.array(points)
    
    # Απεικόνιση της τριγωνοποίησης Delaunay
    plt.triplot(points[:, 0], points[:, 1], delaunay_tri.simplices, 'g-', alpha=0.6, label='Τριγωνοποίηση Delaunay')
    
    # Απεικόνιση του διαγράμματος Voronoi
    voronoi_plot_2d(vor, show_vertices=False, line_colors='b', line_width=1.5, point_size=5, ax=plt.gca())
    
    # Προσθήκη του διαγράμματος Voronoi στο legend
    plt.plot([], [], 'b-', label='Διάγραμμα Voronoi')
    
    # Απεικόνιση των αρχικών σημείων
    plt.plot(points[:, 0], points[:, 1], 'ro', label='Αρχικά Σημεία')
    
    # Προσθήκη τίτλου και ετικετών αξόνων
    plt.title("Τριγωνοποίηση Delaunay & Διάγραμμα Voronoi")
    plt.xlabel("Άξονας X")
    plt.ylabel("Άξονας Y")
    
    # Προσθήκη υπομνήματος
    plt.legend()
    
    # Εμφάνιση του διαγράμματος
    plt.show()

if __name__ == "__main__":
    # Παράδειγμα χρήσης
    num_points = 20
    points = generate_random_points(num_points)
    plot_voronoi_delaunay(points)
    
    
    
