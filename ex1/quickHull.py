import matplotlib.pyplot as plt
from point import generate_points
from utils import cross, distance_to_line

def quickhull(points):
    # Βήμα 1: Εύρεση δύο ακροτάτων σημείων
    leftmost = min(points)
    rightmost = max(points)

    # Βήμα 2: Διάσπαση σε άνω και κάτω ημιεπίπεδο
    upper_points = [p for p in points if cross(leftmost, rightmost, p) > 0]
    lower_points = [p for p in points if cross(rightmost, leftmost, p) > 0]

    # Βήμα 3: Αναδρομική υπολογισμός για κάθε ημιεπίπεδο
    upper_hull = find_hull(upper_points, leftmost, rightmost)
    lower_hull = find_hull(lower_points, rightmost, leftmost)

    # Βήμα 4: Συνένωση των ημιεπιπέδων
    return [leftmost] + upper_hull + [rightmost] + lower_hull


def find_hull(points, p1, p2):
    if not points:
        return []

    # Βήμα 3.1: Εύρεση του πιο απομακρυσμένου σημείου
    farthest = max(points, key=lambda p: distance_to_line(p1, p2, p))
    points.remove(farthest)

    # Βήμα 3.2: Διαίρεση σε νέα ημιεπίπεδα
    left_points = [p for p in points if cross(p1, farthest, p) > 0]
    right_points = [p for p in points if cross(farthest, p2, p) > 0]

    # Βήμα 3.3: Αναδρομικός υπολογισμός για κάθε υποσύνολο
    return find_hull(left_points, p1, farthest) + [farthest] + find_hull(right_points, farthest, p2)

if __name__ == "__main__":
    points = generate_points(100)
    hull = quickhull(points)

    plt.scatter(*zip(*points), label="Points")
    plt.plot(*zip(*(hull + [hull[0]])), linestyle='solid', color='red')
    plt.legend()
    plt.title("QuickHull Algorithm")
    plt.show()
