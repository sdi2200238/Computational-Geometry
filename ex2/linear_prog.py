import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from scipy.optimize import linprog

def solve_and_plot(A, b, c, step, final_step):
    # Επίλυση με τη μέθοδο 
    res = linprog(-c, A_ub=A, b_ub=b, method='highs')

    # Εμφάνιση αποτελεσμάτων
    if res.success:
        solution = res.x
        optimal_value = res.fun
        print(f"Βήμα {step}:")
        print("Βέλτιστη Λύση: ", solution)
        print("Βέλτιστη Τιμή: ", -optimal_value)
    else:
        print(f"Βήμα {step}: Το πρόβλημα δεν έχει λύση.")

    # Απεικόνιση μόνο στο τελικό βήμα
    if step == final_step:
        # Ορισμός των τιμών x1 και x2
        x1_vals = np.linspace(-5, 10, 400)
        x2_vals = np.linspace(-5, 10, 400)
        X1, X2 = np.meshgrid(x1_vals, x2_vals)

        # Ορισμός των ανισοτήτων
        feasible_region = np.ones(X1.shape, dtype=bool)

        # Έλεγχος αν οι τιμές των μεταβλητών x1 και x2 είναι εφικτές
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
        if res.success:
            plt.scatter(solution[0], solution[1], color='red', marker='o', label="Βέλτιστη Λύση", zorder=3)

        # Δημιουργία προσαρμοσμένης εγγραφής για την εφικτή περιοχή
        feasible_patch = Patch(color='lightblue', alpha=0.5, label="Εφικτή Περιοχή")

        # Ετικέτες και εμφάνιση γραφήματος
        plt.xlabel('$x_1$')
        plt.ylabel('$x_2$')
        plt.title(f"Εφικτή Περιοχή και Βέλτιστη Λύση")
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        plt.xlim(-5, 5)
        plt.ylim(-5, 5)
        plt.legend(handles=[feasible_patch] + plt.gca().get_legend_handles_labels()[0], loc='lower left')
        plt.grid(True)
        plt.show()

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
        [-1, 0],
        [0, -1],
        
    ])
    b = np.array([12, 3, 18, -8, 35, 29, 9, 0, 0])

    # Επίλυση και απεικόνιση βήμα προς βήμα
    final_step = A.shape[0]
    for i in range(1, final_step + 1):
        solve_and_plot(A[:i], b[:i], c, i, final_step)
