"""
utils.py
Funciones auxiliares para graficar resultados de simulación.
"""

import os
import re
import unicodedata
import matplotlib.pyplot as plt
from config import OUT_DIR

def normalize_filename(title: str) -> str:
    """
    Normaliza un título para usarlo como nombre de archivo.

    - Convierte a minúsculas.
    - Reemplaza espacios por guiones bajos.
    - Elimina acentos y caracteres diacríticos.
    - Corta el texto en el primer ':' si existe.

    Parameters
    ----------
    title : str
        Texto original del título.

    Returns
    -------
    str
        Nombre de archivo seguro y normalizado.
    """
    # Reemplazar espacios y cortar en ':'
    base = title.replace(' ', '_').split(':')[0].lower()

    # Normalizar a NFD (descompone letras con acento)
    nfkd = unicodedata.normalize('NFD', base)

    # Filtrar los caracteres que no sean marcas diacríticas
    no_accents = ''.join(
        c for c in nfkd if not unicodedata.combining(c)
    )

    # Eliminar caracteres inseguros: (),=., etc.
    safe = re.sub(r'[()\=\.\[\]\{\},;]', '', no_accents)

    # Opcional: reemplazar múltiples guiones bajos consecutivos por uno solo
    safe = re.sub(r'_+', '_', safe)

    return safe.strip('_')


def equation_to_latex(equation: str) -> str:
    """
    Convierte una ecuación en formato texto a una cadena
    con sintaxis LaTeX para usar en títulos de gráficas.

    - Detecta fracciones del tipo a/b o expresiones entre paréntesis.
    - Convierte a notación LaTeX con \\frac{}{}.
    - Encapsula todo en delimitadores $...$.

    Parameters
    ----------
    equation : str
        Ecuación en formato texto, por ejemplo:
        "F(s) = 1/(RCs + 1 + (R/Rf))"

    Returns
    -------
    str
        Cadena con sintaxis LaTeX, por ejemplo:
        r"$F(s) = \\frac{1}{RCs + 1 + \\frac{R}{R_f}}$"
    """

    # Reemplazar fracciones simples con regex
    # Patrón: (numerador)/(denominador)
    def frac_repl(match):
        num = match.group(1).strip()
        den = match.group(2).strip()
        return f"\\frac{{{num}}}{{{den}}}"

    # Detectar expresiones tipo (R/Rf), 1/(...)
    latex = re.sub(r"\(([^()/]+)\s*/\s*([^()/]+)\)", frac_repl, equation)

    # Detectar fracción principal tipo 1/(...)
    latex = re.sub(r"1/\((.+)\)", r"\\frac{1}{\1}", latex)

    # Encapsular en delimitadores de LaTeX
    return f"${latex}$"

def format_title(title: str) -> str:
    """
    Formatea un título para desplegarlo con ecuaciones LaTeX.

    - Corta el texto en el primer ':' si existe.
    - La parte antes de ':' queda igual.
    - La parte después se convierte a LaTeX.

    Parameters
    ----------
    title : str
        Texto original del título.

    Returns
    -------
    str
        Título formateado con LaTeX.
    """
    name, equation = title.split(':', 1)
    equation = equation_to_latex(equation.strip())
    return f"{name}: {equation}"

def step_response_plot(t, y, title="Respuesta al escalón"):
    """
    Grafica la respuesta temporal de un sistema al escalón unitario.

    Parameters
    ----------
    t : array_like
        Vector de tiempo.
    y : array_like
        Respuesta del sistema.
    title : str, optional
        Título de la gráfica. Default = "Respuesta al escalón".
    """
    fig = plt.figure(figsize=(8,6))
    plt.plot(t, y, label="Salida")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title(format_title(title))
    plt.grid(True)
    plt.legend()
    
    filename = os.path.join(OUT_DIR, f"{normalize_filename(title)}.png")
    plt.savefig(filename)
    print(f"Gráfica guardada en {filename}")
