
class Masajista():
    def __init__(self, nombre, estado):
        self.__nombre = nombre
        self.__estado = estado

    def setEstado(self, estado):
        self.__estado = estado

    def estas(self, cadena):
        return self.__estado.sosEste(cadena)
