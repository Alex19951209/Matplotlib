import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=40)

# Задати назву для графік та кожної з її осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squer of Value", fontsize=14)

# Задати розмір шрифту для підписів на розмітці.
ax.tick_params(labelsize=14)

plt.show()