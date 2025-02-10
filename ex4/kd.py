import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree
import random

class KDNode:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    """
    Υλοποίηση της συνάρτησης για την κατασκευή του δέντρου k-d.
    
    Είσοδος: Λίστα σημείων και βάθος του δέντρου.
    Έξοδος: Ρίζα του δέντρου k-d.
    """
    if not points:
        return None
    
    k = len(points[0])  # Διαστάσεις (2D περίπτωση)
    axis = depth % k
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2
    
    return KDNode(
        points[median],
        build_kd_tree(points[:median], depth + 1),
        build_kd_tree(points[median + 1:], depth + 1)
    )

def range_search(node, rect, depth=0, found_points=[]):
    """
    Υλοποίηση της συνάρτησης για την εύρεση σημείων εντός ορθογωνίου.
    
    Είσοδος: Ρίζα του δέντρου k-d, ορθογώνιο αναζήτησης, βάθος του δέντρου, λίστα με τα βρεθέντα σημεία.
    Έξοδος: Λίστα σημείων εντός του ορθογωνίου.
    """
    if node is None:
        return
    
    x_min, x_max, y_min, y_max = rect
    x, y = node.point
    
    if x_min <= x <= x_max and y_min <= y <= y_max:
        found_points.append(node.point)
    
    axis = depth % 2
    if axis == 0:
        if x_min <= x:
            range_search(node.left, rect, depth + 1, found_points)
        if x <= x_max:
            range_search(node.right, rect, depth + 1, found_points)
    else:
        if y_min <= y:
            range_search(node.left, rect, depth + 1, found_points)
        if y <= y_max:
            range_search(node.right, rect, depth + 1, found_points)
    
    return found_points

def plot_kd_tree(points, tree, rect=None):
    """
    Υλοποίηση της συνάρτησης για την απεικόνιση του δέντρου k-d και των σημείων εντός ορθογωνίου.
    
    Είσοδος: Λίστα σημείων, ρίζα του δέντρου k-d, ορθογώνιο αναζήτησης.
    Έξοδος: Καμία.
    """
    fig, ax = plt.subplots()
    ax.scatter(*zip(*points), color='blue', label='Points')
    
    if rect:
        x_min, x_max, y_min, y_max = rect
        rect_patch = plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, 
                                   linewidth=1, edgecolor='red', facecolor='none', linestyle='dashed')
        ax.add_patch(rect_patch)
        inside_points = range_search(tree, rect, 0, [])
        ax.scatter(*zip(*inside_points), color='red', label='Inside Rectangle')
    
    ax.legend()
    plt.xlabel("X-axis", fontsize=12)
    plt.ylabel("Y-axis", fontsize=12)
    plt.title("KD-Tree Range Search Visualization", fontsize=14)
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # Δημιουργία τυχαίων 2D σημείων
    np.random.seed(12)
    num_points = 150
    points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_points)]

    # Κατασκευή του δέντρου k-d
    kd_tree = build_kd_tree(points)

    # Ορισμός ορθογωνίου αναζήτησης
    search_rect = (30, 70, 30, 70)
    found_points = range_search(kd_tree, search_rect)

    # Απεικόνιση του δέντρου k-d με την αναζήτηση εντός ορθογωνίου
    plot_kd_tree(points, kd_tree, search_rect)

    # Εκτύπωση των σημείων εντός του ορθογωνίου αναζήτησης
    print("Points inside the search rectangle:")
    print(found_points)
