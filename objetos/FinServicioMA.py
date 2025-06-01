from Evento.py import Evento
from random import random


class FinServicioMA(Evento):
    def __init__(self, vec_fun_demora):
        super.__init__("FinServicioMA")
        # Quiero hacer que la func_demora sea un diccionario donde le tiras el valor de la tension y te da la demora asociada
        self.__func_demora = vec_fun_demora

    def calcularProxEv(self):
        rnd = random.random()
        c = 3 + (10 - 3) * rnd
        self.__prox_ev = self.__func_demora[c]
