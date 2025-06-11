from random import random
from objetos.Evento import Evento


class LlegadaCliente(Evento):
    def __init__(self, a_llegada_cliente, b_llegada_cliente):
        super().__init__("Llegada Cliente")
        self._rnd2 = None
        self._cod_masajista = None
        self._a = a_llegada_cliente
        self._b = b_llegada_cliente

    def calcular_prox_ev(self, reloj):
        self._rnd = random()
        self._tiempo = self._a + (self._b - self._a) * self._rnd
        self._prox_ev = reloj + self._tiempo

    def asignar_masajista(self):
        self._rnd2 = random()
        if 0 <= self._rnd2 <= 0.44:
            self._cod_masajista = "M A"
        elif 0.45 <= self._rnd <= 0.84:
            self._cod_masajsta = "M B"
        else:
            self._cod_masajista = "M Ap"
        return self._cod_masajista

    def crear_vector(self):
        if self._prox_ev is None:
            return ["", "", "", "", ""]
        else:
            return [str(self._rnd), str(self._tiempo),
                    str(self._prox_ev), str(self._rnd2),
                    str(self._cod_masajista)
                    ]
