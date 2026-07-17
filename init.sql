-- Crear tablas (igual que en models.py)
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    registration_date DATE,
    country VARCHAR(2)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    order_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(20)
);

CREATE TABLE order_items (
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    PRIMARY KEY (order_id, product_id)
);

-- Insertar datos de prueba (puedes usar faker)
INSERT INTO products (name, category, price) VALUES
('Laptop', 'Electrónica', 800),
('Smartphone', 'Electrónica', 600),
('Camiseta', 'Ropa', 20),
('Pantalón', 'Ropa', 40),
('Sofá', 'Hogar', 300);

INSERT INTO customers (name, email, registration_date, country) VALUES
('Juan', 'juan@mail.com', '2025-01-01', 'ES'),
('Maria', 'maria@mail.com', '2025-01-05', 'FR'),
('Pedro', 'pedro@mail.com', '2025-01-10', 'ES');

-- Pedidos de ejemplo (fechas recientes)
INSERT INTO orders (customer_id, order_date, total_amount, status) VALUES
(1, CURRENT_DATE - INTERVAL '1 day', 820, 'completed'),
(2, CURRENT_DATE - INTERVAL '2 days', 620, 'completed'),
(3, CURRENT_DATE - INTERVAL '3 days', 340, 'completed'),
(1, CURRENT_DATE - INTERVAL '5 days', 40, 'completed');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 800),
(1, 3, 1, 20),
(2, 2, 1, 600),
(2, 4, 1, 20),   -- error? corregir
(3, 5, 1, 300),
(3, 3, 2, 20),
(4, 3, 2, 20);
