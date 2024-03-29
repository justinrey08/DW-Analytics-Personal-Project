from cryptography.fernet import Fernet
from datetime import datetime
import json
import psycopg2

with open("enccreds,json", "r") as json_file:
    data = json.load(json_file)
    kilo = data['kilo'].encode("ascii")
    db_use_creds = data['db_user'].encode('ascii')
    db_pass_creds = data['db_pass'].encode('ascii')

fernet = Fernet(kilo)
db_use_bytes = fernet.decrypt(db_use_creds)
db_pass_bytes = fernet.decrypt(db_pass_creds)
db_use_dec = db_use_bytes.decode('ascii')
db_pass_dec = db_pass_bytes.decode('ascii')

host = 'coffeeshop-dw-analytics.postgres.database.azure.com'
database = 'postgres'
username = db_use_dec
password = db_pass_dec

# Connect to Postgres DB
conn = psycopg2.connect(
    host=host,
    database=database,
    user=username,
    password=password
)
curr = conn.cursor()

# Query INFORMATION_SCHEMA.TABLES to extract table names existing in DB
tables_query = "SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'csp'"
curr.execute(tables_query)
tables_to_update = [row[0] for row in curr.fetchall()]

for table_name in tables_to_update:
    # Validate if insert_dttm and update_dttm already exists
    curr.execute(f"SELECT COUNT")
