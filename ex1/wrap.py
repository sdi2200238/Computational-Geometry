import matplotlib.pyplot as plt
from point import generate_points
from utils import cross
import numpy as np

def gift_wrapping(points):
    # Βήμα 1: Εύρεση του αριστερότερου σημείου
    start = min(points)
    hull = [start]
    current_point = start

    while True:
        # Βήμα 2: Εύρεση του επόμενου σημείου με την μικρότερη γωνία
        next_point = points[0]
        for point in points:
            if next_point == current_point or cross(current_point, next_point, point) < 0:
                next_point = point

        # Βήμα 3: Προσθήκη του σημείου στο περίβλημα
        current_point = next_point
        if current_point == start:
            break
        hull.append(current_point)
    
    return hull


if __name__ == "__main__":
    points = generate_points(100)
    hull = gift_wrapping(points)

    plt.scatter(*zip(*points), label="Points")
    plt.plot(*zip(*(hull + [hull[0]])), label="Gift Wrapping Hull", linestyle='solid')
    plt.legend()
    plt.title("Gift Wrapping Algorithm")
    plt.show()
