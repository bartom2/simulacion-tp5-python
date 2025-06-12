from objetos.VectorEstado import VectorEstado


class Simulador():
    def __init__(self, x, a_dc, b_dc, c_dc):
        self._func_tension, self._iteraciones_runge_kutta = self.obtener_func_tension(
            x, a_dc, b_dc, c_dc)
        self._cant_iteraciones = 0
        self._cant_dias_a_simular = None

    def simular(self, dias, j, i, a_c, b_c, a_llegada_cliente, b_llegada_cliente):
        self._vector_estado = VectorEstado(
            self._func_tension, dias, j, i, a_c, b_c, a_llegada_cliente, b_llegada_cliente)

        self._cant_dias_a_simular = dias

        vectores_guardados = []

        while not self._vector_estado.finalizo() and self._cant_iteraciones < 100000:
            self._vector_estado.simular()
            self._cant_iteraciones += 1

            if self._vector_estado.guardar(j) and len(vectores_guardados) < i:
                vectores_guardados.append(self._vector_estado.crear_vector())

        max_cola_clientes = self._vector_estado.determinar_cant_clientes_vecs()
        reporte = self._vector_estado.crear_reporte()

        return vectores_guardados, max_cola_clientes, reporte

    @staticmethod
    def obtener_func_tension(x, a, b, c):
        # x creo que es la equivalencia en minutos para cada uno de los valores
        # La func_tension es nivel de tension y da la cantidad de minutos
        x1 = 0
        y1 = 0
        h = 0.01
        k1 = k2 = k3 = k4 = None
        xn1 = yn = yn1 = None
        func_tension = {}
        vec_iteraciones = []
        func_tension[y1] = x1
        lim = 10

        while y1 <= lim:
            k1 = h * (a*((y1 + b)**2) + c)

            y2 = y1 + k1/2
            k2 = h * (a*((y2 + b)**2) + c)

            y3 = y1 + k2/2
            k3 = h * (a*((y3 + b)**2) + c)

            y4 = y1 + k3
            k4 = h * (a*((y4 + b)**2) + c)

            yn1 = y1 + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
            xn1 = x1 + h
            func_tension[yn1] = xn1 / x
            vec_iteraciones.append(
                {"x1": x1, "y1": y1, "k1": k1, "k2": k2, "k3": k3,
                 "k4": k4, "xn1": xn1, "yn1": yn1})

            x1 = xn1
            y1 = yn1
        return func_tension, vec_iteraciones

    def get_iteraciones_runge_kutta(self):
        return self._iteraciones_runge_kutta

    def cuanto_se_simulo(self):
        texto = ""
        if self._cant_dias_a_simular is None:
            texto = "Todavía no se ha simulado."
        elif self._cant_iteraciones < 100000:
            texto = f"Se simuló exitosamente los {
                self._cant_dias_a_simular} dias."
        else:
            texto = f"Se intentó simular {
                self._cant_dias_a_simular} días pero se llegó al tope de 100000 iteraciones."

        return texto
