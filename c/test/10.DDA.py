import matplotlib.pyplot as plt


def dda_line(x1, y1, x2, y2):
    # Calculate the change in x and y
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the number of steps needed based on the greater absolute difference between dx and dy
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calculate the increment along x and y for each step
    x_increment = dx / steps
    y_increment = dy / steps

    # Initialize the starting point of the line
    x = x1
    y = y1

    # List to store the points of the line
    points = []

    # Add the starting point to the list
    points.append((round(x), round(y)))

    # Incrementally calculate and add points to the list until the end point is reached
    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))

    return points


# Example usage:
if __name__ == "__main__":
    # Define the two points of the line (x1, y1) and (x2, y2)
    x1, y1 = 2, 7
    x2, y2 = 3, 2

    # Get the points of the line using the DDA algorithm
    line_points = dda_line(x1, y1, x2, y2)

    # Extract the x and y coordinates from the list of points
    x_values, y_values = zip(*line_points)

    # Plot the line using Matplotlib
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('DDA Line Drawing Algorithm')
    plt.grid(True)
    plt.show()
