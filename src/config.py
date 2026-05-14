# src/config.py

import os
from dotenv import load_dotenv
from pathlib import Path 

# Obtener la ruta raíz del proyecto (un nivel arriba de src/)
ROOT_DIR = Path(__file__).parent.parent

# Cargar variables de entorno desde .env en la raíz del proyecto
dotenv_path = ROOT_DIR / '.env'
load_dotenv(dotenv_path)
 
DB_USER = os.getenv("DB_USER", 'root')
DB_PASSWORD = os.getenv("DB_PASSWORD", '')
DB_HOST = os.getenv("DB_HOST", 'localhost')
DB_NAME = os.getenv("DB_NAME", 'sakila')
DB_PORT = os.getenv("DB_PORT", '3306')

# === CONFIGURACIÓN DE ARCHIVOS ===
EXCEL_FILE = os.getenv('EXCEL_FILE', 'Sakila_Dashboard.xlsx')
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', 'output')

# === CONFIGURACIÓN DE AUTOMATIZACIÓN ===
AUTO_OPEN_EXCEL = os.getenv('AUTO_OPEN_EXCEL', 'true').lower() == 'true'