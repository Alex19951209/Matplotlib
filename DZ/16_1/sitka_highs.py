import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Отримати дані опадів з цього файлу.
	highs = []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[8])
		except ValueError:
			print(f"Missing date for {current_date}")
		else:
			highs.append(high)

print(highs)