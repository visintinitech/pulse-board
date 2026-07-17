import pandas as pd
import numpy as np

def calculate_revenue(df):
    return df['total_amount'].sum()

def calculate_avg_order_value(df):
    total = df['total_amount'].sum()
    orders = df['order_id'].nunique()
    return total / orders if orders > 0 else 0

def calculate_orders_count(df):
    return df['order_id'].nunique()

def calculate_active_customers(df, days=30):
    # Suponemos que tenemos columna 'customer_id' en df
    if 'customer_id' not in df.columns:
        # Si no, lo simulamos con country (solo para demo)
        return df['country'].nunique()
    return df['customer_id'].nunique()

def calculate_revenue_vs_previous(df, previous_df):
    current = calculate_revenue(df)
    previous = calculate_revenue(previous_df) if previous_df is not None else 0
    if previous == 0:
        return 0
    return (current - previous) / previous * 100

def calculate_top_products(df, top_n=5):
    # Agrupar por producto (necesitamos product_id, quantity)
    if 'product_id' in df.columns and 'quantity' in df.columns:
        top = df.groupby('product_id')['quantity'].sum().nlargest(top_n).reset_index()
        return top
    else:
        # Simulación con categorías
        top = df.groupby('category')['total_amount'].sum().nlargest(top_n).reset_index()
        top.columns = ['product_id', 'quantity']  # renombramos para consistencia
        return top
