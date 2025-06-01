
class Estado():
    def __init__(self, nombre):
        self.__nombre = nombre

    def sosEste(self, cadena):
        if self.__nombre == cadena:
            return True
        return False
