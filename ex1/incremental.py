import matplotlib.pyplot as plt
from point import generate_points
from utils import cross

def incremental_hull(points):
    """
    Υλοποίηση του αυξητικού αλγορίθμου για το κυρτό περίβλημα.
    
    Είσοδος: Λίστα σημείων ως (x, y) συντεταγμένες.
    Έξοδος: Τα σημεία του κυρτού περιβλήματος.
    """
    # Ταξινόμηση των σημείων με βάση την x-συντεταγμένη
    points = sorted(points)

    # Υπολογισμός του άνω κυρτού περιβλήματος
    upper_hull = []
    for point in points:
        while len(upper_hull) >= 2 and cross(upper_hull[-2], upper_hull[-1], point) <= 0:
            upper_hull.pop()
        upper_hull.append(point)

    # Υπολογισμός του κάτω κυρτού περιβλήματος
    lower_hull = []
    for point in reversed(points):
        while len(lower_hull) >= 2 and cross(lower_hull[-2], lower_hull[-1], point) <= 0:
            lower_hull.pop()
        lower_hull.append(point)

    # Συνένωση των δύο περιβλημάτων χωρίς διπλότυπα άκρα
    return upper_hull[:-1] + lower_hull[:-1]

if __name__ == "__main__":
    points = generate_points(100)
    hull = incremental_hull(points)

    # Οπτικοποίηση αποτελέσματος
    plt.scatter(*zip(*points), label="Σημεία")
    plt.plot(*zip(*(hull + [hull[0]])), label="Αυξητικό Κυρτό Περίβλημα", linestyle='dashed', color="red")
    plt.title("Αυξητικός Αλγόριθμος Κυρτού Περιβλήματος")
    plt.show()
