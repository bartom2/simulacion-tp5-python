
from Evento.py import Evento
from random import random


class FinServicioMB(Evento):
    def __init__():
        super.__init__("FinServicioMB")

    def calcularProxEv(self):
        rnd = random.random()
        self.__prox_ev = 12 + (18 - 12) * rnd
