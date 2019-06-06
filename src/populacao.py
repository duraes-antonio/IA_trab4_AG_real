from random import choice, uniform

from src.crossover.abs_crossover import ABSCrossover
from src.individuo import Individuo
from src.mutacao.abs_mutacao import ABSMutacao


class Populacao(object):
	"""Representa um conjunto de indivíduos.
	Contém operações de seleção, crossover e mutação."""

	def __init__(self, tx_mutacao: float, tx_cross: float, n_individ: int,
	             func_cross: ABSCrossover, func_mutacao: ABSMutacao):
		"""
		Instancia uma população com N indivíduos e com as taxas recebidas.

		:param tx_mutacao: Inteiro (entre 0 e 100) que representa a chance de um bit ser alterado.
		:param tx_cross: Inteiro (entre 0 e 100) que representa a chance de ocorrer um crossover.
		:param n_individ: Inteiro positivo. É a quantidade de indivíduos da população.
		:param func_cross: Função responsável pelo cruzamento de dois indivíduos.
		:param func_mutacao: Função responsável por aplicar a mutação em um indivíduo.
		"""

		# Atualize as propriedades com os valores recebidos
		self.n_ind = n_individ
		self.__taxa_mut = tx_mutacao
		self.__taxa_cross = tx_cross
		self.__func_cross = func_cross
		self.__func_mut = func_mutacao

		# Gera os indiviuos da população
		self.individuos: [Individuo] = [Individuo() for i in range(self.n_ind)]
		self.elite = Individuo(self.get_best_or_worst().cromossomo)

	def get_best_or_worst(self, best: bool = True) -> Individuo:
		"""
		Retorna o indivíduo mais adaptado ou menos adaptado.

		:param best: Se True, indica que deseja-se o melhor indivíduo, senão, o pior.
		:return: O melhor ou pior individuo da população com base no fitness (Quanto menor, melhor)
		"""

		aux = self.individuos[0]
		mult = 1 if best else -1

		for ind in self.individuos[1:]:
			aux = ind if ind.fitness * mult <= aux.fitness * mult else aux

		return aux

	def __apply_elite(self):
		temp_best = self.get_best_or_worst()

		if temp_best.fitness < self.elite.fitness:
			self.elite = Individuo(temp_best.cromossomo)

		# Se o pior individuo tiver o fitness pior que o da elite
		# Coloca a elite no lugar dele
		else:
			worst = self.get_best_or_worst(best=False)

			if worst.fitness > self.elite.fitness:
				idx = self.individuos.index(worst)
				self.individuos[idx] = Individuo(self.elite.cromossomo)

	def select(self):
		"""
		Seleciona os melhores individuos usando método de torneio com n = 2
		"""

		inds_selected = []

		for i in range(self.n_ind):
			# Escolhe aleatoriamente 2 individuos
			ind1 = choice(self.individuos)
			ind2 = choice(self.individuos)

			# O Individuo selecionado será o de menor fitness
			inds_selected.append(ind1 if ind1.fitness <= ind2.fitness else ind2)

		# Muda os individuos para os que foram selecionados
		self.individuos = inds_selected

		self.__apply_elite()

	def make_crossover(self):
		"""
		Cruza dois individuos pelo método recebido como parâmetro na criação da população
		"""

		children: [Individuo] = []

		while len(children) < self.n_ind:

			# Sorteia a taxa entre 0% e 100%
			tax = uniform(0, 100)

			# Escolhe aleatoriamente 2 individuos
			ind1: Individuo = choice(self.individuos)
			ind2: Individuo = choice(self.individuos)

			# Se a taxa estiver no intervalo aceitável
			if tax <= self.__taxa_cross:
				children.append(self.__func_cross.aplicar(ind1, ind2))

			else:
				children.append(ind1)
				children.append(ind2)

		# Atualiza os individuos para os filhos gerados
		self.individuos = children

		# Se o número de indivíduos ultrapassou o máximo (extrapolará 0 ou 1),
		# então remova o pior indivíduo
		if(len(self.individuos) > self.n_ind):
			self.individuos.remove(self.get_best_or_worst(best=False))



		self.__apply_elite()

	def apply_mutation(self):
		"""
		Aplica o processo de mutação no código genético de cada indivíduo se
		as condições estiverem dentro da taxa mínima.
		"""

		# Para cada individuo
		for ind in self.individuos:
			self.__func_mut.aplicar_mutacao(ind)

		self.__apply_elite()
