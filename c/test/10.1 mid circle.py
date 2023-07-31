import matplotlib.pyplot as plt


def draw_circle(center_x, center_y, radius):
    x = 0
    y = radius
    d = 1 - radius

    # Lists to store the points forming the circle
    points = []

    while x <= y:
        points.append((x + center_x, y + center_y))
        points.append((y + center_x, x + center_y))
        points.append((-x + center_x, y + center_y))
        points.append((-y + center_x, x + center_y))
        points.append((-x + center_x, -y + center_y))
        points.append((-y + center_x, -x + center_y))
        points.append((x + center_x, -y + center_y))
        points.append((y + center_x, -x + center_y))

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1

    return points


# Example usage:
if __name__ == "__main__":
    # Define the center and radius of the circle
    center_x, center_y = 0, 0
    radius = 3

    # Get the points of the circle using the Midpoint Circle Algorithm
    circle_points = draw_circle(center_x, center_y, radius)

    # Extract the x and y coordinates from the list of points
    x_values, y_values = zip(*circle_points)

    # Plot the circle using Matplotlib
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Midpoint Circle Algorithm')
    plt.grid(True)
    plt.show()
