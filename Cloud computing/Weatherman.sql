Create Database Weatherman_DB;
USE Weatherman_DB;

-- Users Table
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
   
);

-- Locations Table
CREATE TABLE Locations (
    location_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    latitude DECIMAL(9,6) NOT NULL,
    longitude DECIMAL(9,6) NOT NULL,
    region VARCHAR(255) NOT NULL
);

-- Rainfall Data Table
CREATE TABLE RainfallData (
    rainfall_id SERIAL PRIMARY KEY,
    location_id INT NOT NULL,
    rainfall_mm DECIMAL(5,2) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    data_source VARCHAR(255),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

-- Flood Events Table
CREATE TABLE FloodEvents (
    flood_event_id SERIAL PRIMARY KEY,
    location_id INT NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,
    flood_level VARCHAR(50) NOT NULL,
    damage_estimate DECIMAL(15,2),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

CREATE TABLE FloodRiskPredictions (
    prediction_id SERIAL PRIMARY KEY,
    location_id INT NOT NULL,
    risk_level VARCHAR(50) NOT NULL,
    forecast_date TIMESTAMP NOT NULL,
    prediction_data TEXT,  -- Use TEXT for older versions
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

