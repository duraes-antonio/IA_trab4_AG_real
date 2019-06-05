from random import uniform


class Individuo(object):
	"""Representa um indivíduo biológico com código genético e valor de aptdão."""
	dMax = 10
	dMin = -10

	def __init__(self, cromossomo: float = None):
		"""Instancia um indivíduo novo ou a partir de um código genético existente.

		:param cromossomo: Código genético de um indivíduo já existente.
		"""

		self.cromossomo = cromossomo if cromossomo else uniform(self.dMin, self.dMax)
		self.fitness = self.__calc_fitness()

	def __calc_fitness(self) -> float:
		return self.cromossomo ** 2 - 3 * self.cromossomo + 4

	def __repr__(self):
		return f'Cromossomo = {self.cromossomo};Fitness = {self.fitness}'

	def __eq__(self, individuo2):
		return individuo2.cromossomo == self.cromossomo
