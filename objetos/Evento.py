
class Evento():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.prox_ev = None

    def calcularProxEv(self):
        self.prox_ev = None
