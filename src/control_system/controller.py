"""
controller.py
Define el controlador (PID o proporcional).
"""

import control as ctrl


def create_controller(Kp=1.0, Ki=0.0, Kd=0.0):
    """
    Crea un controlador PID en el dominio de Laplace.

    Parameters
    ----------
    Kp : float, optional
        Ganancia proporcional. Default = 1.0
    Ki : float, optional
        Ganancia integral. Default = 0.0
    Kd : float, optional
        Ganancia derivativa. Default = 0.0

    Returns
    -------
    control.TransferFunction
        Controlador C(s) = Kp + Ki/s + Kd*s.
    """
    C = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
    return C