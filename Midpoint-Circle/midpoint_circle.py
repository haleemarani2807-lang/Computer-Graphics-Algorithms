import matplotlib.pyplot as plt

xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))

x = 0
y = r
p = 1 - r

points_x = []
points_y = []

while x <= y:
    points_x.extend([
        xc + x, xc - x, xc + x, xc - x,
        xc + y, xc - y, xc + y, xc - y
    ])

    points_y.extend([
        yc + y, yc + y, yc - y, yc - y,
        yc + x, yc + x, yc - x, yc - x
    ])

    x += 1

    if p < 0:
        p += 2 * x + 1
    else:
        y -= 1
        p += 2 * (x - y) + 1

plt.scatter(points_x, points_y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Midpoint Circle Drawing Algorithm")
plt.axis("equal")
plt.grid(True)
plt.show()
