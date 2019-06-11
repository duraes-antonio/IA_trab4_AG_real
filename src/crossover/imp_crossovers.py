from random import uniform

from src.crossover.abs_crossover import *
from src.individuo import Individuo


class CrossoverMedia(ABSCrossover):

	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		"""Resulta em um filho com a média dos cromossomo dos dois pais"""

		return Individuo((pai1.cromossomo + pai2.cromossomo) / 2)


class CrossoverBlend(ABSCrossover):

	__alpha = 0.5

	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		"""Resulta em um filho com cromossomo derivado dos dois pais"""

		beta = uniform(CrossoverBlend.__alpha, 1 + CrossoverBlend.__alpha)

		# C = p1 + beta(p2 - p1) -> beta = U(-alpha, 1 + alpha)
		return Individuo(pai1.cromossomo + beta * (pai2.cromossomo - pai1.cromossomo))


class CrossoverLinear(ABSCrossover):

	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		"""Resulta em no filho mais apto entre três filhos gerados"""
		filhos = [
			Individuo(0.5 * pai1.cromossomo + 0.5 * pai2.cromossomo),
			Individuo(1.5 * pai1.cromossomo - 0.5 * pai2.cromossomo),
			Individuo(-0.5 * pai1.cromossomo + 1.5 * pai2.cromossomo)
		]
		filho = min(filhos, key=lambda individuo: individuo.fitness)
		filhos = None
		return filho


class CrossoverAritmetico(ABSCrossover):

	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		"""Resulta em no filho mais apto entre dois, e não extrapolar o intervalo dos pais"""

		beta = uniform(0, 1)
		c1 = beta * pai1.cromossomo + (1 - beta) * pai2.cromossomo
		c2 = (1 - beta) * pai1.cromossomo + beta * pai2.cromossomo
		melhor_filho = min(c1, c2)
		return Individuo(melhor_filho)


class CrossoverHeuristico(ABSCrossover):

	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		"""Gera um filho considerando o pai mais apto. Descarta o filho se ele for infactível"""

		r = uniform(0, 1)
		mais_apto = min(pai1, pai2, key=lambda individuo: individuo.fitness)
		menos_apto = max(pai1, pai2, key=lambda individuo: individuo.fitness)

		cromo = mais_apto.cromossomo + r * (mais_apto.cromossomo - menos_apto.cromossomo)

		while cromo > mais_apto.dMax or cromo < mais_apto.dMin:
			r = uniform(0, 1)
			cromo = mais_apto.cromossomo + r * (mais_apto.cromossomo - menos_apto.cromossomo)

		return Individuo(cromo)
