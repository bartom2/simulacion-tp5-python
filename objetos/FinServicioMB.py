from objetos.Evento import Evento
from random import random


class FinServicioMB(Evento):
    def __init__(self):
        super().__init__("Fin Servicio M B")

    def calcular_prox_ev(self, reloj):
        self._rnd = random()
        self._tiempo = 12 + (18 - 12) * self._rnd
        self._prox_ev = reloj + self._tiempo

    def crear_vector(self):
        if self._prox_ev is None:
            return ["", "", ""]
        else:
            return [str(self._rnd), str(self._tiempo), str(self._prox_ev)]
