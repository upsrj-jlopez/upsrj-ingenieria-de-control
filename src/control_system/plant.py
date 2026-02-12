"""
plant.py
Define funciones de transferencia genéricas para el laboratorio.
"""

import control as ctrl


def first_order(a=1.0):
    """
    Genera una función de transferencia de primer orden:
    F(s) = 1 / (s + a)

    Parameters
    ----------
    a : float
        Constante del denominador.

    Returns
    -------
    control.TransferFunction
        Función de transferencia de primer orden.
    """
    num = [1]
    den = [1, a]
    return ctrl.TransferFunction(num, den)

def rc_feedback(R=1.0, C=1.0, Rf=1.0):
    """
    Función de transferencia de un circuito RC con realimentación resistiva R/Rf.
    F(s) = 1 / (RCs + 1 + (R/Rf))

    .. image:: ../../doc/img/rc.png
       :alt: Circuito RC con realimentación
       :align: center

    Parameters
    ----------
    R : float
        Resistencia principal (ohmios).
    C : float
        Capacitancia (faradios).
    Rf : float
        Resistencia de realimentación (ohmios).

    Returns
    -------
    control.TransferFunction
        Función de transferencia del circuito RC con realimentación.
    """
    import control as ctrl

    # TODO: declarar la función de transferencia
    num = [1]
    den = [1]

    return ctrl.TransferFunction(num, den)

def second_order(wn=1.0, zeta=0.5):
    """
    Genera una función de transferencia de segundo orden:
    F(s) = wn^2 / (s^2 + 2*zeta*wn*s + wn^2)

    Parameters
    ----------
    wn : float
        Frecuencia natural.
    zeta : float
        Factor de amortiguamiento.

    Returns
    -------
    control.TransferFunction
        Función de transferencia de segundo orden.
    """
    num = [wn**2]
    den = [1, 2*zeta*wn, wn**2]
    return ctrl.TransferFunction(num, den)