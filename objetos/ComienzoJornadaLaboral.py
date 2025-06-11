from objetos.Evento import Evento


class ComienzoJornadaLaboral(Evento):
    def __init__(self):
        super().__init__("Comienzo Jornada Laboral")
        self._prox_ev = 0

    def calcular_prox_ev(self, reloj):
        self._tiempo = 24 * 60
        self._prox_ev = reloj + self._tiempo

    def crear_vector(self):
        if self._prox_ev is None:
            return ["", ""]
        else:
            return [str(self._tiempo), str(self._prox_ev)]
