
from Evento.py import Evento
from random import random


class FinServicioMB(Evento):
    def __init__():
        super.__init__("Fin Servicio M B")

    def calcular_prox_ev(self, reloj):
        rnd = random.random()
        self.__prox_ev = reloj + 12 + (18 - 12) * rnd
