import abc
from src.individuo import Individuo

class ABSMutacao(object):

	@abc.abstractmethod
	def aplicar_mutacao(self, individuo: Individuo) -> Individuo:
		raise NotImplementedError()