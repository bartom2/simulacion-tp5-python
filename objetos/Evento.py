from abc import ABC, abstractmethod
import traceback


class Evento(ABC):
    def __init__(self, nombre):
        self._nombre = nombre
        self._prox_ev = None
        self._rnd = None
        self._tiempo = None

    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"nombre='{self._nombre}', "
                f"prox_ev={self._prox_ev}, "
                f"rnd={self._rnd}, "
                f"tiempo={self._tiempo})")

    @abstractmethod
    def calcular_prox_ev(self, reloj):
        pass

    def get_nombre(self):
        return self._nombre

    def get_prox_ev(self):
        return self._prox_ev

    def set_prox_ev_none(self):
        self._prox_ev = None
        self._rnd = None
        self._tiempo = None

    def es_tu_nombre(self, cadena):
        if self._nombre == cadena:
            return True
        return False

    def es_prox_ev_none(self):
        if self._prox_ev is None:
            return True
        return False

    @abstractmethod
    def crear_vector(self):
        pass
