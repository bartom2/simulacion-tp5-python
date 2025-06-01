from Evento.py import Evento
from random import random


class LlegadaCliente(Evento):
    def __init__():
        super.__init__("LlegadaCliente")

    def calcularProxEv(self):
        rnd = random.random()
        self.__prox_ev = 2 + (12-2) * rnd
