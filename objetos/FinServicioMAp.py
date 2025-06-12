from objetos.Evento import Evento
from random import random


class FinServicioMAp(Evento):
    def __init__(self):
        super().__init__("Fin Servicio M Ap")

    def calcular_prox_ev(self, reloj):
        self._rnd = round(random(), 4)
        self._tiempo = round(20 + (30 - 20) * self._rnd, 4)
        self._prox_ev = round(reloj + self._tiempo, 4)

    def crear_vector(self):
        if self._prox_ev is None:
            return ["", "", ""]
        else:
            return [str(self._rnd), str(self._tiempo), str(self._prox_ev)]
