import abc

from src.individuo import Individuo

# MÉTODOS NÃO IMPLEMENTADOS:
# - Crossover Simples

class ABSCrossover(object):

	@staticmethod
	@abc.abstractmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()


class ABSCrossoverMedia(ABSCrossover):
	"""Resulta em um filho com a média dos cromossomo dos dois pais"""

	@staticmethod
	@abc.abstractmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()


class ABSCrossoverBlend(ABSCrossover):
	"""Resulta em um filho com cromossomo derivado dos dois pais"""

	@staticmethod
	@abc.abstractmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()


class ABSCrossoverLinear(ABSCrossover):
	"""Resulta em no filho mais apto entre três filhos gerados"""

	@staticmethod
	@abc.abstractmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()


# Métodos crossover descritos por Michalewicz

class ABSCrossoverAritmetico(ABSCrossover):
	"""Crossover semelhante ao BLX, porém não extrapolar os valores dos pais"""

	@staticmethod
	@abc.abstractmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()


class ABSCrossoverHeuristico(ABSCrossover):
	"""Crossover que pode extrapolar os cromossomos dos pais dependendo da aptidão"""

	@staticmethod
	@abc.abstractmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()