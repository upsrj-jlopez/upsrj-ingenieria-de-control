"""
simulation.py
Simula la respuesta de distintas funciones de transferencia.
"""

import control as ctrl
from control_system.utils import step_response_plot


def simulate_system(system, title="Respuesta al escalón"):
    """
    Simula la respuesta al escalón de un sistema dado.

    Parameters
    ----------
    system : control.TransferFunction
        Función de transferencia a simular.
    title : str, optional
        Título de la gráfica.
    """
    t, y = ctrl.step_response(system)
    step_response_plot(t, y, title)