CREATE TABLE csp.fe_product (
    product_id INT,
    current_retail_price FLOAT,
    current_wholesale_price FLOAT,
    new_product VARCHAR(50),
    product_category VARCHAR(50),
    product_description VARCHAR(255),
    product_group VARCHAR(50),
    product_type VARCHAR(50),
    promo BOOL,
    tax_exempt BOOL,
    unit_of_measure VARCHAR(50)
)