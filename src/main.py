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
from control_system.plant import greenhouse_temp
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
        # 1. Declara la función greenhouse_temp() en plant.py para construir la función de transferencia:
        #       F(s)= 1 / ((tau * s) + 1 + alpha)
        # 2. Calcular tau  a partir de la masa de aire, calor específico y coeficiente de pérdidas del 
        #    invernadero de acrílico que diseñaron.
        # 3. Proponer alpha  según el nivel de ventilación o fugas de su proyecto.
        # 4. Determinar el polo dominante y estimar los tiempos de establecimiento para t_s=300s, 600s, 900s, 1200s, 1500s.
        # 5. Registrar todos estos datos (tau ,alpha ,t_s,p) en register.csv.

        G = greenhouse_temp()
        simulate_system(G, "Modelo térmico de invernadero: F(s) = 1/(tau*s + 1 + alpha)")

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