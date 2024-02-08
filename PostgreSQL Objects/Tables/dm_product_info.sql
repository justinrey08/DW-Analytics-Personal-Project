CREATE TABLE csp.dm_product_info (
    product_id INT REFERENCES csp.fe_product(product_id),
    new_product VARCHAR(50),
    product VARCHAR(50),
    product_category VARCHAR(50),
    product_description VARCHAR(255),
    prodcut_group VARCHAR(50),
    product_type VARCHAR(50)
)