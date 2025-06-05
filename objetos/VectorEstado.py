from objetos.LlegadaCliente import LlegadaCliente
from objetos.FinServicioMA import FinServicioMA
from objetos.FinServicioMAp import FinServicioMAp
from objetos.FinServicioMB import FinServicioMB
from objetos.Estado import Estado
from objetos.Cliente import Cliente
from objetos.Masajista import Masajista
from objetos.FinJornadaLaboral import FinJornadaLaboral
from objetos.ComienzoJornadaLaboral import ComienzoJornadaLaboral
from objetos.FinSimulacion import FinSimulacion

# Hay que cambiar la implementación de los Clientes para que los objetos se
# reutilicen. Y que estos nos muevan de posición sino que solo se agregan
# clientes a la cola cuando cuando todos los demás se encuentran activos.

# El momento del calculo y el calculo de los proximos eventos de
# ComienzoJornadaLaboral, FinSimulacion y FinJornadaLaboral se
# deben cambiar según el profe, no se como


class VectorEstado():
    def __init__(self, func_tension, x, j, i):
        self.__reloj = 0
        self.__eventos = [ComienzoJornadaLaboral, FinJornadaLaboral,
                          LlegadaCliente, FinServicioMA(func_tension),
                          FinServicioMB, FinServicioMAp,
                          FinSimulacion]
        self.__estados_cliente, self.__estados_masajistas = self.inicializar_estados()
        self.__masajistas = self.inicializar_masajistas
        self.__precio_masajistas = {"M A": 3500, "M B": 3500, "M Ap": 1800}
        self.__clientes = []
        self.__x = x
        self.__cant_dias_simulados = 0
        self.__evento_actual = ""
        self.__acc_recaudacion = 0
        self.__cant_max_cola = 0

    def guardar(self, j):
        if self.__reloj >= j:
            return True
        return False

    def simular(self):
        if self.__cant_dias_simulados == self.__x:
            return
        evento = self.__eventos.pop(0)
        self.__reloj = evento.get_prox_ev()
        self.__evento_actual = evento.get_nombre()
        # Tengo que tomar en cuenta cuando un evento se cancela y cuando un
        # evento vuelve a necesitar calcular su tiempo
        if self.__evento_actual == "Comienzo Jornada Laboral":
            if self.__reloj != 0:
                self.__cant_dias_simulados += 1
            evento.set_prox_ev_none()
            llegada = self.encontrar("Llegada Cliente")
            llegada.calcular_prox_ev()
            fin_jornada = self.encontrar("Fin Jornada Laboral")
            fin_jornada.calcular_prox_ev(self.__reloj)
            self.add_ev_in_order(llegada)
            self.add_ev_in_order(fin_jornada)

        elif self.__evento_actual == "Fin Jornada Laboral":
            llegada = self.encontrar("Llegada Cliente")
            llegada.set_prox_ev_none()
            self.add_ev_in_order(llegada)

        elif self.__evento_actual == "Llegada Cliente":
            evento.calcular_prox_ev(self.__reloj)
            cod_masajista = self.cod_masajista_disponible()
            self.nuevo_cliente(cod_masajista, self.__reloj)

            if cod_masajista != "":
                self.__masajistas[cod_masajista].setEstado(
                    self.__estados_masajistas["O"])
                fin_servicio = self.encontrar(f"Fin Servicio {cod_masajista}")
                fin_servicio.calcular_prox_ev(self.__reloj)
                self.add_ev_in_order(fin_servicio)
            else:
                nuevo_cliente = Cliente(
                    self.__estados_cliente["C"], self.__reloj)

            self.__clientes.add(nuevo_cliente)

            if self.__cant_max_cola < len(self.__clientes):
                self.__cant_max_cola = len(self.__clientes)

        elif self.__evento_actual in ("Fin Servicio M A",
                                      "Fin Servicio M B", "Fin Servicio M Ap"):
            cod = self.__evento_actual[12:]
            self.cobrar_cliente(f"Atendido Por {cod}")
            if not self.llamar_sig_cliente(cod):
                self.__masajistas[cod].setEstado(
                    self.__estados_masajistas["L"])
                evento.set_prox_ev_none()
            else:
                evento.calcular_prox_ev(self.__reloj)

            if self.es_prox_ev_none("Llegada Cliente") and self.todos_masajistas_desocupados():
                if self.__cant_dias_simulados == self.__x:
                    fin_sim = self.encontrar("Fin Simulación")
                    fin_sim.calcular_prox_ev(self.__reloj)
                    self.add_ev_in_order(fin_sim)
                else:
                    comienzo = self.encontrar("Comienzo Jornada Laboral")
                    comienzo.calcular_prox_ev(self.__reloj)
                    self.add_ev_in_order(comienzo)

        else:
            self.__evento_actual = evento.get_nombre()

        # Tengo que chequear que esta linea de codigo quede bien
        self.add_ev_in_order(evento)

    @staticmethod
    def inicializar_estados():
        estados_cliente = {}
        estados_masajistas = {}

        for name, handler, categoria in [
            ("En Cola", "C", "Cola"),
            ("Atendido Por M A", "M A", "Atendido"),
            ("Atendido Por M B", "M B", "Atendido"),
            ("Atendido Por M Ap", "M Ap", "Atendido")
        ]:
            estado = Estado(name, categoria)
            estados_cliente[handler] = estado

        for name, handler, categoria in [
            ("Ocupado", "O", "Masajista"),
            ("Libre", "L", "Masajista")
        ]:
            estado = Estado(name, categoria)
            estados_masajistas[handler] = estado

        return estados_cliente, estados_masajistas

    @staticmethod
    def inicializar_masajistas():
        masajistas = {}

        for name, handler in [
            ("Masajita A", "M A"),
            ("Masajita B", "M B"),
            ("Masajista Ap", "M Ap")
        ]:
            masajista = Masajista(name)
            masajistas[handler] = masajista

        return masajistas

    def encontrar(self, cadena):
        for ev in self.__eventos:
            if ev.es_tu_nombre(cadena):
                self.__eventos.remove(ev)
                return ev

    def add_ev_in_order(self, evento):
        # add in order binario en función del valor de prox_ev
        if evento.get_prox_ev() is None:
            self.__eventos.append(evento)
            return

        izquierda = 0
        derecha = len(self.__eventos)

        while izquierda < derecha:
            medio = (izquierda + derecha) // 2
            medio_tiempo = self.__eventos[medio].get_prox_ev()

            if medio_tiempo is None:
                derecha = medio
            elif medio_tiempo < evento.get_prox_ev():
                izquierda = medio + 1
            else:
                derecha = medio

        self.__eventos.insert(izquierda, evento)

    def cod_masajista_disponible(self):
        for codigo in ["M A", "M B", "M Ap"]:
            if self.__masajistas[codigo].estas(self.__estados_masajistas["L"]):
                return codigo
        return ""

    def get_longitud_cola(self):
        return len(self.__clientes)

    def cola_es_mayor(self, n):
        if len(self.__clientes) > n:
            return True
        return False

    def nuevo_cliente(self, cod_masajista, hora):
        for c in self.__clientes:
            if c.esta_fuera_del_sistema():
                if cod_masajista == "":
                    c.reutilizar(self.__estados_cliente["C"], hora)
                else:
                    c.reutilizar(self.__estados_cliente[cod_masajista], hora)
                return
        if cod_masajista == "":
            nuevo_cliente = Cliente(self.__estados_cliente["C"], hora)
        else:
            nuevo_cliente = Cliente(
                self.__estados_cliente[cod_masajista], hora)

        self.__clientes.add(nuevo_cliente)

    # Aca voy a tener el estado literal del cliente
    def cobrar_cliente(self, codigo_masajista):
        acc_gasto = 0
        for c in self.__clientes:
            if c.estas(self.__estados_cliente[codigo_masajista]):
                if c.tiempo_espera_mayor_treinta():
                    acc_gasto += 1500

                acc_gasto += self.__precio_masajistas[codigo_masajista]
                self.__acc_recaudacion += acc_gasto
                self.__clientes.remove(c)
                break

    def llamar_sig_cliente(self, codigo_masajista):
        for c in self.__clientes:
            if c.estas(self.__estados_cliente["C"]):
                c.setEstado(
                    self.__estados_cliente[codigo_masajista], self.__reloj)
                return True
        return False

    def es_prox_ev_none(self, nombre_ev):
        for ev in self.__eventos:
            if ev.es_tu_nombre(nombre_ev):
                return ev.es_prox_ev_none()

    def todos_masajistas_desocupados(self):
        for codigo in ["M A", "M B", "M Ap"]:
            if self.__masajistas[codigo].estas(self.__estados_masajistas["O"]):
                return False
        return True

    def guardar(self, j):
        if self.__reloj >= j:
            return True
        return False
