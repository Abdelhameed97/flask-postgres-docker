from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Connect to PostgreSQL using environment variables
        conn = psycopg2.connect(
            dbname=os.environ.get('POSTGRES_DB', 'mydb'),
            user=os.environ.get('POSTGRES_USER', 'user'),
            password=os.environ.get('POSTGRES_PASSWORD', 'password'),
            host=os.environ.get('DB_HOST', 'db'),
            port=5432
        )
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        db_version = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"✅ Connected to PostgreSQL!<br>DB Version: {db_version[0]}"
    except Exception as e:
        return f"❌ Failed to connect to PostgreSQL:<br>{e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
