from objetos.VectorEstado import VectorEstado


class Simulador():
    def __init__(self):
        self.__func_tension, self.__iteraciones_runge_kutta = self.obtener_func_tension()

    def simular(self, x, i, j, func_tension):
        vector_estado = VectorEstado(self.__func_tension, x, j, i)

        max_cola_clientes = 0
        vectores_guardados = []

        while not self.__vector_estado.finalizo:
            self.__vector_estado.simular()

            if self.__vector_estado.guardar(j) and len(self.__vectores_guardados) < i:
                self.__vectores_guardados.append(self.__vector_estado)

                if self.__vector_estado.cola_es_mayor(self.__max_cant_clientes):
                    max_cola_clientes = self.__vector_estado.get_longitud_cola()

        return vectores_guardados, max_cola_clientes

    @staticmethod
    def obtener_func_tension():
        x1 = 0
        y1 = 0
        h = 0.01
        k1, k2, k3, k4, = None
        xn1, yn, yn1 = None
        func_tension = {}
        vec_iteraciones = []
        func_tension[x1] = y1
        lim = 10

        while x1 <= lim:
            k1 = h * (2*((y1 + 0.5)**2) + 50)

            y2 = y1 + k1/2
            k2 = h * (2*((y2 + 0.5)**2) + 50)

            y3 = y1 + k2/2
            k3 = h * (2*((y3 + 0.5)**2) + 50)

            y4 = y1 + k3
            k4 = h * (2*((y4 + 0.5)**2) + 50)

            yn1 = y1 + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
            xn1 = x1 + h
            func_tension[xn1] = yn1
            vec_iteraciones.append(
                {"x1": x1, "y1": y1, "k1": k1, "k2": k2, "k3": k3,
                 "k4": k4, "xn1": xn1, "yn1": yn1})

            x1 = xn1
            y1 = yn1
       return func_tension, vec_iteraciones

