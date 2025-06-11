
class Masajista():
    def __init__(self, nombre, estado):
        self._nombre = nombre
        self._estado = estado

    def set_estado(self, estado):
        self._estado = estado

    def estas(self, estado):
        return self._estado.sos_este(estado)

    def get_nombre_estado(self):
        return self._estado.get_nombre()
