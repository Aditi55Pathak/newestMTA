from flask import Flask
import mysql.connector
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(
            host='db',  
            user='root',
            password='Atg@105pa',
            database='mydatabase'
        )
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM mytable')
        data = cursor.fetchall()
        conn.close()
        return str(data)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return "An error occurred while processing your request", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
