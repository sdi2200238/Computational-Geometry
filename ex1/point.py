import random

def generate_points(n):
    # Set the random seed so the points are always the same for comparison
    random.seed(0)    
    # Create a list to store the points
    points = []
    
    # Generate n random points
    for _ in range(n):
        x = random.uniform(0, 1000)  # Random x-coordinate
        y = random.uniform(0, 1000)  # Random y-coordinate
        points.append((x, y))  # Add the point as a tuple to the list
    
    return points