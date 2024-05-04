from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Створити кубики D8.
die_1 = Die()
die_2 = Die()

# Зробити декілька кидків та зберегти результат у список.
results = []
for roll_num in range(100_000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Проаналізувати результати.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
	frequency = results.count(value)
	frequencies.append(frequency)

# Візуалізувати результати.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
ma_layout = Layout(title='Result of rolling two D8 1000 times',
		xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': ma_layout}, filename='d8_d8.html')