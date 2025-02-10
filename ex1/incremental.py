import matplotlib.pyplot as plt
from point import generate_points
from utils import cross


def incremental_hull(points):
    # Βήμα 1: Ταξινόμηση σημείων ως προς x-συντεταγμένη
    points = sorted(points)
    
    # Βήμα 2: Υπολογισμός του άνω περιβλήματος
    upper_hull = []
    for point in points:
        while len(upper_hull) >= 2 and cross(upper_hull[-2], upper_hull[-1], point) <= 0:
            upper_hull.pop()
        upper_hull.append(point)
    
    # Βήμα 3: Υπολογισμός του κάτω περιβλήματος
    lower_hull = []
    for point in reversed(points):
        while len(lower_hull) >= 2 and cross(lower_hull[-2], lower_hull[-1], point) <= 0:
            lower_hull.pop()
        lower_hull.append(point)
    
    # Βήμα 4: Συνένωση του άνω και κάτω περιβλήματος
    return upper_hull[:-1] + lower_hull[:-1]


if __name__ == "__main__":
    points = generate_points(100)
    hull = incremental_hull(points)

    plt.scatter(*zip(*points), label="Points")
    plt.plot(*zip(*(hull + [hull[0]])), label="Incremental Hull", linestyle='dashed')
    plt.legend()
    plt.title("Incremental Algorithm")
    plt.show()
