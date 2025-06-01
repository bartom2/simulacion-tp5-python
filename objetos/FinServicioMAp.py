from Evento.py import Evento
from random import random


class FinServicioMAp(Evento):
    def __init__():
        super.__init__("FinServicioMAp")

    def calcularProxEv(self):
        rnd = random.random()
        self.__prox_ev = 20 + (30 - 20) * rnd
