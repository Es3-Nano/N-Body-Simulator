import bodies
import math

G = 10000

for p1 in bodies.Body.all_bodies:
    for p2 in bodies.Body.all_bodies:
        if p1 == p2:
            continue
        else:
            acc = G * p2.mass / math.sqrt((p1.x_pos - p2.x_pos) ** 2 + (p1.y_pos - p2.y_pos) ** 2)
            bodies.p1.update_acc(acc)
print(p1.x_acc)
