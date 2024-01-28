import psycopg2
from datetime import datetime
from download import fetch_ticker_id

DATABASE = {
    'username': 'kennethzhang',
    'password': 'Trolled#0223',
    'host': 'localhost',
    'port': '5432',
    'database': 'fintrackengine'
}

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=DATABASE['database'],
            user=DATABASE['username'],
            password=DATABASE['password'],
            host=DATABASE['host'],
            port=DATABASE['port']
        )
        conn.autocommit = True
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def ticker_exists(conn, ticker_symbol):
    with conn.cursor() as cur:
        cur.execute("SELECT EXISTS(SELECT 1 FROM tickers WHERE ticker_symbol = %s)", (ticker_symbol,))
        return cur.fetchone()[0]

def fetch_stock_data(conn, ticker_id, date):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT * FROM stock_data 
            WHERE ticker_id = %s AND date = %s
            """, (ticker_id, date))
        return cur.fetchone()

def main():
    conn = connect_to_db()
    if conn:
        ticker_symbol = input("Enter the ticker symbol to check in the database: ")
        if ticker_exists(conn, ticker_symbol):
            ticker_id = fetch_ticker_id(conn, ticker_symbol)
            date_input = input("Enter the date for the stock data (YYYY-MM-DD): ")
            try:
                date_formatted = datetime.strptime(date_input, "%Y-%m-%d").date()
                stock_data = fetch_stock_data(conn, ticker_id, date_formatted)
                if stock_data:
                    print("Stock Data Found:", stock_data)
                else:
                    print("No data found for that date.")
            except ValueError as e:
                print("Date format error:", e)
        else:
            print("Ticker symbol not found.")
        conn.close()

if __name__ == "__main__":
    main()
