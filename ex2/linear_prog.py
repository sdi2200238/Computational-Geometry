import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def simplex(c, A, b):
    """
    Υλοποίηση της μεθόδου Simplex για την επίλυση προβλημάτων γραμμικού προγραμματισμού.
    
    Μέγιστο: c^T x
    Υπό συνθήκη: Ax <= b, x >= 0
    """
    m, n = A.shape

    # Μετατροπή του προβλήματος σε τυπική μορφή προσθέτοντας μεταβλητές χαλάρωσης
    A = np.hstack([A, np.eye(m)])  # Προσθήκη ταυτοτικής μήτρας για τις μεταβλητές χαλάρωσης
    c = np.concatenate([c, np.zeros(m)])  # Επέκταση της συνάρτησης κόστους με μηδενικά για τις μεταβλητές χαλάρωσης

    # Αρχικοποίηση του Simplex 
    tableau = np.zeros((m + 1, n + m + 1))
    tableau[:-1, :-1] = A
    tableau[:-1, -1] = b
    tableau[-1, :-1] = -c  # Αρνητική συνάρτηση κόστους για μεγιστοποίηση

    # Παρακολούθηση βάσης
    basis = list(range(n, n + m))

    while True:
        # Έλεγχος αν είναι βέλτιστο
        if np.all(tableau[-1, :-1] >= 0):
            break  # Βρέθηκε βέλτιστη λύση

        # Εύρεση εισερχόμενης μεταβλητής (πιο αρνητική στην γραμμή του στόχου)
        pivot_col = np.argmin(tableau[-1, :-1])

        # Έλεγχος για απεριόριστη λύση
        if np.all(tableau[:-1, pivot_col] <= 0):
            raise ValueError("Απεριόριστη Λύση")

        # Εύρεση εξερχόμενης μεταβλητής (ελάχιστος θετικός λόγος)
        ratios = np.divide(tableau[:-1, -1], tableau[:-1, pivot_col], 
                           out=np.full(m, np.inf), where=tableau[:-1, pivot_col] > 0)
        pivot_row = np.argmin(ratios)

        # Pivoting
        tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]  # Κανονικοποίηση γραμμής pivot
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

        # Ενημέρωση βάσης
        basis[pivot_row] = pivot_col

    # Εξαγωγή λύσης
    solution = np.zeros(n + m)
    solution[basis] = tableau[:-1, -1]
    
    return solution[:n], tableau[-1, -1]  # Επιστροφή μόνο των μεταβλητών απόφασης


if __name__ == "__main__":
    # Ορισμός του προβλήματος
    c = np.array([3, -10])  # Μέγιστο 3x1 - 10x2
    A = np.array([
        [-2, 1],
        [-1, 3],
        [6, 7],
        [3, -12],
        [2, -7],
        [-1, 8],
        [2, -6],
    ])
    b = np.array([12, 3, 18, -8, 35, 29, 9])

    # Προσθήκη των περιορισμών: x1 >= 0 και x2 >= 0
    A = np.vstack([A, [-1, 0]])  # x1 >= 0 → -x1 <= 0
    b = np.append(b, 0)

    A = np.vstack([A, [0, -1]])  # x2 >= 0 → -x2 <= 0
    b = np.append(b, 0)

    # Επίλυση με τη μέθοδο Simplex
    solution, optimal_value = simplex(c, A, b)

    # Εμφάνιση αποτελεσμάτων
    print("Βέλτιστη Λύση: ", solution)
    print("Βέλτιστη Τιμή: ", optimal_value)

    # =================== ΑΠΕΙΚΟΝΙΣΗ ΕΦΙΚΤΗΣ ΠΕΡΙΟΧΗΣ ===================
    x1_vals = np.linspace(-5, 10, 400)
    x2_vals = np.linspace(-5, 10, 400)
    X1, X2 = np.meshgrid(x1_vals, x2_vals)

    # Ορισμός των ανισοτήτων
    feasible_region = np.ones(X1.shape, dtype=bool)

    for i in range(A.shape[0]):
        feasible_region &= (A[i, 0] * X1 + A[i, 1] * X2 <= b[i])

    # Απεικόνιση της εφικτής περιοχής
    plt.figure(figsize=(8, 6))
    plt.contourf(X1, X2, feasible_region, levels=[0.5, 1], colors=['lightblue'], alpha=0.5)

    # Απεικόνιση των γραμμών περιορισμών
    for i in range(A.shape[0]):
        if A[i, 1] != 0:  # Αποφυγή διαίρεσης με το μηδέν για κάθετες γραμμές (x1 >= 0)
            y = (b[i] - A[i, 0] * x1_vals) / A[i, 1]
            plt.plot(x1_vals, y, label=f'Περιορισμός {i+1}')
        else:  # Κάθετος περιορισμός (x1 = 0)
            plt.axvline(b[i] / A[i, 0], color='black', linestyle='--', label=f'Περιορισμός {i+1}')

    # Απεικόνιση της βέλτιστης λύσης
    if solution is not None:
        plt.scatter(solution[0], solution[1], color='red', marker='o', label="Βέλτιστη Λύση", zorder=3)

    # Δημιουργία προσαρμοσμένης εγγραφής για την εφικτή περιοχή
    feasible_patch = Patch(color='lightblue', alpha=0.5, label="Εφικτή Περιοχή")

    # Ετικέτες και εμφάνιση γραφήματος
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.title("Εφικτή Περιοχή και Βέλτιστη Λύση με τη Μέθοδο Simplex")
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.legend(handles=[feasible_patch] + plt.gca().get_legend_handles_labels()[0], loc='lower left')
    plt.grid(True)
    plt.show()
