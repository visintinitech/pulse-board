import pytest
import pandas as pd
from datetime import datetime, timedelta

@pytest.fixture
def sample_df():
    # Crear DataFrame de prueba
    dates = [datetime.today() - timedelta(days=i) for i in range(10)]
    data = {
        'order_id': [1,2,3,4,5,6,7,8,9,10],
        'order_date': dates,
        'total_amount': [100, 200, 150, 300, 250, 180, 220, 400, 350, 280],
        'category': ['Electrónica', 'Ropa', 'Electrónica', 'Hogar', 'Ropa',
                     'Electrónica', 'Hogar', 'Ropa', 'Electrónica', 'Hogar'],
        'country': ['ES', 'ES', 'FR', 'ES', 'FR', 'ES', 'FR', 'ES', 'ES', 'FR'],
        'customer_id': [101,102,103,104,105,106,107,108,109,110]
    }
    return pd.DataFrame(data)
