#!/usr/bin/env python3
import subprocess
import os
import sys
import re
import pandas as pd
import numpy as np

# ANSI escape codes for colors
GREEN = "\033[92m"
RED   = "\033[91m"
BLUE  = "\033[34m"
RESET = "\033[0m"

# Paths
SRC_DIR   = "src"
FILENAME  = "main"
SCRIPT    = os.path.join(SRC_DIR, f"{FILENAME}.py")
BUILD_DIR = "build"
OUT_DIR   = os.path.join(BUILD_DIR, "out")
LOG_DIR   = os.path.join(BUILD_DIR, "log")
REGISTER  = os.path.join(OUT_DIR, "register.csv")
PLOTS     = os.path.join(OUT_DIR, "*.png")
LOG_PATH  = os.path.join(LOG_DIR, f"{FILENAME}.log")
VENV_PYTHON = os.path.join("venv", "bin", "python")

def run_cmd(cmd, cwd=None, input_data=None):
    """Run a shell command and return (exit_code, stdout, stderr)."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            shell=True,
            input=input_data,
            capture_output=True,
            text=True
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def run_main():
    """Ejecuta el script principal y valida que termine correctamente."""
    print(">>> Running main.py ...")
    code, out, err = run_cmd(f"{VENV_PYTHON} {SCRIPT}")
    if err:
        print(f"{RED}stderr:\n{err}{RESET}")
    assert code == 0, f"{RED}Program execution failed{RESET}"
    print(f"{GREEN}Program executed successfully{RESET}")

def test_script_exists():
    print(">>> Checking if Python script exists...")
    assert os.path.isfile(SCRIPT), f"{RED}Script not found at {SCRIPT}{RESET}"
    print(f"{GREEN}Script found: {SCRIPT}{RESET}")


def test_log_exists_and_content():
    print(">>> Checking if log file exists and has content...")
    assert os.path.isfile(LOG_PATH), f"{RED}Log file not found at {LOG_PATH}{RESET}"
    with open(LOG_PATH, "r") as f:
        content = f.read().strip()
    assert content, f"{RED}Log file is empty{RESET}"
    print(f"{GREEN}Log file OK{RESET}")
    print(f"{BLUE}Log content:\n{content}{RESET}")


def test_register_file():
    print(">>> Checking register.csv contents...")
    assert os.path.isfile(REGISTER), f"{RED}Register file not found at {REGISTER}{RESET}"
    df = pd.read_csv(REGISTER)
    assert len(df) == 3, f"{RED}Register should have 3 rows, found {len(df)}{RESET}"
    expected_cols = ["R", "C", "Rf", "ts", "pole"]
    assert all(col in df.columns for col in expected_cols), f"{RED}Missing columns in register.csv{RESET}"
    print(f"{GREEN}Register file OK with 3 entries{RESET}")
    print(f"{BLUE}Register content:\n{df}{RESET}")


def test_graphics_exist():
    print(">>> Checking if output graphics exist...")
    assert os.path.isdir(OUT_DIR), f"{RED}Output directory not found at {OUT_DIR}{RESET}"
    files = [f for f in os.listdir(OUT_DIR) if f.endswith(".png")]
    assert len(files) >= 3, f"{RED}Expected at least 3 graphs, found {len(files)}{RESET}"
    print(f"{GREEN}Found {len(files)} graphs in {OUT_DIR}{RESET}")
    print(f"{BLUE}Graphs:\n{files}{RESET}")


def test_register_values():
    print(">>> Checking register.csv numerical values...")
    df = pd.read_csv(REGISTER)

    # Validar que los ts sean exactamente 0.1, 0.2, 0.3
    ts_values = df["ts"].tolist()
    assert sorted(ts_values) == [0.1, 0.2, 0.3], f"{RED}Unexpected ts values: {ts_values}{RESET}"

    # Validar que los polos correspondan a la relación ts ≈ 4/|pole|
    for _, row in df.iterrows():
        ts = row["ts"]
        pole = row["pole"]
        expected_pole = -4 / ts
        assert np.isclose(pole, expected_pole, rtol=1e-2), (
            f"{RED}Pole mismatch for ts={ts}: expected {expected_pole}, got {pole}{RESET}"
        )

        # Validar que R, C y Rf sean realistas
        R, C, Rf = row["R"], row["C"], row["Rf"]

        # R debe ser positivo y mayor a 500 Ω (limitación de corriente 5V/10mA)
        assert R >= 500, f"{RED}R unrealistically small: {R} Ω{RESET}"

        # C debe ser positivo y en rango típico (>= 1e-9 F y <= 1 F)
        assert 1e-9 <= C <= 1, f"{RED}C unrealistic: {C} F{RESET}"

        # Rf debe ser positivo y no exageradamente grande (ej. <= 10 MΩ)
        assert 0 < Rf <= 1e7, f"{RED}Rf unrealistic: {Rf} Ω{RESET}"

    print(f"{GREEN}Register values OK (poles and parameters are realistic){RESET}")


if __name__ == "__main__":
    try:

        test_script_exists()
        run_main()
        test_log_exists_and_content()
        test_register_file()
        test_register_values()
        test_graphics_exist()
        
        print(f"\n{GREEN}All tests passed{RESET}")
    except AssertionError as e:
        print(f"{RED}Test failed: {e}{RESET}")
        sys.exit(1)
