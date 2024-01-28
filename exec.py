import subprocess
import psycopg2

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
            dbname =DATABASE['database'],
            user =DATABASE['username'],
            password=DATABASE['password'],
            host=DATABASE['host'],
            port=DATABASE['port']
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def fetch_ticker_id(conn, ticker_symbol):
    with conn.cursor() as cur:
        cur.execute("SELECT ticker_id FROM tickers WHERE ticker_symbol = %s", (ticker_symbol,))
        result = cur.fetchone()
        return result[0] if result else None

def get_closing_prices(conn, ticker_id):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT close FROM stock_data
            WHERE ticker_id = %s
            ORDER BY date ASC;
            """, (ticker_id,))
        return [row[0] for row in cur.fetchall()]

def main():
    conn = connect_to_db()
    if conn:
        ticker_symbol = input("Enter the ticker symbol: ")
        ticker_id = fetch_ticker_id(conn, ticker_symbol)
        if ticker_id is not None:
            closing_prices = get_closing_prices(conn, ticker_id)
            
            process = subprocess.Popen(['./analysis'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for close in closing_prices:
                process.stdin.write(f"{close}\n")
            process.stdin.close()
            
            for line in process.stdout:
                print(line.strip())

        else:
            print("Ticker symbol not found in the database.")
        conn.close()

if __name__ == "__main__":
    main()
