# main.py
# Ejecuta la automatización completa: 
# MySQL → Python → CSV → Excel

import sys
import os
from datetime import datetime
from pathlib import Path

# Agregar la carpeta src al path
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'src')
sys.path.append(src_path)

# Configuración
from src.config import (EXCEL_FILE, AUTO_OPEN_EXCEL, OUTPUT_FOLDER)

# Funciones ETL
from sakila_ETL import (test_connection, get_data_list_from_join)

def main():

    print("\n" + "=" * 50)
    print("AUTOMATIZACIÓN SAKILA")
    print("=" * 50)

    # Fecha y hora actual
    print(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # PASO 1: Verificar conexión MySQL
    print("\nVerificando conexión MySQL...\n")
    test_connection()

    # PASO 2: Ejecutar ETL
    print("\nProcesando datos...\n")

    try:
        get_data_list_from_join()
        print("Datos procesados correctamente")
    except Exception as e:
        print(f"\nError durante el ETL: {e}")
        return False

    # PASO 3: Abrir Excel automáticamente
    if AUTO_OPEN_EXCEL:
        print("\nAbriendo Excel...")
        excel_path = Path(__file__).parent / EXCEL_FILE
        if excel_path.exists():
            try:
                os.startfile(str(excel_path))
                print(f"Excel abierto: {EXCEL_FILE}")
            except Exception as e:
                print(f"No se pudo abrir Excel: {e}")
        else:
            print(f"Archivo no encontrado: {EXCEL_FILE}")

    # RESUMEN FINAL
    print("\n" + "=" * 50)
    print("PROCESO COMPLETADO")
    print("=" * 50)
    print(f"\nArchivos generados en '{OUTPUT_FOLDER}/'")

    return True

if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario")
    except Exception as e:
        print(f"\nError inesperado: {e}")
    finally:
        input("\nPresiona ENTER para salir...")
