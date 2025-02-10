import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def simplex(c, A, b):
    """
    Solves the linear programming problem using the Simplex method.
    
    Maximizes: c^T x
    Subject to: Ax <= b, x >= 0
    """
    m, n = A.shape

    # Convert the problem to standard form by adding slack variables
    A = np.hstack([A, np.eye(m)])  # Add identity matrix for slack variables
    c = np.concatenate([c, np.zeros(m)])  # Extend cost function with zeros for slack variables

    # Initializing Simplex Tableau
    tableau = np.zeros((m + 1, n + m + 1))
    tableau[:-1, :-1] = A
    tableau[:-1, -1] = b
    tableau[-1, :-1] = -c  # Negative cost function for maximization

    # Basis tracking
    basis = list(range(n, n + m))

    while True:
        # Step 1: Check if optimal
        if np.all(tableau[-1, :-1] >= 0):
            break  # Optimal solution found

        # Step 2: Find entering variable (most negative in objective row)
        pivot_col = np.argmin(tableau[-1, :-1])

        # Step 3: Check for unboundedness
        if np.all(tableau[:-1, pivot_col] <= 0):
            raise ValueError("Unbounded Solution")

        # Step 4: Find leaving variable (minimum positive ratio test)
        ratios = np.divide(tableau[:-1, -1], tableau[:-1, pivot_col], 
                           out=np.full(m, np.inf), where=tableau[:-1, pivot_col] > 0)
        pivot_row = np.argmin(ratios)

        # Step 5: Pivoting
        tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]  # Normalize pivot row
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

        # Update basis
        basis[pivot_row] = pivot_col

    # Extract solution
    solution = np.zeros(n + m)
    solution[basis] = tableau[:-1, -1]
    
    return solution[:n], tableau[-1, -1]  # Return only the decision variables


# Problem Definition
c = np.array([3, -10])  # Maximize 3x1 - 10x2
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

# Add missing constraints: x1 >= 0 and x2 >= 0 (corrected)
A = np.vstack([A, [-1, 0]])  # x1 >= 0 → -x1 <= 0
b = np.append(b, 0)

A = np.vstack([A, [0, -1]])  # x2 >= 0 → -x2 <= 0
b = np.append(b, 0)

# Solve using the Simplex Algorithm
solution, optimal_value = simplex(c, A, b)

# Display results
print("Optimal Solution: ", solution)
print("Optimal Value: ", optimal_value)

# =================== PLOTTING FEASIBLE REGION ===================
x1_vals = np.linspace(-5, 10, 400)
x2_vals = np.linspace(-5, 10, 400)
X1, X2 = np.meshgrid(x1_vals, x2_vals)

# Define the inequalities
feasible_region = np.ones(X1.shape, dtype=bool)

for i in range(A.shape[0]):
    feasible_region &= (A[i, 0] * X1 + A[i, 1] * X2 <= b[i])

# Plot the feasible region
plt.figure(figsize=(8, 6))
plt.contourf(X1, X2, feasible_region, levels=[0.5, 1], colors=['lightblue'], alpha=0.5)

# Plot constraint lines
for i in range(A.shape[0]):
    if A[i, 1] != 0:  # Avoid division by zero for vertical lines (x1 >= 0)
        y = (b[i] - A[i, 0] * x1_vals) / A[i, 1]
        plt.plot(x1_vals, y, label=f'Constraint {i+1}')
    else:  # Vertical constraint (x1 = 0)
        plt.axvline(b[i] / A[i, 0], color='black', linestyle='--', label=f'Constraint {i+1}')

# Plot optimal solution
if solution is not None:
    plt.scatter(solution[0], solution[1], color='red', marker='o', label="Optimal Solution", zorder=3)

# Create a custom legend entry for the feasible region
feasible_patch = Patch(color='lightblue', alpha=0.5, label="Feasible Region")

# Labels and show plot
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title("Feasible Region and Optimal Solution using Simplex Algorithm")
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.legend(handles=[feasible_patch] + plt.gca().get_legend_handles_labels()[0], loc='lower left')
plt.grid(True)
plt.show()
