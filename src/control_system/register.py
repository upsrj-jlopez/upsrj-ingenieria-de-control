"""
register.py
Genera un archivo de registro de datos definidos por el usuario.
"""

import os
import pandas as pd
from config import OUT_DIR

REGISTER_FILE = os.path.join(OUT_DIR, "register.csv")

def init_register() -> None:
    """
    Inicializa el archivo register.csv con encabezados
    para el modelo térmico del invernadero.
    """
    if os.path.isfile(REGISTER_FILE) and os.path.exists(REGISTER_FILE):
        os.remove(REGISTER_FILE)
        
    df = pd.DataFrame(columns=["tau", "alpha", "ts", "pole"])
    df.to_csv(REGISTER_FILE, index=False)


def add_entry(tau: float = 0, alpha: float = 0, ts: float = 0, pole: float = 0) -> None:
    """
    Agrega una nueva fila al archivo register.csv con los parámetros
    de la simulación térmica del invernadero. No acumula entradas:
    cada ejecución del programa debe llamar primero a init_register()
    para reiniciar el archivo.

    Parameters
    ----------
    tau : float
        Constante de tiempo térmica (segundos).
    alpha : float
        Factor de pérdidas adicionales (adimensional).
    ts : float
        Tiempo de establecimiento (segundos).
    pole : float
        Polo dominante del sistema.
    """
    new_row = {"tau": tau, "alpha": alpha, "ts": ts, "pole": pole}
    df = pd.DataFrame([new_row])
    df.to_csv(REGISTER_FILE, mode="a", header=False, index=False)
