import pytest
from kpis import (calculate_revenue, calculate_avg_order_value,
                  calculate_orders_count, calculate_active_customers)

def test_calculate_revenue(sample_df):
    assert calculate_revenue(sample_df) == 2430

def test_calculate_avg_order_value(sample_df):
    assert calculate_avg_order_value(sample_df) == 243.0

def test_calculate_orders_count(sample_df):
    assert calculate_orders_count(sample_df) == 10

def test_calculate_active_customers(sample_df):
    # Con customer_id distintos, debería dar 10
    assert calculate_active_customers(sample_df) == 10
