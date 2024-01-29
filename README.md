# TrackFin

TrackFin is a comprehensive financial data management and analysis application designed to handle stock market data effectively. It allows users to manage ticker symbols, download and view financial data, and perform data analysis.

## Features

- **Ticker Management**: Add new ticker symbols to your database.
- **Data Viewing**: Search for existing tickers and view associated financial data.
- **Data Downloading**: Download financial data for tickers not present in the database.
- **User-Friendly Interface**: Easy-to-use command-line interface for navigating the application.

## Installation

```bash
# Clone the repository
git clone [repository-url]

# Navigate to the project directory
cd TrackFin
```

# TrackFin Project Structure

TrackFin is structured with several key files, each serving a specific purpose in the application. Below is a description of each file and its role in the project.

## Python Scripts

### `tickers.py`
- **Purpose**: Manages ticker symbols in the database.
- **Functionality**:
  - Adds new ticker symbols to the `tickers` table in the database.
  - Checks if a ticker symbol already exists to prevent duplicates.
  - Connects to the PostgreSQL database using `psycopg2`.

### `view.py`
- **Purpose**: Handles viewing and fetching stock data for existing tickers.
- **Functionality**:
  - Checks if a given ticker symbol exists in the `tickers` table.
  - Fetches and displays stock data for a given ticker from the `stock_data` table for a specific date.
  - Uses `psycopg2` for database operations.

### `download.py`
- **Purpose**: Downloads and updates financial data for tickers.
- **Functionality**:
  - Downloads financial data for a given ticker symbol using the `yfinance` library.
  - Inserts the downloaded financial data into the `stock_data` table in the database.
  - Ensures no duplicate entries are created in the database.

### `main.py`
- **Purpose**: Serves as the main entry point for the application.
- **Functionality**:
  - Provides a command-line interface for user interaction.
  - Allows users to choose between searching/viewing existing tickers or adding new tickers and downloading data.
  - Integrates and orchestrates the flow between `tickers.py`, `view.py`, and `download.py`.

## C++ File

### `analysis.cpp`
- **Purpose**: Performs complex and performance-intensive financial data analysis.
- **Functionality**:
  - Implements advanced algorithms for analyzing stock market data. These could include statistical analysis, trend detection, predictive modeling, or other complex financial computations.
  - Optimized for performance, handling large datasets or calculations that are computationally intensive, which is a common use case for incorporating C++ in a data analysis pipeline.
  - [If applicable] Interacts with the Python components of the application, possibly using a Python-C++ bridge like `pybind11`, to provide results back to the main application for further use or display.
  - [If applicable] Generates reports or summaries of the analyzed data, which could be used for making informed financial decisions or understanding market trends.

## SQL Scripts

### `createSD.sql` and `createTables.sql`
- **Purpose**: Used for setting up the database schema.
- **Functionality**:
  - Defines the structure of tables such as `tickers` and `stock_data`.
  - Includes SQL commands for creating necessary tables and configuring their fields.

## Configuration and Setup

- **Database Configuration**:
  - The application connects to a PostgreSQL database.
  - Database credentials and connection details are defined within the Python scripts.

- **Dependency Installation**:
  - Requires `psycopg2` for database connectivity and `yfinance` for downloading stock data.

- **Running the Application**:
  - Execute `python main.py` in the command line to start the application.

## Contributing

- Contributions to enhance and expand TrackFin's capabilities are welcome.


