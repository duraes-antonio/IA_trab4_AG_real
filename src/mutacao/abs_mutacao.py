import abc
from src.individuo import Individuo


# MÉTODOS NÃO IMPLEMENTADOS:
# - Mutação não-uniforme múltipla
# - Mutação Creep

class ABSMutacao(object):

    @abc.abstractmethod
    def aplicar_mutacao(self, individuo: Individuo) -> Individuo:
        raise NotImplementedError()


class ABSMutacaoUniforme(ABSMutacao):
    """Sorteia um valor dentro do intervalo aceito, caso extrapole, pega o valor padrão"""

    @abc.abstractmethod
    def aplicar_mutacao(self, individuo: Individuo):
        raise NotImplementedError()


class ABSMutacaoLimite(ABSMutacao):
    """Sorteia um dos extremos do domínio para ser o valor do gene"""

    @abc.abstractmethod
    def aplicar_mutacao(self, individuo: Individuo):
        raise NotImplementedError()


class ABSMutacaoNaoUniforme(ABSMutacao):
    """Substitui o gene por um número de uma distribuição não uniforme"""

    @abc.abstractmethod
    def aplicar_mutacao(self, individuo: Individuo):
        raise NotImplementedError()


class ABSMutacaoCreep(ABSMutacao):
    """Substitui o gene por um número aleatório de uma distribuição gaussiana"""

    @abc.abstractmethod
    def aplicar_mutacao(self, individuo: Individuo):
        raise NotImplementedError()
