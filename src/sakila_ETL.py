from sqlalchemy import create_engine, text
from config import *
import pandas as pd
import os

def conection_bd():
    """Establece el motor de conexión (Engine)"""
    # Usamos pymysql para mayor compatibilidad con MariaDB
    url_db = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(url_db)
    return engine

def test_connection():
    """Probar la conexión a la base de datos"""
    engine = conection_bd()
    try:
        with engine.connect() as connection:
            print("✅ Conexión exitosa a Sakila.")
            result = connection.execute(text("SELECT * FROM film LIMIT 1;"))
            print(result.fetchone())
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")

def get_data_list_from_join():
    """Obtener datos y generar múltiples CSV"""
    engine = conection_bd()
    
    queries = [
        {
            "name": "DataFrame1",
            "query": """
                SELECT 
                    c.customer_id, LOWER(c.first_name) AS first_name, LOWER(c.last_name) AS last_name,
                    LOWER(c.email) AS email, LOWER(ci.city) AS city, LOWER(co.country) AS country,
                    r.rental_id, r.rental_date, r.return_date,
                    DATEDIFF(r.return_date, r.rental_date) AS rental_duration_days,
                    p.payment_id, p.amount, p.payment_date
                FROM customer c
                JOIN address a ON c.address_id = a.address_id
                JOIN city ci ON a.city_id = ci.city_id
                JOIN country co ON ci.country_id = co.country_id
                JOIN rental r ON c.customer_id = r.customer_id
                JOIN payment p ON r.rental_id = p.rental_id
                WHERE r.rental_id IS NOT NULL AND p.amount > 0 AND r.return_date IS NOT NULL;
            """
        },
        {
            "name": "DataFrame2",
            "query": """
                SELECT 
                    LOWER(TRIM(f.title)) AS title, 
                    LOWER(TRIM(c.name)) AS category, 
                    LOWER(TRIM(l.name)) AS language,
                    f.length,
                    CASE WHEN f.length >= 120 THEN 1 ELSE 0 END AS is_long_film
                FROM film f
                JOIN film_category fc ON f.film_id = fc.film_id
                JOIN category c ON fc.category_id = c.category_id
                JOIN language l ON f.language_id = l.language_id;
            """
        },
        {
            "name": "DataFrame3",
            "query": """
                SELECT 
                    f.film_id, f.title, a.actor_id,
                    CONCAT(LOWER(TRIM(a.first_name)), ' ', LOWER(TRIM(a.last_name))) AS actor_full_name,
                    (SELECT COUNT(*) FROM film_actor fa2 WHERE fa2.film_id = f.film_id) AS num_actors_per_film,
                    (SELECT COUNT(*) FROM film_actor fa3 WHERE fa3.actor_id = a.actor_id) AS num_films_per_actor
                FROM film f
                JOIN film_actor fa ON f.film_id = fa.film_id
                JOIN actor a ON fa.actor_id = a.actor_id;
            """
        }
    ]

    # Configuración de rutas
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIR = os.path.dirname(BASE_DIR)
    DATA_DIR = os.path.join(PARENT_DIR, "output")
    os.makedirs(DATA_DIR, exist_ok=True)

    # Abrimos la conexión UNA SOLA VEZ para todas las consultas
    try:
        with engine.connect() as connection:
            for query_info in queries:
                result = connection.execute(text(query_info["query"]))
                rows = result.fetchall()
                
                # Crear DataFrame
                df = pd.DataFrame(rows, columns=result.keys())

                # Guardar CSV
                file_path = os.path.join(DATA_DIR, f"{query_info['name']}.csv")
                df.to_csv(file_path, index=False, encoding='utf-8')
                print(f"✅ {query_info['name']} guardado en: {file_path} | Registros: {len(df)}")
                
    except Exception as e:
        print(f"❌ Error durante el proceso ETL: {e}")