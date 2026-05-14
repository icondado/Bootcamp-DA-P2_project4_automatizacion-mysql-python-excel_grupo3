# 📊 Proyecto 4 - Automatización sakila → Python → Excel
## Sistema de Automatización y Análisis de Datos con Python, SQL y Excel

Proyecto de automatización de datos orientado al análisis, transformación y visualización de información mediante procesos ETL desarrollados en Python.
El sistema conecta con una base de datos relacional, ejecuta consultas SQL, procesa los datos con Pandas y genera archivos CSV preparados para su análisis en Excel mediante dashboards y tablas dinámicas.

✨ Arquitectura ETL ligera · Automatización con Python · Visualización en Excel

---

## 👥 Autores - Grupo 3
* **Rita Isabel Romero Ruiz**
* **Marco Ohimai Imouokhome**
* **Irene Condado Alcantarilla**

---

# 📖 Documentación
README.md (este archivo) - Guía completa del proyecto
Dashboard/README.md - Guía completa del Dashboard

---
# 🚀 Puesta en Marcha

## 1. Clonar el repositorio
```bash
git clone https://github.com/Bootcamp-DA-P2/automatizaci-n-mysql-python-excel_grupo3.git
```
Acceder a la carpeta del proyecto:
```cd automatizaci-n-mysql-python-excel_grupo3```

## 2. Instalar dependencias
```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar base de datos
# Edita el archivo .env con tus credenciales

# Ejecutar
python main.py
```


---

# 📁 Estructura del Proyecto

```txt
automatizaci-n-mysql-python-excel_grupo3/
│
├── main.py                    ⭐ EJECUTAR ESTE
│
├── src/                       📦 Código fuente
│   ├── __init__.py
│   ├── sakila_ETL.py          (extracción y transformación)
│   └── config.py              (configuración desde .env)
│
├── output/                    📂 Datos procesados
│   ├── DataFrame1.csv
│   ├── DataFrame2.csv
│   └── DataFrame3.csv
│
├── assets/   
│
├── dashboard/                 📊 Visualización
│   ├── Sakila_dashboard.xlsx
│   └── README.md
│
├── queries/                   🗄️ Consultas SQL
│   ├── DataFrame1.sql
│   ├── DataFrame2.sql
│   └── DataFrame3.sql
│
├── requirements.txt
├── .env                       🔒 Credenciales
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ CONFIGURACIÓN

## 1. Instalar Python y Base de Datos

### Requisitos:
    - Python 3.8 o superior

    - [MYSQL / POSTGRESQL / SQL SERVER]

    - Excel o Excel Online

## 2. Instalar dependencias
```bash
pip install -r requirements.txt
```
Ejemplo:
```bash
pip install pandas sqlalchemy openpyxl python-dotenv
```

## 3. Configurar conexión (.env)

Crea un archivo .env basado en .env.example con tus credenciales de acceso:
```
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=3306
DB_NAME=sakila

```

---
# 🎯 USO

Ejecutar el proceso completo:

```bash
python main.py
```

Esto hará:

* ✅ Extrae datos desde la base de datos
* ✅ Transforma y analiza datos con Pandas
* ✅ Genera archivos CSV automáticamente
* ✅ Actualiza la información del dashboard

---

# 📂 Archivos generados

| Archivo       | Descripción                |
| ------------- | -------------------------- |
| DataFrame1.csv | [Descripción del análisis] |
| DataFrame2.csv | [Descripción del análisis] |
| DataFrame3.csv | [Descripción del análisis] |

---

# 📊 Dashboard y Análisis Final
El análisis final se centraliza en el archivo Sakila_dashboard.xlsx. Para comprender el funcionamiento de los filtros, segmentadores y métricas visualizadas, consulta la Guía del Dashboard[dashboard\README.md].

---

# 📖 Metodología Scrum Adaptada

El equipo trabajó utilizando una metodología inspirada en Scrum, adaptada a un entorno académico y
colaborativo.
En lugar de reuniones diarias formales, el grupo se reunía cada vez que era necesario tomar decisiones
importantes o resolver complicaciones técnicas. Cuando surgían errores o dificultades, el trabajo se
realizaba de forma conjunta para encontrar soluciones y mantener el avance del proyecto.
## ⚙️ Organización del Equipo

👩 Rita Isabel Romero Ruiz
**Product Owner · Gestión del Proyecto y Visualización**
Responsable de:
- Crear el repositorio del proyecto.
- Tomar decisiones sobre tablas dinámicas y análisis visual.
- Diseñar y crear las tablas dinámicas en Excel.
- Participar en decisiones generales sobre la estructura del dashboard.
- Colaborar en tareas conjuntas del proyecto.

👨 Marco Ohimai Imouokhome
**Desarrollo de Datos y Dashboard**
Responsable de:
- Limpieza y preparación de tablas.
- Apoyo en la estructura y organización de datos.
- Creación del dashboard final en Excel.
- Participación en tareas técnicas compartidas.
- Resolución colaborativa de incidencias.

👩 Irene Condado Alcantarilla
**Desarrollo ETL y Automatización**
Responsable de:
- Desarrollo del archivo principal `main.py`.
- Automatización y ajustes en Python.
- Transformación de datos mediante Pandas.
- Generación de archivos CSV.
- Preparación de datos para su integración en Excel.
- Participación en mejoras y revisiones conjuntas.

## 🤝 Trabajo Colaborativo
Aunque cada integrante tenía responsabilidades principales, muchas partes del proyecto fuerondesarrolladas de forma conjunta.
El equipo colaboró especialmente en:
- Resolución de errores.
- Organización del flujo ETL.
- Ajustes del dashboard.
- Validación de resultados.
- Revisión de tablas y visualizaciones.
- Toma de decisiones técnicas.
- La comunicación constante y el apoyo mutuo permitieron avanzar de manera organizada y adaptarse alas necesidades de cada fase del proyecto.

## 🔄 Flujo de Trabajo Aplicado

1️⃣ Extracción de Datos
- Consultas SQL sobre la base de datos Sakila.
- Limpieza inicial de tablas.
- Preparación de información para el procesamiento.

---

2️⃣ Transformación y Automatización
- Procesamiento de datos mediante Python y Pandas.
- Automatización del flujo ETL.
- Generación automática de archivos CSV.
- Preparación de datos para Excel.

---

3️⃣ Visualización y Análisis
- Creación de tablas dinámicas.
- Diseño del dashboard interactivo.
- Implementación de KPIs y gráficos.
- Organización visual de métricas y tendencias.

---

## 📋 Organización de Tareas

| Área | Responsable Principal |
|---|---|
| Repositorio y decisiones visuales | Rita |
| Limpieza de tablas y dashboard | Marco |
| ETL, Python y CSV | Irene |
| Resolución de problemas y mejoras | Trabajo conjunto |


## 💡 Forma de Trabajo del Equipo
El proyecto se desarrolló mediante:
- Reuniones según necesidad.
- Colaboración constante.
- División flexible de tareas.
- Resolución conjunta de complicaciones técnicas.
- Participación colectiva en decisiones importantes.

Este enfoque permitió mantener una dinámica de trabajo organizada, eficiente y adaptable.

## 📊 Resultado Final
El equipo consiguió desarrollar:
- ✅ Un sistema ETL automatizado.
- ✅ Integración entre SQL, Python y Excel.
- ✅ Generación automática de archivos CSV.
- ✅ Un dashboard dinámico con métricas y visualizaciones.
- ✅ Un entorno organizado y documentado para futuras actualizaciones.

## 🚀 Conclusión
La metodología utilizada permitió combinar organización, colaboración y flexibilidad durante el
desarrollo del proyecto.
Gracias al trabajo conjunto y a la división equilibrada