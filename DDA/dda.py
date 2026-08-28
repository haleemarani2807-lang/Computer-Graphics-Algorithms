import matplotlib.pyplot as plt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

x_inc = dx / steps
y_inc = dy / steps

x = x1
y = y1

points_x = []
points_y = []

for i in range(steps + 1):
    points_x.append(round(x))
    points_y.append(round(y))
    x += x_inc
    y += y_inc

plt.plot(points_x, points_y, 'ro-')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("DDA Line Drawing Algorithm")
plt.grid(True)
plt.show()
