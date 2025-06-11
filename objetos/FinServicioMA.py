from objetos.Evento import Evento
from random import random


class FinServicioMA(Evento):
    def __init__(self, a_tension, b_tension, vec_fun_demora):
        super().__init__("Fin Servicio M A")
        # Quiero hacer que la func_demora sea un diccionario donde le tiras el valor de la tension y te da la demora asociada
        self._func_demora = vec_fun_demora
        self._a = a_tension
        self._b = b_tension
        self._c = None

    def calcular_prox_ev(self, reloj):
        self._rnd = random()
        self._c = self._a + (self._b - self._a) * self._rnd
        self._tiempo = self._func_demora(min(self._func_demora.keys(),
                                             key=lambda k: abs(k - self._c)))
        self._prox_ev = reloj + self._tiempo

    def set_prox_ev_none(self):
        super.set_prox_ev_none()
        self._c = None

    def crear_vector(self):
        if self._prox_ev is None:
            return ["", "", "", ""]
        else:
            return [str(self._rnd), str(self._c), str(self._tiempo),
                    str(self._prox_ev)]
