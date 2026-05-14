# src/sakila_ETL.property
# Arquitectura: cada consulta SQL queris/*.sql
from sqlalchemy import create_engine, text
from pathlib import Path
from config import *
import pandas as pd
import os

# Carpeta de queries relativa a la raíz del proyecto
QUERIES_DIR = Path(__file__).parent.parent / 'queries'

# Mapeo: nombre_de_archivo_sql → nombre_de_archivo_csv
# Modelo estrella: 1 tabla de hechos + 3 dimensiones
CONSULTAS = {
    "DataFrame1.sql": "DataFrame1.csv",
    "DataFrame2.sql": "DataFrame2.csv",
    "DataFrame3.sql": "DataFrame3.csv",
}

def conection_bd():
    """Establece el motor de conexión (Engine)"""
    # Usamos pymysql para mayor compatibilidad con MariaDB
    url_db = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(url_db)
    return engine

def test_connection():
    """Probar la conexión a la base de datos"""
    try:
        engine = conection_bd()
        with engine.connect() as connection:
            print("✅ Conexión exitosa a Sakila.")
            result = connection.execute(text("SELECT * FROM film LIMIT 1;"))
            print(result.fetchone())
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")

def get_data_list_from_join():

    # Conectar BD
    try:
        engine = conection_bd()  
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")

    # Extraer datos
    
    print("Extrayendo datos de MySQL...")
    
    resultados = {}
    with engine.connect() as connection:
        for archivo_sql, archivo_csv in CONSULTAS.items():
            try:
                ruta_sql = QUERIES_DIR / archivo_sql
                query = ruta_sql.read_text(encoding='utf-8')
                df = pd.read_sql(query, engine)
                
                resultados[archivo_csv] = df
                print(f"  ✓ {archivo_sql} → {len(df)} filas")                
            except Exception as e:
                print(f"❌ Error durante el proceso ETL: {e}")
    
    # Guarda cada DataFrame como CSV en la carpeta output/
    print("Guardando archivos...")
    try:
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        for archivo_csv, df in resultados.items():
            df.to_csv(f'{OUTPUT_FOLDER}/{archivo_csv}', index=False)
            print(f"  ✓ {archivo_csv}")

        print(f"✓ Archivos guardados en carpeta '{OUTPUT_FOLDER}/'")
    except Exception as e:
        print(f"❌ Error durante el proceso de guardar archivos: {e}")

if __name__ == "__main__":
    get_data_list_from_join()