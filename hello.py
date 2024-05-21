import psycopg2
from flask import Flask
        
app = Flask(__name__)    
    
DBHOST = 'final-rg.postgres.database.azure.com'
DBNAME = 'postgres'
DB_USER = 'dengin'
DB_PASSWORD = 'Diken1234'

def get_connection():
    return psycopg2.connect(host=DBHOST, dbname=DBNAME, user=DB_USER, password=DB_PASSWORD)

@app.route('/hello')
def hello():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello, World!'")
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result

if __name__ == '__main__':
    app.run(debug=True)
    
