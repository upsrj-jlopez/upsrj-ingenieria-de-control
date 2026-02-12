# ============================================================
# Politécnica de Santa Rosa
#
# Materia: Ingeniería de control
# Profesor: Jesús Salvador López Ortega
# Archivo: main.py
# Descripción: Punto de entrada del laboratorio de control.
#              Permite a los alumnos experimentar con distintas
#              funciones de transferencia y visualizar sus respuestas.
# ============================================================

import sys
import os
import config
from logger import set_logger, get_logger, plogger
from logging import ERROR, INFO
from control_system.plant import first_order, rc_feedback
from control_system.simulation import simulate_system
from control_system.register import init_register, add_entry

config.init_dirs()

# Configuración del logger
set_logger(file_path=__file__, level=INFO)
logger = get_logger(__name__)


def main():
    """
    Función principal del programa.
    Los alumnos pueden modificar aquí los parámetros de las funciones
    de transferencia para observar diferentes comportamientos.
    """
    try:
        logger.info("Iniciando laboratorio de funciones de transferencia...")
        plogger("Simulando distintas respuestas al escalón...")

        # TODO:
        # 1. Modificar la función rc_feedback() en control_system/plant.py
        #    para que construya la función de transferencia indicada:
        #    F(s) = 1 / (RCs + 1 + (R/Rf))
        #
        # 2. Calcular los valores de los parámetros R, C y Rf que definan
        #    el circuito. A partir de esos valores:
        #       - Determinar el polo dominante del sistema.
        #       - Estimar el polo para los siguientes tiempos de establecimiento (ts): 1s, 3s, 5s
        #       - Registrar todos estos datos (R, C, Rf, ts, pole) en
        #         register.csv mediante add_entry().
        #
        G = rc_feedback()
        simulate_system(G, "Circuito RC con retroalimentación: F(s) = 1/(RCs + 1 + (R/Rf))")

        init_register()
        add_entry()
        
    except OSError as e:
        plogger(f"OSError [{e.errno}]: {os.strerror(e.errno)}", level=ERROR)
        return os.EX_SOFTWARE

    except Exception:
        logger.exception("Error inesperado durante la ejecución")
        return os.EX_SOFTWARE

    logger.info("Programa finalizado correctamente.")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())