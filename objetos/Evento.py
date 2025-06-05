from abc import ABC, abstractmethod


class Evento(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__prox_ev = None

    @abstractmethod
    def calcular_prox_ev(self, reloj):
        pass

    def get_nombre(self):
        return self.__nombre

    def get_prox_ev(self):
        return self.__prox_ev

    def set_prox_ev_none(self):
        self.__prox_ev = None

    def es_tu_nombre(self, cadena):
        if self.__nombre == cadena:
            return True
        return False

    def es_prox_ev_none(self):
        if self.__prox_ev is None:
            return True
        return False
