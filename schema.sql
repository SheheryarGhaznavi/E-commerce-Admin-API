CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

-- Products Table
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL
);

-- Sales Table
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    total_price FLOAT NOT NULL,
    sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Inventory Table
CREATE TABLE inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL UNIQUE,
    stock_level INT NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Sample Products
INSERT INTO products (name, category, price) VALUES
('MacBook Pro', 'Electronics', 2500),
('iPhone 14', 'Electronics', 999),
('T-Shirt', 'Clothing', 25),
('Running Shoes', 'Footwear', 120);

-- Sample Inventory
INSERT INTO inventory (product_id, stock_level) VALUES
(1, 5),
(2, 12),
(3, 3),
(4, 20);

-- Sample Sales
INSERT INTO sales (product_id, quantity, total_price, sale_date) VALUES
(1, 1, 2500, '2025-05-01'),
(2, 2, 1998, '2025-05-02'),
(3, 3, 75, '2025-05-05'),
(4, 1, 120, '2025-05-06');
