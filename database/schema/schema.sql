-- HomeScope Core Database Schema

CREATE TABLE zip_codes (
    zip_id SERIAL PRIMARY KEY,
    zip_code VARCHAR(10) UNIQUE NOT NULL,
    city VARCHAR(100),
    state VARCHAR(50)
);

CREATE TABLE housing_metrics (
    metric_id SERIAL PRIMARY KEY,
    zip_code VARCHAR(10) REFERENCES zip_codes(zip_code),
    date DATE NOT NULL,

    median_rent FLOAT,
    median_home_price FLOAT,
    median_income FLOAT,

    mortgage_rate FLOAT,

    rent_burden_ratio FLOAT,
    affordability_index FLOAT
);