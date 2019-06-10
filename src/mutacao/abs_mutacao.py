import abc
from src.individuo import Individuo


# MÉTODOS NÃO IMPLEMENTADOS:
# - Mutação não-uniforme múltipla
# - Mutação creep

class ABSMutacao(object):

    @staticmethod
    @abc.abstractmethod
    def aplicar_mutacao(self, individuo: Individuo) -> Individuo:
        raise NotImplementedError()


class ABSMutacaoUniforme(ABSMutacao):
    """Sorteia um valor dentro do intervalo aceito, caso extrapole, pega o valor padrão"""

    @staticmethod
    @abc.abstractmethod
    def aplicar_mutacao(self, individuo: Individuo) -> Individuo:
        raise NotImplementedError()


class ABSMutacaoLimite(ABSMutacao):
    """Sorteia um dos extremos do domínio para ser o valor do gene"""

    @staticmethod
    @abc.abstractmethod
    def aplicar_mutacao(self, individuo: Individuo) -> Individuo:
        raise NotImplementedError()


class ABSMutacaoNaoUniforme(ABSMutacao):
    """Substitui o gene por um número de uma distribuição não uniforme"""

    @staticmethod
    @abc.abstractmethod
    def aplicar_mutacao(self, individuo: Individuo) -> Individuo:
        raise NotImplementedError()


class ABSMutacaoGaussiana(ABSMutacao):
    """Substitui o gene por um número aleatório de uma distribuição gaussiana"""

    @staticmethod
    @abc.abstractmethod
    def aplicar_mutacao(self, individuo: Individuo) -> Individuo:
        raise NotImplementedError()
