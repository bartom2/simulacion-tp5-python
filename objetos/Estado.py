
class Estado():
    def __init__(self, nombre, categoria):
        self.__nombre = nombre
        self.__categoria = categoria

    def sosEste(self, estado):
        if self == estado:
            return True
        return False

    def sosCategoria(self, cadena):
        if self.__categoria == cadena:
            return True
        return False
