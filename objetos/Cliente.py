
class Cliente():
    def __init__(self, estado, hora_llegada):
        self.__nombre = self.asignar_id()
        self.__estado = estado
        self.__hora_llegada = hora_llegada
        self.__tiempo_espera = 0

    def setEstado(self, estado, hora):
        self.calcular_tiempo_espera(estado, hora)
        self.__estado = estado

    def asignar_id():
        return 1

    def calcular_tiempo_espera(self, estado, hora):
        if estado.sosCategoria("Atendido"):
            self.__tiempo_espera = hora - self.__hora_llegada

    def estas(self, estado):
        if self.__estado.sosEste(estado):
            return True
        return False

    def tiempo_espera_mayor_treinta(self):
        if self.__tiempo_espera >= 30:
            return True
        return False
