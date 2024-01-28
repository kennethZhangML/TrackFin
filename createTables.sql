CREATE TABLE tickers (
    ticker_id SERIAL PRIMARY KEY,
    ticker_symbol VARCHAR(10) UNIQUE NOT NULL,
    company_name VARCHAR(255) 
);

