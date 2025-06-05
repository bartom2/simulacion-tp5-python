
class Masajista():
    def __init__(self, nombre, estado):
        self.__nombre = nombre
        self.__estado = estado

    def setEstado(self, estado):
        self.__estado = estado

    def estas(self, estado):
        return self.__estado.sosEste(estado)
