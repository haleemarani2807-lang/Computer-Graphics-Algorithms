import matplotlib.pyplot as plt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x2 > x1 else -1
sy = 1 if y2 > y1 else -1

x = x1
y = y1

points_x = []
points_y = []

if dx > dy:
    p = 2 * dy - dx

    for i in range(dx + 1):
        points_x.append(x)
        points_y.append(y)

        if p >= 0:
            y += sy
            p += 2 * (dy - dx)
        else:
            p += 2 * dy

        x += sx

else:
    p = 2 * dx - dy

    for i in range(dy + 1):
        points_x.append(x)
        points_y.append(y)

        if p >= 0:
            x += sx
            p += 2 * (dx - dy)
        else:
            p += 2 * dx

        y += sy

plt.plot(points_x, points_y, 'bo-')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Bresenham Line Drawing Algorithm")
plt.grid(True)
plt.show()
