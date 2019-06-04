import abc
from src.individuo import Individuo

class ABSCrossover(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def crossover(self, pai1: Individuo, pai2: Individuo):
        raise NotImplementedError()