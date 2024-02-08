CREATE TABLE csp.dm_product_prices (
	product_id INT REFERENCES csp.fe_product(product_id),
	current_retail_price FLOAT,
	current_wholesale_price FLOAT
)