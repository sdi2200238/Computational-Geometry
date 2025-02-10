import time
import matplotlib.pyplot as plt
import numpy as np
from incremental import incremental_hull
from divide import divide_and_conquer
from wrap import gift_wrapping
from quickHull import quickhull
from point import generate_points

def benchmark_algorithms(sizes):
    """
    Υλοποίηση της συνάρτησης για τη μέτρηση της απόδοσης των αλγορίθμων κυρτού περιβλήματος για διάφορα μεγέθη εισόδου.
    
    Είσοδος: Λίστα μεγεθών εισόδου για τη μέτρηση.
    Έξοδος: Λίστα λεξικών που περιέχουν τους χρόνους εκτέλεσης για κάθε αλγόριθμο.
    """
    results = []
    for size in sizes:
        points = generate_points(size)  # Δημιουργία τυχαίων σημείων

        # Μέτρηση απόδοσης του αυξητικού αλγορίθμου
        start_time = time.time()
        incremental_hull(points)
        incremental_time = time.time() - start_time

        # Μέτρηση απόδοσης του αλγορίθμου Gift Wrapping
        start_time = time.time()
        gift_wrapping(points)
        gift_wrapping_time = time.time() - start_time

        # Μέτρηση απόδοσης του αλγορίθμου Divide and Conquer
        start_time = time.time()
        divide_and_conquer(points)
        divide_and_conquer_time = time.time() - start_time

        # Μέτρηση απόδοσης του αλγορίθμου QuickHull
        start_time = time.time()
        quickhull(points)
        quickhull_time = time.time() - start_time

        # Αποθήκευση αποτελεσμάτων για αυτό το μέγεθος εισόδου
        results.append((size, incremental_time, gift_wrapping_time, divide_and_conquer_time, quickhull_time))

    return results

def fit_polynomial(x, y, degree=3):
    """
    Προσαρμογή πολυωνύμου δεδομένου βαθμού στα δεδομένα.
    
    Είσοδος: Λίστα x-τιμών (ανεξάρτητη μεταβλητή), λίστα y-τιμών (εξαρτημένη μεταβλητή), βαθμός του πολυωνύμου.
    Έξοδος: Προσαρμοσμένες y-τιμές.
    """
    coefficients = np.polyfit(x, y, degree)
    polynomial = np.poly1d(coefficients)
    return polynomial(x)

if __name__ == "__main__":
    # Ορισμός μεγεθών συνόλων σημείων για τη μέτρηση
    sizes = np.linspace(10, 100000000, num=3).astype(int)

    # Εκτέλεση της μέτρησης
    results = benchmark_algorithms(sizes)

    # Εξαγωγή αποτελεσμάτων για την απεικόνιση
    sizes = [result[0] for result in results]
    incremental_times = [result[1] for result in results]
    gift_wrapping_times = [result[2] for result in results]
    divide_and_conquer_times = [result[3] for result in results]
    quickhull_times = [result[4] for result in results]

    # Απεικόνιση των αποτελεσμάτων
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, incremental_times, label="Αυξητικός", marker='o')
    plt.plot(sizes, gift_wrapping_times, label="Περιτύλιγμα", marker='o')
    plt.plot(sizes, divide_and_conquer_times, label="Διαίρει και Βασίλευε", marker='o')
    plt.plot(sizes, quickhull_times, label="QuickHull", marker='o')

    # Προσθήκη ετικετών και τίτλου
    plt.xlabel("Αριθμός Σημείων", fontsize=12)
    plt.ylabel("Χρόνος Εκτέλεσης (δευτερόλεπτα)", fontsize=12)
    plt.title("Σύγκριση Αλγορίθμων Κυρτού Περιβλήματος", fontsize=14)
    plt.legend()
    plt.grid()
    plt.show()
