import matplotlib.pyplot as plt

# Визначити дані.
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Задати назву для графіка ко кожної з її осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Squer of Value", fontsize=24)

# Задати розмір шрифту для підписів на розмітці.
ax.tick_params(axis='both', labelsize=14)

# покозати графік.
plt.show()