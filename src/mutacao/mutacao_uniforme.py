from random import uniform

from src.individuo import Individuo
from src.mutacao.abs_mutacao import ABSMutacao


class MutacaoUniforme(ABSMutacao):
	"""Altera o cromossomo do indivíduo com um valor entre o mínimo e máximo do domínio"""

	def aplicar_mutacao(self, individuo: Individuo) -> Individuo:
		individuo.cromossomo = uniform(individuo.dMin, individuo.dMax)
		return individuo