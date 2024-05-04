import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.winter,  s=10)

# Задати назву для графік та кожної з її осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squer of Value", fontsize=14)

# Задати розмір шрифтудля підписів на розмітці.
ax.tick_params(labelsize=14)

plt.show()