from random import uniform

from src.crossover.abs_crossover import ABSCrossoverBlend, ABSCrossoverLinear, ABSCrossoverMedia
from src.individuo import Individuo


class CrossoverMedia(ABSCrossoverMedia):

	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		"""Resulta em um filho com a média dos cromossomo dos dois pais"""

		return Individuo((pai1.cromossomo + pai2.cromossomo) / 2)


class CrossoverBlend(ABSCrossoverBlend):

	__alpha = 0.5

	@staticmethod
	def aplicar(pai1: Individuo, pai2: Individuo) -> Individuo:
		"""Resulta em um filho com cromossomo derivado dos dois pais"""

		beta = uniform(CrossoverBlend.__alpha, 1 + CrossoverBlend.__alpha)

		# C = p1 + beta(p2 - p1) -> beta = U(-alpha, 1 + alpha)
		return Individuo(pai1.cromossomo + beta * (pai2.cromossomo - pai1.cromossomo))


class CrossoverLinear(ABSCrossoverLinear):

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