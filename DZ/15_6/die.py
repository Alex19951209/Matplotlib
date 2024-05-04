from random import randint

class Die:
	"""Клас репрезентує адин кубик"""

	def __init__(self, num_sides=8):
		"""Визначити кубик із восьма гранями."""
		self.num_sides = num_sides


	def roll(self):
		"""Повернути випадкове значення від 1 до 8."""
		return randint(1, self.num_sides)