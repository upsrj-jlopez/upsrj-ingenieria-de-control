import os 
import shutil

BUILD_DIR = 'build'
LOG_DIR   = os.path.join(BUILD_DIR, 'log')
OUT_DIR   = os.path.join(BUILD_DIR, 'out')

def init_dirs():

    if os.path.isdir(LOG_DIR):
        shutil.rmtree(LOG_DIR)
    if os.path.isdir(OUT_DIR):
        shutil.rmtree(OUT_DIR)

    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)

def get_log_file(file_path: str) -> str:
    base = os.path.basename(file_path)      
    name, _ = os.path.splitext(base)        
    return os.path.join(LOG_DIR, f"{name}.log")

