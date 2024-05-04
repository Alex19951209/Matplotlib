from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Створити три кубики D6.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Зробити декілька кидків та зберегти результат у список.
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

# Проаналізувати результати.
frecuencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)
for value in poss_results:
	frecuency = results.count(value)
	frecuencies.append(frecuency)

# Візуалізувати результат.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frecuencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frecuency of Result'}
m_layout = Layout(title='Result of rolling two D6 1000 times',
		xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': m_layout}, filename='d6_d6_d6.html')