CREATE TABLE csp.fe_customers (
    customer_id INT NOT NULL,
    customer_name VARCHAR(20),
    customer_email VARCHAR(25),
    customer_since DATE,
    gender VARCHAR(8),
    birthdate DATE,
    birthyear INT,
    home_store INT,
    loyalty_card_number VARCHAR(10)
)