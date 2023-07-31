import matplotlib.pyplot as plt

def drawEllipse(a, b):
    x0, y0 = 0, b  # Starting point (center of the ellipse)
    a_sqr = a * a
    b_sqr = b * b

    # Region 1 (x > 0)
    dx = 2 * b_sqr * x0
    dy = 2 * a_sqr * y0
    d1 = b_sqr - (a_sqr * b) + (0.25 * a_sqr)

    while dx < dy:
        plt.plot(x0, y0, 'bo')  # Plotting the current pixel
        plt.plot(x0, -y0, 'bo')  # Reflecting the pixel in the bottom half
        if d1 < 0:
            x0 += 1
            dx += 2 * b_sqr
            d1 += dx + b_sqr
        else:
            x0 += 1
            y0 -= 1
            dx += 2 * b_sqr
            dy -= 2 * a_sqr
            d1 += dx - dy + b_sqr

    # Region 2 (x <= 0)
    d2 = (
        b_sqr * (x0 + 0.5) * (x0 + 0.5) +
        a_sqr * (y0 - 1) * (y0 - 1) -
        a_sqr * b_sqr
    )
    while y0 >= 0:
        plt.plot(x0, y0, 'bo')  # Plotting the current pixel
        plt.plot(x0, -y0, 'bo')  # Reflecting the pixel in the bottom half
        if d2 > 0:
            y0 -= 1
            dy -= 2 * a_sqr
            d2 += a_sqr - dy
        else:
            y0 -= 1
            x0 += 1
            dx += 2 * b_sqr
            dy -= 2 * a_sqr
            d2 += dx - dy + a_sqr

    plt.gca().set_aspect('equal', adjustable='box')  # Set aspect ratio to be equal
    plt.show()

if __name__ == "__main__":
    a = 5  # Semi-major axis length
    b = 3  # Semi-minor axis length
    drawEllipse(a, b)
