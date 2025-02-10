import numpy as np
import matplotlib.pyplot as plt
import random

class KDNode:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if not points:
        return None
    
    k = len(points[0])  # 2D case
    axis = depth % k
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2
    
    return KDNode(
        points[median],
        build_kd_tree(points[:median], depth + 1),
        build_kd_tree(points[median + 1:], depth + 1)
    )

def visualize_kd_tree(points, tree, depth=0, bounds=(-1, 100, -1, 100)):
    if tree is None:
        return
    
    x_min, x_max, y_min, y_max = bounds
    axis = depth % 2
    x, y = tree.point
    
    plt.scatter(x, y, color='black', zorder=3)
    
    if axis == 0:
      plt.plot([x, x], [y_min, y_max], 'r--', zorder=2)
      plt.pause(0.5)
      visualize_kd_tree(points, tree.left, depth + 1, (x_min, x, y_min, y_max))
      visualize_kd_tree(points, tree.right, depth + 1, (x, x_max, y_min, y_max))
    else:
      plt.plot([x_min, x_max], [y, y], 'b--', zorder=2)
      plt.pause(0.5)
      visualize_kd_tree(points, tree.left, depth + 1, (x_min, x_max, y_min, y))
      visualize_kd_tree(points, tree.right, depth + 1, (x_min, x_max, y, y_max))

np.random.seed(12)
sample_points = [(np.random.uniform(20, 80), np.random.uniform(20, 80)) for _ in range(10)]
kdtree = build_kd_tree(sample_points)

plt.figure(figsize=(6, 6))
plt.scatter(*zip(*sample_points), color='blue', zorder=1)
visualize_kd_tree(sample_points, kdtree)
plt.xlim(-1, 100)
plt.ylim(-1, 100)
plt.title("KD-Tree Construction Steps")
plt.show()