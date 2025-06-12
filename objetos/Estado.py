
class Estado():
    def __init__(self, nombre, categoria):
        self._nombre = nombre
        self._categoria = categoria

    def sos_este(self, estado):
        if self == estado:
            return True
        return False

    def sos_categoria(self, cadena):
        if self._categoria == cadena:
            return True
        else:
            return False

    def get_nombre(self):
        return self._nombre
