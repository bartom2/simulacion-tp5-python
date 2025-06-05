from PyQt5.QtWidgets import (
    QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QStackedWidget,
    QTableWidget, QTableWidgetItem, QWidget, QHeaderView,
    QComboBox
)
from PyQt5.QtCore import Qt

from ..core.rungekutta import obtener_func_tension
from ..core.simulador import simular

from .PaginaBase import PaginaBase


class PaginaResultados(PaginaBase):
    def __init__(
        self,
        callback_volver,
        callback_cerrar,
        x,
        j,
        i
    ):
        super().__init__("Resultados", callback_volver, callback_cerrar)
        self.boton_extra.hide()
        self.x = x
        self.j = j
        self.i = i
        self.func_tension = obtener_func_tension()

        self.agregar_widget(
            QLabel(f"<h2>Simulación de {self.x} días de Centro de Masajes Urbanos</h2>"))
        self.stack = QStackedWidget()
        self.stack.addWidget(self._widget_vectores())
        self.stack.addWidget(self._widget_runge_kutta())

        # Botones de navegación de vistas
        botones = QHBoxLayout()
        for txt, handler in [
            ("Vectores Estado", self.mostrar_vectores),
            ("Runge Kutta", self.mostrar_runge_kutta)
        ]:
            btn = QPushButton(txt)
            btn.clicked.connect(handler)
            botones.addWidget(btn)
        self.contenedor.addLayout(botones)

        # Navegación interna de serie
        self._crear_controles_serie()
        self.contenedor.addWidget(self.stack)

    def _widget_runge_kutta(self):
        runge_kutta = None
        return runge_kutta

    def _widget_vectores(self):
        contenedor = QWidget()
        layout = QVBoxLayout(contenedor)
        # Generar datos de tabla
        vectores_estado, max_clientes_en_intervalo = frecuencias_observadas(
            self.datos, self.intervalos)
        # extraer sólo límites para FE
        limites = [(li, ls) for (li, ls, fo) in datos_interv]

        # Crear tabla con 5 columnas
        tabla = QTableWidget(len(datos_interv), 5)
        tabla.setHorizontalHeaderLabels(
            ["Intervalo N°", "Límite Inf.", "Límite Sup.", "FO", "FE"]
        )
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Calcular FE según distribución
        total = len(self.datos)
        if self.distribucion == "Uniforme":
            params = (self.param_A, self.param_B)
        elif self.distribucion == "Exponencial Negativa":
            params = (self.param_lmd,)
        else:  # "Normal"
            params = (self.param_media, self.param_desv)
        fe_list = frecuencias_esperadas(
            limites, total, self.distribucion, params)

        # Poblar Tabla
        for i, (li, ls, fo) in enumerate(datos_interv):
            valores = [
                i + 1,
                f"{li:.4f}",
                f"{ls:.4f}",
                fo,
                f"{fe_list[i]:.4f}",
            ]
            for j, v in enumerate(valores):
                item = QTableWidgetItem(str(v))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                tabla.setItem(i, j, item)
        layout.addWidget(tabla)

        # Crear Tabla de chi2
        layout.addLayout(self._crear_seccion_chi2())

        return contenedor

    # Vistas
    def mostrar_vectores(self):
        self.stack.setCurrentIndex(0)
        self.nav.hide()

    def mostrar_runge_kutta(self):
        self.stack.setCurrentIndex(1)
        self.nav.hide()
