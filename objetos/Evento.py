from abc import ABC, abstractmethod


class Evento(ABC):
    def __init__(self, nombre):
        self._nombre = nombre
        self._prox_ev = None
        self._rnd = None
        self._tiempo = None

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
