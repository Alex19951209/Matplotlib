import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Створити випадкове блукання.
rw = RandomWalk(50_000)
rw.fill_walk()

# Нанести на графік точки блукання.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)
ax.set_aspect('equal')

# Виокремити першу та останю точки.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
	 s=100)

# Приховати осі.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()