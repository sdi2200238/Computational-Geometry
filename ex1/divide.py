from itertools import chain
import matplotlib.pyplot as plt
from point import generate_points
from utils import cross

# Αλγόριθμος Διαίρει και Βασίλευε για το Κυρτό Περίβλημα

def divide_and_conquer(points):
    """
    Υλοποιεί τον αλγόριθμο Διαίρει και Βασίλευε για το κυρτό περίβλημα.
    """
    # Βήμα 1: Ταξινόμηση των σημείων κατά x-συντεταγμένη
    points = sorted(points)

    # Βάση αναδρομής: Επιστροφή αν υπάρχουν 1 ή 2 σημεία
    if len(points) <= 2:
        return points

    # Βήμα 2: Διαίρεση των σημείων σε δύο υποσύνολα
    mid_index = len(points) // 2
    left_points = points[:mid_index]
    right_points = points[mid_index:]

    # Βήμα 3: Υπολογισμός κυρτών περιβλημάτων για κάθε υποσύνολο
    left_hull = divide_and_conquer(left_points)
    right_hull = divide_and_conquer(right_points)

    # Βήμα 4: Συνένωση των κυρτών περιβλημάτων
    return merge_hulls(left_hull, right_hull)


def merge_hulls(left, right):
    """
    Ενώνει δύο κυρτά περιβλήματα σε ένα ενιαίο κυρτό περίβλημα.
    """
    # Βήμα 1: Συνένωση και ταξινόμηση σημείων
    merged_points = sorted(chain(left, right), key=lambda p: (p[0], p[1]))

    # Βήμα 2: Υπολογισμός του κάτω και του άνω περιβλήματος
    lower_hull, upper_hull = [], []

    # Κάτω περίβλημα
    for point in merged_points:
        while len(lower_hull) >= 2 and cross(lower_hull[-2], lower_hull[-1], point) <= 0:
            lower_hull.pop()
        lower_hull.append(point)

    # Άνω περίβλημα
    for point in reversed(merged_points):
        while len(upper_hull) >= 2 and cross(upper_hull[-2], upper_hull[-1], point) <= 0:
            upper_hull.pop()
        upper_hull.append(point)

    # Βήμα 3: Συνένωση του άνω και κάτω περιβλήματος χωρίς διπλότυπα
    return lower_hull[:-1] + upper_hull[:-1]


if __name__ == "__main__":
    # Δημιουργία τυχαίων σημείων
    points = generate_points(200)

    # Υπολογισμός κυρτού περιβλήματος
    convex_hull = divide_and_conquer(points)

    # Οπτικοποίηση αποτελέσματος
    plt.scatter(*zip(*points), label="Σημεία")
    plt.plot(*zip(*(convex_hull + [convex_hull[0]])), label="Κυρτό Περίβλημα", color="red")
    plt.legend()
    plt.title("Αλγόριθμος Διαίρει και Βασίλευε - Κυρτό Περίβλημα")
    plt.show()
