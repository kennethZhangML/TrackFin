CREATE TABLE stock_data (
    data_id SERIAL PRIMARY KEY,
    ticker_id INTEGER REFERENCES tickers(ticker_id),
    date DATE NOT NULL,
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    adj_close NUMERIC,
    volume BIGINT,
    UNIQUE (ticker_id, date) 
);
