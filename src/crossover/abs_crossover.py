import abc

from src.individuo import Individuo


class ABSCrossover(object):

	@abc.abstractmethod
	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()


class ABSCrossoverMedia(ABSCrossover):
	"""Resulta em um filho com a média dos cromossomo dos dois pais"""

	@abc.abstractmethod
	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()


class ABSCrossoverBlend(ABSCrossover):
	"""Resulta em um filho com cromossomo derivado dos dois pais"""

	@abc.abstractmethod
	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()

class ABSCrossoverLinear(ABSCrossover):
	"""Resulta em no filho mais apto entre três filhos gerados"""

	@abc.abstractmethod
	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()

