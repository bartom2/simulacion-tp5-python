from objetos.Evento import Evento


class ComienzoJornadaLaboral(Evento):
    def __init__(self):
        super.__init__("Comienzo Jornada Laboral")
        self.__prox_ev = 0

    def calcular_prox_ev(self, reloj):
        self.__prox_ev = reloj + 0.01
