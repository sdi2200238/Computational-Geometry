import matplotlib.pyplot as plt
from point import generate_points
from utils import cross
import numpy as np

def gift_wrapping(points):
    """
    Υλοποίηση του αλγορίθμου περιτυλίγματος δώρου για το κυρτό περίβλημα.
    
    Είσοδος: Λίστα σημείων ως (x, y) συντεταγμένες.
    Έξοδος: Τα σημεία του κυρτού περιβλήματος.
    """
    # Εύρεση του αριστερότερου σημείου
    start = min(points)
    hull = [start]
    current_point = start

    while True:
        # Εύρεση του επόμενου σημείου με την μικρότερη γωνία
        next_point = points[0]
        for point in points:
            if next_point == current_point or cross(current_point, next_point, point) < 0:
                next_point = point

        # Προσθήκη του σημείου στο περίβλημα
        current_point = next_point
        if current_point == start:
            break
        hull.append(current_point)
    
    return hull

if __name__ == "__main__":
    points = generate_points(100)
    hull = gift_wrapping(points)

    # Οπτικοποίηση αποτελέσματος
    plt.scatter(*zip(*points), label="Σημεία")
    plt.plot(*zip(*(hull + [hull[0]])), label="Περιτύλιγμα Κυρτό Περίβλημα", linestyle='dashed', color='red')
    plt.title("Αλγόριθμος Περιτυλίγματος")
    plt.show()
