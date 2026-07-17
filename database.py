from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import pandas as pd
from config import DB_TYPE, DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, SQLITE_PATH

def get_engine():
    if DB_TYPE == "postgresql":
        url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    else:  # sqlite
        url = f"sqlite:///{SQLITE_PATH}"
    return create_engine(url)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

def query_data(sql, params=None):
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql_query(text(sql), conn, params=params)

# Funciones específicas de consulta (con caché)

def get_orders_by_date(start_date, end_date, category=None):
    sql = """
        SELECT o.id as order_id, o.order_date, o.total_amount, 
               p.category, c.country
        FROM orders o
        JOIN order_items oi ON o.id = oi.order_id
        JOIN products p ON oi.product_id = p.id
        JOIN customers c ON o.customer_id = c.id
        WHERE o.order_date BETWEEN :start AND :end
          AND o.status = 'completed'
    """
    params = {"start": start_date, "end": end_date}
    if category:
        sql += " AND p.category = :category"
        params["category"] = category
    return query_data(sql, params)

def get_all_categories():
    sql = "SELECT DISTINCT category FROM products ORDER BY category"
    return query_data(sql)['category'].tolist()
