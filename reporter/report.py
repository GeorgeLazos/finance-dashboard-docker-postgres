import os
import psycopg2


#Connect to the database using environment variables
def get_db_conn():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'password'),
        dbname=os.environ.get('DB_NAME', 'coinsafe')
    )


#Connect to database query results and generate daily financial report
def generate_report():
    print("Starting daily financial report generation...")
    conn = get_db_conn()
    cur = conn.cursor()

    #Query total transaction count and sum
    cur.execute("SELECT COUNT(*), SUM(amount) FROM transactions")
    total_count, total_amount = cur.fetchone()

    #Query breakdown by transaction type
    cur.execute("""
        SELECT transaction_type, COUNT(*), SUM(amount)
        FROM transactions
        GROUP BY transaction_type
    """)
    breakdown = cur.fetchall()

    cur.close()
    conn.close()

    print("----------------------------------------")
    print("DAILY SUMMARY REPORT")
    print(f"Total transactions: {total_count}")
    print(f"Total amount:       £{total_amount:.2f}")
    print("\nBreakdown by type:")
    for row in breakdown:
        print(f"  {row[0]}: {row[1]} transactions, £{float(row[2]):.2f}")
    print("----------------------------------------")


if __name__ == "__main__":
    generate_report()
