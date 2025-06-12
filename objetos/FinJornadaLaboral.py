from objetos.Evento import Evento


class FinJornadaLaboral(Evento):
    def __init__(self):
        super().__init__("Fin Jornada Laboral")

    def calcular_prox_ev(self, reloj):
        if reloj == 0:
            self._tiempo = 8 * 60
        else:
            self._tiempo = 24 * 60

        self._prox_ev = reloj + self._tiempo

    def crear_vector(self):
        if self._prox_ev is None:
            return ["", ""]
        else:
            return [str(self._tiempo), str(self._prox_ev)]
