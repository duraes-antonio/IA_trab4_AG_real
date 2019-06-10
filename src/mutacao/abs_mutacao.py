import abc
from src.individuo import Individuo


# MÉTODOS NÃO IMPLEMENTADOS:
# - Mutação não-uniforme múltipla
# - Mutação creep

class ABSMutacao(object):

    @staticmethod
    @abc.abstractmethod
    def aplicar_mutacao(individuo: Individuo) -> Individuo:
        raise NotImplementedError()