from objetos.Evento import Evento


class FinJornadaLaboral(Evento):
    def __init__(self):
        super.__init__("Fin Jornada Laboral")

    def calcular_prox_ev(self, reloj):
        self.__prox_ev = reloj + 8 * 60
