import abc

from src.individuo import Individuo

# MÉTODOS NÃO IMPLEMENTADOS:
# - Crossover Simples

class ABSCrossover(object):

	@staticmethod
	@abc.abstractmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		raise NotImplementedError()
