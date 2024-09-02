import matplotlib.pyplot as plt
import random

def chaos_game(iterations, vertices):
    # Start at an arbitrary point, usually one of the vertices
    x, y = vertices[0]
    
    # Lists to hold the x and y coordinates of points
    x_coords = [x]
    y_coords = [y]
    
    for _ in range(iterations):
        # Choose a random vertex
        vx, vy = random.choice(vertices)
        
        # Move halfway towards the chosen vertex
        x = (x + vx) / 2
        y = (y + vy) / 2
        
        # Store the new point
        x_coords.append(x)
        y_coords.append(y)
    
    return x_coords, y_coords

# Define the vertices of the triangle
vertices = [(0, 0), (1, 0), (0.5, 0.866)]

# Number of iterations
iterations = 10000

# Run the Chaos Game
x_coords, y_coords = chaos_game(iterations, vertices)

# Plot the points
plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, 'k.', markersize=0.5)
plt.axis('equal')
plt.axis('off')
plt.show()
