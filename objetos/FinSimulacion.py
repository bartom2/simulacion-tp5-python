from objetos.Evento import Evento


class FinSimulacion(Evento):
    def __init__(self):
        super.__init__("Fin Simulacion")

    def calcular_prox_ev(self, reloj):
        self._prox_ev = reloj + 0.01
