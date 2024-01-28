import psycopg2
import yfinance as yf
from datetime import datetime

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

def fetch_ticker_id(conn, ticker_symbol):
    with conn.cursor() as cur:
        cur.execute("SELECT ticker_id FROM tickers WHERE ticker_symbol = %s", (ticker_symbol,))
        result = cur.fetchone()
        return result[0] if result else None

def download_finance_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period="1y")  
    return data

def insert_finance_data(conn, ticker_id, data):
    with conn.cursor() as cur:
        for index, row in data.iterrows():
            try:
                cur.execute("""
                    INSERT INTO stock_data (ticker_id, date, open, high, low, close, volume) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (ticker_id, date) DO NOTHING;
                    """, (ticker_id, index.date(), row['Open'], row['High'], row['Low'], row['Close'], row['Volume']))
            except Exception as e:
                print(f"Error inserting data: {e}")

def main():
    conn = connect_to_db()
    if conn:
        ticker_symbol = input("Enter the ticker symbol for the data you want to download: ")
        ticker_id = fetch_ticker_id(conn, ticker_symbol)
        if ticker_id:
            data = download_finance_data(ticker_symbol)
            insert_finance_data(conn, ticker_id, data)
        else:
            print("Ticker symbol not found in the database.")
        conn.close()

if __name__ == "__main__":
    main()
