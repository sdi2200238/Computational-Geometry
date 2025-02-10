import matplotlib.pyplot as plt
from point import generate_points
from utils import cross, distance_to_line

def quickhull(points):
    """
    Υλοποίηση του αλγορίθμου QuickHull για το κυρτό περίβλημα.
    
    Είσοδος: Λίστα σημείων ως (x, y) συντεταγμένες.
    Έξοδος: Τα σημεία του κυρτού περιβλήματος.
    """
    # Εύρεση δύο ακροτάτων σημείων
    leftmost = min(points)
    rightmost = max(points)

    # Διάσπαση σε άνω και κάτω ημιεπίπεδο
    upper_points = [p for p in points if cross(leftmost, rightmost, p) > 0]
    lower_points = [p for p in points if cross(rightmost, leftmost, p) > 0]

    # Αναδρομική υπολογισμός για κάθε ημιεπίπεδο
    upper_hull = find_hull(upper_points, leftmost, rightmost)
    lower_hull = find_hull(lower_points, rightmost, leftmost)

    # Συνένωση των ημιεπιπέδων
    return [leftmost] + upper_hull + [rightmost] + lower_hull

def find_hull(points, p1, p2):
    """
    Βοηθητική συνάρτηση για τον αναδρομικό υπολογισμό του QuickHull.
    
    Είσοδος: Λίστα σημείων, δύο σημεία p1 και p2.
    Έξοδος: Τα σημεία του κυρτού περιβλήματος για το συγκεκριμένο υποσύνολο.
    """
    if not points:
        return []

    # Εύρεση του πιο απομακρυσμένου σημείου
    farthest = max(points, key=lambda p: distance_to_line(p1, p2, p))
    points.remove(farthest)

    # Διαίρεση σε νέα ημιεπίπεδα
    left_points = [p for p in points if cross(p1, farthest, p) > 0]
    right_points = [p for p in points if cross(farthest, p2, p) > 0]

    # Αναδρομικός υπολογισμός για κάθε υποσύνολο
    return find_hull(left_points, p1, farthest) + [farthest] + find_hull(right_points, farthest, p2)

if __name__ == "__main__":
    points = generate_points(100)
    hull = quickhull(points)

    # Οπτικοποίηση αποτελέσματος
    plt.scatter(*zip(*points), label="Σημεία")
    plt.plot(*zip(*(hull + [hull[0]])), label="QuickHull Κυρτό Περίβλημα", linestyle='dashed', color='red')
    plt.title("Αλγόριθμος QuickHull για Κυρτό Περίβλημα")
    plt.show()
