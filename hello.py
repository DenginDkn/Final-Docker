import psycopg2
from psycopg2 import OperationalError

# Veritabanı bağlantısı kur
host = "final-rg.postgres.database.azure.com"
dbname = "postgres"
user = "dengin"
password = "Diken1234"
sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)

try:
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()
except OperationalError as e:
    print(f"An error occurred: {e}")
    
def main():
    print("Hello world")

if __name__ == "__main__":
    main()
