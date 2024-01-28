import tickers
import view
import download
import datetime 

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Search and View Existing Tickers")
        print("2. Add New Tickers and Download Data")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            search_and_view()
        elif choice == '2':
            add_and_download()
        elif choice == '3':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-3.")

def search_and_view():
    conn = view.connect_to_db()
    if conn:
        ticker_symbol = input("Enter the ticker symbol to check in the database: ")
        if view.ticker_exists(conn, ticker_symbol):
            date_input = input("Enter the date for the stock data (YYYY-MM-DD): ")
            try:
                date_formatted = datetime.strptime(date_input, "%Y-%m-%d").date()
                stock_data = view.fetch_stock_data(conn, ticker_symbol, date_formatted)
                if stock_data:
                    print("Stock Data Found:", stock_data)
                else:
                    print("No data found for that date.")
            except ValueError as e:
                print("Date format error:", e)
        else:
            print("Ticker symbol not found.")
        conn.close()
    else:
        print("Failed to connect to the database.")

def add_and_download():
    conn = tickers.connect_to_db()
    if conn:
        ticker_symbol = input("Enter the ticker symbol to add: ")
        company_name = input("Enter the company name: ")
        tickers.add_ticker(conn, ticker_symbol, company_name)

        download.download_finance_data(ticker_symbol)
        print("Data for", ticker_symbol, "downloaded and added to the database.")
        conn.close()
    else:
        print("Failed to connect to the database.")


if __name__ == "__main__":
    main_menu()
