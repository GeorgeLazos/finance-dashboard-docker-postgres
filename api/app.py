import os
import psycopg2
from flask import Flask, jsonify, make_response

#Create Flask app instance
app = Flask(__name__)

#Allow cross-origin requests from the frontend
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


#Connect to the database using environment variables
def get_db_conn():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'password'),
        dbname=os.environ.get('DB_NAME', 'coinsafe')
    )


#Run function when /health endpoint is accessed
@app.route('/health')
#Function to check endpoint health and return JSON response
def health_check():
    return jsonify({"status": "healthy"}), 200

#Return all transactions from the database as JSON
@app.route('/api/transactions')
def get_transactions():
    conn = get_db_conn() #Connect to the database
    cur = conn.cursor()  # Create a cursor to execute SQL queries
    #Execute SQL query to select all transactions and fetch results
    cur.execute("SELECT id, user_id, amount, transaction_type, timestamp FROM transactions")
    rows = cur.fetchall()   # Fetch all rows returned by the query
    cur.close() 
    conn.close()

    # Convert query results to JSON format and return with 200 OK status
    return jsonify([
        {"id": r[0], "user_id": r[1], "amount": float(r[2]),
         "transaction_type": r[3], "timestamp": str(r[4])}
        for r in rows
    ]), 200


#Return summary of transactions grouped by type
@app.route('/api/summary')
def get_summary():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT transaction_type, COUNT(*), SUM(amount)
        FROM transactions
        GROUP BY transaction_type
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {"type": r[0], "count": r[1], "total": float(r[2])}
        for r in rows
    ]), 200


#Start Flask server on all interfaces so it is reachable from other containers
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
