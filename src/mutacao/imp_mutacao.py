from random import uniform

from src.individuo import Individuo
from src.mutacao.abs_mutacao import *


class MutacaoUniforme(ABSMutacao):

	@staticmethod
	@abc.abstractmethod
	def aplicar_mutacao(individuo: Individuo, g_atual: int, g_max: int) -> Individuo:
		"""Altera o cromossomo do indivíduo com um valor entre o mínimo e máximo do domínio"""

		individuo.cromossomo = uniform(individuo.dMin, individuo.dMax)
		return individuo


class MutacaoLimite(ABSMutacao):

	@staticmethod
	@abc.abstractmethod
	def aplicar_mutacao(individuo: Individuo, g_atual: int, g_max: int):
		"""Sorteia um dos extremos do domínio para ser o valor do gene"""

		r = uniform(0, 1)

		individuo.cromossomo = individuo.dMin if r < 0.5 else individuo.dMax

		return individuo


class MutacaoNaoUniforme(ABSMutacao):

	@staticmethod
	@abc.abstractmethod
	def aplicar_mutacao(individuo: Individuo, g_atual: int, g_max: int):
		"""Substitui o gene por um número de uma distribuição não uniforme"""

		r1 = uniform(0, 1)
		r2 = uniform(0, 1)

		f = (r2 * (1 - g_atual / g_max)) ** individuo.dMax

		if r1 < 0.5:
			novo_cromossomo = individuo.cromossomo + (individuo.dMax - individuo.cromossomo) * f
		else:
			novo_cromossomo = individuo.cromossomo - (individuo.cromossomo - individuo.dMin) * f

		individuo.cromossomo = novo_cromossomo
