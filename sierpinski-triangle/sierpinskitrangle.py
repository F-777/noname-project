import matplotlib.pyplot as plt
import numpy as np

def sierpinski_triangle(vertices, level):
    if level == 0:
        plt.fill(vertices[:, 0], vertices[:, 1], 'k')
    else:
        mid_points = (vertices + np.roll(vertices, 1, axis=0)) / 2
        sierpinski_triangle(vertices[:2, :], level - 1)
        sierpinski_triangle(vertices[1:, :], level - 1)
        sierpinski_triangle(mid_points, level - 1)

# Define the vertices of the main triangle
vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])

# Create the plot
plt.figure(figsize=(8, 8))
sierpinski_triangle(vertices, 5)
plt.axis('equal')
plt.axis('off')
plt.show()
