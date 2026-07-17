import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from config import REVENUE_THRESHOLD, ORDERS_THRESHOLD, CACHE_TTL
from database import get_orders_by_date, get_all_categories
from kpis import (calculate_revenue, calculate_avg_order_value,
                  calculate_orders_count, calculate_active_customers,
                  calculate_revenue_vs_previous)
from charts import (create_revenue_line, create_category_bar,
                    create_orders_by_country, create_top_products)
from auth import login, logout, is_admin, admin_panel
from notifications import check_alerts_and_notify

# Configuración de página
st.set_page_config(page_title="PulseBoard", layout="wide", initial_sidebar_state="expanded")

# Inicializar sesión
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Sidebar de autenticación
if not st.session_state["logged_in"]:
    login()
    st.stop()
else:
    st.sidebar.markdown(f"👤 {st.session_state['username']} ({st.session_state['role']})")
    if st.sidebar.button("Cerrar sesión"):
        logout()

# Caché de datos (TTL configurable)
@st.cache_data(ttl=CACHE_TTL)
def load_data(start_date, end_date, category):
    return get_orders_by_date(start_date, end_date, category)

# Sidebar filtros
st.sidebar.header("Filtros")
default_start = datetime.today() - timedelta(days=30)
start_date = st.sidebar.date_input("Fecha inicio", default_start)
end_date = st.sidebar.date_input("Fecha fin", datetime.today())
categories = get_all_categories()
selected_categories = st.sidebar.multiselect("Categorías", categories, default=categories)

# Obtener datos
df = load_data(start_date, end_date, selected_categories if selected_categories else None)

if df.empty:
    st.warning("No hay datos para los filtros seleccionados.")
    st.stop()

# Calcular KPIs
revenue = calculate_revenue(df)
orders = calculate_orders_count(df)
avg_order = calculate_avg_order_value(df)
active_customers = calculate_active_customers(df)

# Obtener periodo anterior (misma duración)
prev_start = start_date - (end_date - start_date)
prev_df = load_data(prev_start, start_date, selected_categories if selected_categories else None)
revenue_variation = calculate_revenue_vs_previous(df, prev_df)

# Almacenar KPIs para alertas
kpis_dict = {
    "revenue": revenue,
    "orders": orders,
    "avg_order": avg_order,
    "active_customers": active_customers
}
# Verificar alertas y enviar correo
check_alerts_and_notify(kpis_dict)

# Título
st.title("📊 PulseBoard - Dashboard de KPIs")

# Métricas
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Ingresos totales", f"${revenue:,.2f}", delta=f"{revenue_variation:.1f}%")
col2.metric("📦 Pedidos", orders)
col3.metric("🧾 Ticket promedio", f"${avg_order:,.2f}")
col4.metric("👥 Clientes activos", active_customers)

# Gráficos
col_chart1, col_chart2 = st.columns(2)
with col_chart1:
    fig_line = create_revenue_line(df)
    st.plotly_chart(fig_line, use_container_width=True)
with col_chart2:
    fig_bar = create_category_bar(df)
    st.plotly_chart(fig_bar, use_container_width=True)

col_chart3, col_chart4 = st.columns(2)
with col_chart3:
    fig_country = create_orders_by_country(df)
    st.plotly_chart(fig_country, use_container_width=True)
with col_chart4:
    fig_top = create_top_products(df)
    st.plotly_chart(fig_top, use_container_width=True)

# Tabla detallada
st.subheader("📋 Detalle de pedidos")
st.dataframe(df[['order_date', 'total_amount', 'category', 'country']].sort_values('order_date', ascending=False))

# Exportación
if st.button("📥 Exportar datos a CSV"):
    csv = df.to_csv(index=False)
    st.download_button("Descargar CSV", data=csv, file_name="pulseboard_export.csv", mime="text/csv")

# Panel de administración (solo admin)
if is_admin():
    with st.expander("🔧 Administración", expanded=False):
        admin_panel()
