from Evento.py import Evento
from random import random


class FinServicioMAp(Evento):
    def __init__():
        super.__init__("Fin Servicio M Ap")

    def calcular_prox_ev(self, reloj):
        rnd = random.random()
        self.__prox_ev = reloj + 20 + (30 - 20) * rnd
