
class Cliente():
    def __init__(self, hora_llegada, estado):
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
        for n in ("Atendido Por M A", "Atendido Por M B", "Atendido Por M Ap"):
            if estado.sosEste(n):
                self__tiempo_espera = hora - self.__hora_llegada
                continue

    def esperasteTreintaMin(self):
        if self.__tiempo_espera >= 30:
            return True
        return False
