CREATE TABLE csp.fe_pastry_inventory (
    product_id INT NOT NULL,
    sales_outlet_id INT,
    start_of_day_stock INT,
    quantity_sold INT,
    transaction_date DATE,
    waste_number INT,
    waste_percentage FLOAT
)