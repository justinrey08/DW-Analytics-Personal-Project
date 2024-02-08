CREATE TABLE csp.dm_product_misc_info (
    product_id INT REFERENCES csp.fe_product(product_id),
    promo BOOL,
    tax_exempt BOOL,
    unit_of_measure VARCHAR(50)
)