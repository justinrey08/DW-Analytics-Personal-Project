CREATE TABLE csp.fe_dates (
    date_id INT NOT NULL,
    month_id INT NOT NULL,
    month_name VARCHAR(15),
    quarter_id INT NOT NULL,
    quarter_name VARCHAR(15),
    week_id INT NOT NULL,
    week_desc VARCHAR(25),
    year_id INT NOT NULL,
    transaction_date DATE
)