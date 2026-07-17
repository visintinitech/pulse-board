import os
from dotenv import load_dotenv

load_dotenv()

# Base de datos
DB_TYPE = os.getenv("DB_TYPE", "postgresql")  # 'postgresql' o 'sqlite'
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "pulseboard")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

# Para SQLite (fallback)
SQLITE_PATH = os.getenv("SQLITE_PATH", "data/pulseboard.db")

# Configuración de correo
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
ALERT_EMAIL = os.getenv("ALERT_EMAIL", "admin@example.com")

# Umbrales de alerta
REVENUE_THRESHOLD = float(os.getenv("REVENUE_THRESHOLD", 10000))
ORDERS_THRESHOLD = int(os.getenv("ORDERS_THRESHOLD", 50))

# Configuración de caché
CACHE_TTL = int(os.getenv("CACHE_TTL", 300))  # segundos
