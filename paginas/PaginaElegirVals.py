from PyQt5.QtWidgets import QLabel, QDoubleSpinBox, QSpinBox
from .PaginaBase import PaginaBase


class PaginaElegirVals(PaginaBase):
    def __init__(self, cantidad, intervalos, callback_generado, callback_volver, callback_cerrar):
        super().__init__(callback_volver, callback_cerrar)

        self.entrada_tiempo_sim = QDoubleSpinBox()
        self.entrada_tiempo_sim.setDecimals(2)
        self.entrada_tiempo_sim.setSingleStep(0.01)
        self.entrada_tiempo_sim.setValue(0)
        self.entrada_tiempo_sim.setMinimum(0)

        self.entrada_j = QDoubleSpinBox()
        self.entrada_j.setDecimals(2)
        self.entrada_j.setSingleStep(0.01)
        self.entrada_j.setValue(0)
        self.entrada_j.setMinimum(0)

        self.entrada_i = QSpinBox()
        self.entrada_i.setValue(0)
        self.entrada_i.setMinimum(1)
        # Corroborar si es correcto poner este limite en el rango para la desv estandar

        self.set_boton_extra_texto("Simular")
        self.conectar_boton_extra(self.simular)

        self.agregar_widget(QLabel("Ingrese el Tiempo de Simualcion (hs): "))
        self.agregar_widget(self.entrada_tiempo_sim)

        self.agregar_widget(QLabel(
            "Ingrese la hora j a partir de la cual se mostrarán los vectores de estado (hs):"))
        self.agregar_widget(self.entrada_j)

        self.agregar_widget(QLabel(
            "Ingrese la cantidad i de vectores de estado que se  muestren a partir de esa hora:"))
        self.agregar_widget(self.entrada_j)

    def simular(self):
        tiempo_sim = self.entrada_tiempo_sim.value()
        j = self.entrada_j.value()
        i = self.entrada_i.value()
        self.callback(tiempo_sim, j, i)
