from random import uniform

from src.individuo import Individuo
from src.mutacao.abs_mutacao import *


class MutacaoUniforme(ABSMutacao):

	@staticmethod
	@abc.abstractmethod
	def aplicar_mutacao(individuo: Individuo) -> Individuo:
		"""Altera o cromossomo do indivíduo com um valor entre o mínimo e máximo do domínio"""

		individuo.cromossomo = uniform(individuo.dMin, individuo.dMax)
		return individuo


class MutacaoLimite(ABSMutacao):

	@staticmethod
	@abc.abstractmethod
	def aplicar_mutacao(individuo: Individuo):
		"""Sorteia um dos extremos do domínio para ser o valor do gene"""

		r = uniform(0, 1)

		individuo.cromossomo = individuo.dMin if r < 0.5 else individuo.dMax

		return individuo


class MutacaoNaoUniforme(ABSMutacao):

	@staticmethod
	@abc.abstractmethod
	def aplicar_mutacao(individuo: Individuo):
		"""Substitui o gene por um número de uma distribuição não uniforme"""
		#TODO finalizar implementação
		raise NotImplementedError()


class MutacaoGaussiana(ABSMutacao):

	@staticmethod
	@abc.abstractmethod
	def aplicar_mutacao(individuo: Individuo):
		"""Substitui o gene por um número aleatório de uma distribuição gaussiana"""
		# TODO finalizar implementação
		raise NotImplementedError()