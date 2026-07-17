import plotly.express as px
import plotly.graph_objects as go

def create_revenue_line(df):
    daily = df.groupby('order_date')['total_amount'].sum().reset_index()
    fig = px.line(daily, x='order_date', y='total_amount',
                  title='Evolución de ingresos diarios',
                  labels={'order_date':'Fecha', 'total_amount':'Ingresos (€)'})
    return fig

def create_category_bar(df):
    cat = df.groupby('category')['total_amount'].sum().reset_index()
    fig = px.bar(cat, x='category', y='total_amount',
                 title='Ingresos por categoría',
                 labels={'category':'Categoría', 'total_amount':'Ingresos (€)'})
    return fig

def create_orders_by_country(df):
    country_orders = df.groupby('country')['order_id'].nunique().reset_index()
    fig = px.bar(country_orders, x='country', y='order_id',
                 title='Pedidos por país',
                 labels={'country':'País', 'order_id':'Nº pedidos'})
    return fig

def create_top_products(df, top_n=5):
    # Asumiendo que df tiene product_id y quantity (o category y total_amount)
    if 'product_id' in df.columns:
        top = df.groupby('product_id')['quantity'].sum().nlargest(top_n).reset_index()
    else:
        top = df.groupby('category')['total_amount'].sum().nlargest(top_n).reset_index()
        top.columns = ['product', 'value']
    fig = px.bar(top, x='product', y='value', title=f'Top {top_n} productos')
    return fig

def create_gauge(value, title, threshold, max_val=None):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={'axis': {'range': [None, max_val or value*1.5]},
               'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': threshold}}))
    return fig
