from Evento.py import Evento
from random import random


class LlegadaCliente(Evento):
    def __init__():
        super.__init__("Llegada Cliente")

    def calcular_prox_ev(self, reloj, a, b):
        # añadi a y b porque tienen que ser parametros cargados por el usuario.
        rnd = random.random()
        self.__prox_ev = reloj + a + (b-a) * rnd
