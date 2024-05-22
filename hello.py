import psycopg2
from flask import Flask

# Veritabanı bağlantısı kur
host = "final-rg.postgres.database.azure.com"
dbname = "postgres"
user = "dengin"
password = "Diken1234"
sslmode = "require"
port = 5432
# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4} port={5}".format(host, user, dbname, password, sslmode,port)

try:
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    cursor = conn.cursor()
except TypeError as e:
    print(f"An error occurred: {e}")
    
    
app = Flask(__name__)    

@app.route('/hello')
def hello():
    return "Hello, our my Colleagues!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int("3000"),debug=True)
    