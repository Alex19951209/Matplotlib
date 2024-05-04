import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Задати назву для графіка та кожної з осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squer of Value", fontsize=14)

# Задати розмір шрифту для підписів на розмітці.
ax.tick_params(axis='both', which='major', labelsize=14)

# Задати діапазон для кожної з осей.
ax.axis([0, 1100, 0, 1100000])

plt.show()