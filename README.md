

---

```markdown
# PulseBoard – Dashboard de KPIs – Español / English

---

## 🇪🇸 Español

### Descripción

**PulseBoard** es un dashboard interactivo diseñado para equipos de ventas, marketing o producto que necesitan monitorizar el rendimiento del negocio en tiempo real. Combina la potencia de **Python**, **Streamlit** y **Plotly** con una base de datos robusta (PostgreSQL o SQLite) y ofrece funcionalidades avanzadas como autenticación de usuarios, alertas por correo electrónico, caché inteligente, tests unitarios y despliegue con Docker.

El nombre **PulseBoard** evoca un tablero que late al ritmo de los datos, reflejando la salud del negocio a través de indicadores clave (KPIs) como ingresos, número de pedidos, ticket promedio, clientes activos y más.

---

### Características principales

- ✅ **KPIs dinámicos** – Ingresos totales, pedidos, ticket promedio, clientes activos, variación respecto al periodo anterior.
- ✅ **Filtros avanzados** – Rango de fechas, categorías de productos y países.
- ✅ **Gráficos interactivos** – Evolución diaria, ventas por categoría, pedidos por país, top productos.
- ✅ **Caché inteligente** – `st.cache_data` con TTL configurable para reducir cargas a la base de datos.
- ✅ **Autenticación y roles** – Panel de administración para gestionar usuarios (crear/eliminar) con roles *admin* y *viewer*.
- ✅ **Alertas por correo** – Notificaciones automáticas cuando los KPIs caen por debajo de umbrales definidos.
- ✅ **Exportación de datos** – Descarga de los datos filtrados en CSV.
- ✅ **Tests unitarios** – Cobertura básica con `pytest`.
- ✅ **Despliegue con Docker** – `docker-compose` para levantar la aplicación y la base de datos PostgreSQL en contenedores.
- ✅ **Base de datos en la nube** – Soporte nativo para PostgreSQL y fácil adaptación a Snowflake u otros motores.

---

### Tecnologías utilizadas

| Tecnología | Propósito |
|------------|-----------|
| Python 3.10+ | Lenguaje principal |
| Streamlit | Framework para dashboards sin HTML/CSS/JS |
| Pandas | Manipulación y agregación de datos |
| Plotly | Gráficos interactivos |
| SQLAlchemy | ORM y conexión a bases de datos |
| PostgreSQL / SQLite | Almacenamiento de datos (PostgreSQL recomendado en producción) |
| Psycopg2 | Adaptador para PostgreSQL |
| Python-dotenv | Gestión de variables de entorno |
| Pytest | Tests unitarios |
| Docker & docker-compose | Contenedorización y orquestación |

---

### Estructura del proyecto

```
pulseboard/
├── app.py                     # Punto de entrada de Streamlit
├── config.py                  # Configuraciones (BD, email, umbrales)
├── database.py                # Conexión y consultas a BD
├── models.py                  # Definición de tablas con SQLAlchemy
├── kpis.py                    # Funciones de cálculo de KPIs
├── charts.py                  # Generación de gráficos con Plotly
├── auth.py                    # Autenticación y gestión de usuarios
├── notifications.py           # Envío de correos de alerta
├── tests/
│   ├── test_kpis.py
│   ├── test_database.py
│   └── conftest.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env                        # Variables de entorno (no subir a Git)
├── init.sql                    # (Opcional) Script de inicialización de BD
└── README.md
```

---

### Instalación y ejecución local

#### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/pulseboard.git
cd pulseboard
```

#### 2. Crear y activar entorno virtual

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
# o en Windows: venv\Scripts\activate
```

#### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

#### 4. Configurar variables de entorno

Copia el archivo `.env.example` (o crea uno nuevo) y completa tus credenciales:

```env
DB_TYPE=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_NAME=pulseboard
DB_USER=postgres
DB_PASSWORD=postgres

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tu_correo@gmail.com
SMTP_PASSWORD=tu_contraseña_de_aplicacion
ALERT_EMAIL=destinatario@ejemplo.com

REVENUE_THRESHOLD=10000
ORDERS_THRESHOLD=50
CACHE_TTL=300
```

#### 5. Inicializar la base de datos

Puedes usar el script `init.sql` para crear las tablas y cargar datos de prueba, o bien ejecutar el siguiente comando desde Python (si has definido `Base.metadata.create_all(engine)`):

```python
from database import get_engine
from models import Base
engine = get_engine()
Base.metadata.create_all(engine)
```

#### 6. Ejecutar la aplicación

```bash
streamlit run app.py
```

Accede a `http://localhost:8501` en tu navegador.

#### 7. Credenciales por defecto

- **Usuario:** `admin`
- **Contraseña:** `admin123`

---

### Despliegue con Docker (recomendado para producción)

1. Asegúrate de tener **Docker** y **docker-compose** instalados.

2. Configura tu archivo `.env` con los valores adecuados (el servicio `db` debe ser accesible desde el contenedor de la app, por lo que `DB_HOST` debe ser `db` – el nombre del servicio en el compose).

3. Construye y levanta los contenedores:

```bash
docker-compose up -d --build
```

4. Accede a `http://localhost:8501` para ver el dashboard.

5. Para detener los contenedores:

```bash
docker-compose down
```

Los datos de la base de datos se mantienen en un volumen Docker (`postgres_data`), por lo que sobreviven a reinicios.

---

### Ejecución de tests

```bash
pytest tests/
```

Los tests unitarios verifican el cálculo de KPIs y las consultas básicas a la base de datos (con una base de datos SQLite en memoria para pruebas).

---

### Personalización y extensión

- **Añadir nuevos KPIs**: Define nuevas funciones en `kpis.py` y agrégalas al dashboard en `app.py`.
- **Cambiar umbrales de alerta**: Modifica `REVENUE_THRESHOLD` y `ORDERS_THRESHOLD` en el archivo `.env`.
- **Conectar a Snowflake**: Instala `snowflake-sqlalchemy` y modifica la función `get_engine()` en `database.py` para usar la URL de Snowflake.
- **Agregar más gráficos**: Crea nuevas funciones en `charts.py` y colócalas en `app.py` con `st.plotly_chart()`.
- **Roles adicionales**: Extiende la lógica en `auth.py` para manejar permisos más granulares.

---

### Contribuciones y soporte

Este proyecto es un punto de partida sólido para equipos que desean implementar un dashboard de KPIs con Python. Si encuentras algún error o deseas proponer mejoras, no dudes en abrir un *issue* o enviar un *pull request*.

---

### Licencia

MIT – Libre para uso comercial y educativo.

---

## 🇬🇧 English

### Description

**PulseBoard** is an interactive dashboard designed for sales, marketing, or product teams that need to monitor business performance in real time. It combines the power of **Python**, **Streamlit** and **Plotly** with a robust database (PostgreSQL or SQLite) and offers advanced features such as user authentication, email alerts, intelligent caching, unit tests, and Docker deployment.

The name **PulseBoard** evokes a board that beats to the rhythm of data, reflecting the health of the business through key performance indicators (KPIs) like revenue, order count, average order value, active customers, and more.

---

### Key features

- ✅ **Dynamic KPIs** – Total revenue, orders, average ticket, active customers, variation vs. previous period.
- ✅ **Advanced filters** – Date range, product categories, and countries.
- ✅ **Interactive charts** – Daily evolution, sales by category, orders by country, top products.
- ✅ **Smart caching** – `st.cache_data` with configurable TTL to reduce database load.
- ✅ **Authentication and roles** – Admin panel to manage users (create/delete) with *admin* and *viewer* roles.
- ✅ **Email alerts** – Automatic notifications when KPIs fall below defined thresholds.
- ✅ **Data export** – Download filtered data as CSV.
- ✅ **Unit tests** – Basic coverage with `pytest`.
- ✅ **Docker deployment** – `docker-compose` to spin up the app and PostgreSQL database in containers.
- ✅ **Cloud database ready** – Native support for PostgreSQL and easy adaptation to Snowflake or other engines.

---

### Technology stack

| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Main language |
| Streamlit | Dashboard framework (no HTML/CSS/JS required) |
| Pandas | Data manipulation and aggregation |
| Plotly | Interactive charts |
| SQLAlchemy | ORM and database connectivity |
| PostgreSQL / SQLite | Data storage (PostgreSQL recommended for production) |
| Psycopg2 | PostgreSQL adapter |
| Python-dotenv | Environment variable management |
| Pytest | Unit testing |
| Docker & docker-compose | Containerization and orchestration |

---

### Project structure

```
pulseboard/
├── app.py                     # Streamlit entry point
├── config.py                  # Configurations (DB, email, thresholds)
├── database.py                # DB connection and queries
├── models.py                  # Table definitions with SQLAlchemy
├── kpis.py                    # KPI calculation functions
├── charts.py                  # Chart generation with Plotly
├── auth.py                    # Authentication and user management
├── notifications.py           # Alert email sending
├── tests/
│   ├── test_kpis.py
│   ├── test_database.py
│   └── conftest.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env                        # Environment variables (do not commit)
├── init.sql                    # (Optional) DB initialization script
└── README.md
```

---

### Local installation and execution

#### 1. Clone the repository

```bash
git clone https://github.com/your-username/pulseboard.git
cd pulseboard
```

#### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
# or on Windows: venv\Scripts\activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Set up environment variables

Copy the `.env.example` file (or create a new one) and fill in your credentials:

```env
DB_TYPE=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_NAME=pulseboard
DB_USER=postgres
DB_PASSWORD=postgres

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
ALERT_EMAIL=recipient@example.com

REVENUE_THRESHOLD=10000
ORDERS_THRESHOLD=50
CACHE_TTL=300
```

#### 5. Initialize the database

You can use the `init.sql` script to create tables and load test data, or run the following Python code (if you have `Base.metadata.create_all(engine)` defined):

```python
from database import get_engine
from models import Base
engine = get_engine()
Base.metadata.create_all(engine)
```

#### 6. Run the application

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

#### 7. Default credentials

- **Username:** `admin`
- **Password:** `admin123`

---

### Docker deployment (recommended for production)

1. Make sure you have **Docker** and **docker-compose** installed.

2. Configure your `.env` file with appropriate values (the `db` service must be reachable from the app container, so `DB_HOST` should be `db` – the service name in the compose file).

3. Build and start the containers:

```bash
docker-compose up -d --build
```

4. Access `http://localhost:8501` to see the dashboard.

5. To stop the containers:

```bash
docker-compose down
```

Database data is persisted in a Docker volume (`postgres_data`), so it survives restarts.

---

### Running tests

```bash
pytest tests/
```

Unit tests verify KPI calculations and basic database queries (using an in-memory SQLite database for tests).

---

### Customization and extensions

- **Add new KPIs**: Define new functions in `kpis.py` and add them to the dashboard in `app.py`.
- **Change alert thresholds**: Modify `REVENUE_THRESHOLD` and `ORDERS_THRESHOLD` in the `.env` file.
- **Connect to Snowflake**: Install `snowflake-sqlalchemy` and modify the `get_engine()` function in `database.py` to use the Snowflake URL.
- **Add more charts**: Create new functions in `charts.py` and place them in `app.py` with `st.plotly_chart()`.
- **Additional roles**: Extend the logic in `auth.py` to handle more granular permissions.

---

### Contributions and support

This project is a solid starting point for teams wanting to implement a KPI dashboard with Python. If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

### License

MIT – Free for commercial and educational use.
```
