import numpy as np
import matplotlib.pyplot as plt

class KDNode:
    """
    Κλάση που αναπαριστά έναν κόμβο του KD-Tree.
    """
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    """
    Κατασκευή KD-Tree από μια λίστα σημείων.
    
    Είσοδος: Λίστα σημείων, βάθος του δέντρου.
    Έξοδος: Ρίζα του KD-Tree.
    """
    if not points:
        return None
    
    k = len(points[0])  # 2D περίπτωση
    axis = depth % k  # Επιλογή άξονα βάσει του βάθους
    points.sort(key=lambda x: x[axis])  # Ταξινόμηση σημείων βάσει του επιλεγμένου άξονα
    median = len(points) // 2  # Εύρεση της μέσης τιμής
    
    # Δημιουργία κόμβου και αναδρομική κατασκευή των υποδέντρων
    return KDNode(
        points[median],
        build_kd_tree(points[:median], depth + 1),
        build_kd_tree(points[median + 1:], depth + 1)
    )

def visualize_kd_tree(points, tree, depth=0, bounds=(-1, 100, -1, 100)):
    """
    Οπτικοποίηση του KD-Tree.
    
    Είσοδος: Λίστα σημείων, ρίζα του KD-Tree, βάθος του δέντρου, όρια του γραφήματος.
    Έξοδος: Καμία.
    """
    if tree is None:
        return
    
    x_min, x_max, y_min, y_max = bounds
    axis = depth % 2  # Επιλογή άξονα βάσει του βάθους
    x, y = tree.point
    
    plt.scatter(x, y, color='black', zorder=3)  # Σχεδίαση του σημείου
    
    if axis == 0:
        # Σχεδίαση κάθετης γραμμής διαχωρισμού
        plt.plot([x, x], [y_min, y_max], 'r--', zorder=2)
        plt.pause(0.5)
        # Αναδρομική οπτικοποίηση των υποδέντρων
        visualize_kd_tree(points, tree.left, depth + 1, (x_min, x, y_min, y_max))
        visualize_kd_tree(points, tree.right, depth + 1, (x, x_max, y_min, y_max))
    else:
        # Σχεδίαση οριζόντιας γραμμής διαχωρισμού
        plt.plot([x_min, x_max], [y, y], 'b--', zorder=2)
        plt.pause(0.5)
        # Αναδρομική οπτικοποίηση των υποδέντρων
        visualize_kd_tree(points, tree.left, depth + 1, (x_min, x_max, y_min, y))
        visualize_kd_tree(points, tree.right, depth + 1, (x_min, x_max, y, y_max))

if __name__ == "__main__":
    # Δημιουργία τυχαίων σημείων
    np.random.seed(12)
    sample_points = [(np.random.uniform(20, 80), np.random.uniform(20, 80)) for _ in range(10)]
    
    # Κατασκευή του KD-Tree
    kd_tree = build_kd_tree(sample_points)
    
    # Οπτικοποίηση του KD-Tree
    plt.figure(figsize=(6, 6))
    plt.scatter(*zip(*sample_points), color='blue', zorder=1)
    visualize_kd_tree(sample_points, kd_tree)
    plt.xlim(-1, 100)
    plt.ylim(-1, 100)
    plt.title("KD-Tree Construction Steps")
    plt.show()