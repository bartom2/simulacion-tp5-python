from Evento.py import Evento
from random import random


class LlegadaCliente(Evento):
    def __init__():
        super.__init__("Llegada Cliente")

    def calcular_prox_ev(self, reloj):
        rnd = random.random()
        self.__prox_ev = reloj + 2 + (12-2) * rnd
