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
        return psycopg2.connect(
            dbname=DATABASE['database'],
            user=DATABASE['username'],
            password=DATABASE['password'],
            host=DATABASE['host'],
            port=DATABASE['port']
        )
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def add_ticker(conn, ticker_symbol, company_name):
    with conn.cursor() as cur:
        try:
            cur.execute("""
                INSERT INTO tickers (ticker_symbol, company_name) 
                VALUES (%s, %s)
                ON CONFLICT (ticker_symbol) DO NOTHING;
                """, (ticker_symbol, company_name))
            conn.commit()
            print(f"Ticker {ticker_symbol} added successfully.")
        except Exception as e:
            print(f"Error adding ticker: {e}")

def main():
    conn = connect_to_db()
    if conn:
        while True:
            ticker_symbol = input("Enter ticker symbol (or 'exit' to quit): ")
            if ticker_symbol.lower() == 'exit':
                break
            company_name = input("Enter company name: ")
            add_ticker(conn, ticker_symbol, company_name)
        conn.close()

if __name__ == "__main__":
    main()
