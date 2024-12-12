
-- Users Table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

-- Locations Table
CREATE TABLE Locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,  
    name VARCHAR(255) NOT NULL,
    latitude DECIMAL(9,6) NOT NULL,
    longitude DECIMAL(9,6) NOT NULL,
    region VARCHAR(255) NOT NULL
);

-- Rainfall Data Table
CREATE TABLE RainfallData (
    rainfall_id INT AUTO_INCREMENT PRIMARY KEY,  
    location_id INT NOT NULL,
    rainfall_mm DECIMAL(5,2) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    data_source VARCHAR(255),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

-- Flood Events Table
CREATE TABLE FloodEvents (
    flood_event_id INT AUTO_INCREMENT PRIMARY KEY,  
    location_id INT NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,
    flood_level VARCHAR(50) NOT NULL,
    damage_estimate DECIMAL(15,2),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)  
);

-- Flood Risk Predictions Table
CREATE TABLE FloodRiskPredictions (
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,  
    location_id INT NOT NULL,
    risk_level VARCHAR(50) NOT NULL,
    forecast_date TIMESTAMP NOT NULL,
    prediction_data TEXT,  
    FOREIGN KEY (location_id) REFERENCES Locations(location_id) 
);



-- User History Table: Tracks user activities
CREATE TABLE UserHistory (
    history_id INT AUTO_INCREMENT PRIMARY KEY, 
    user_id INT NOT NULL,                       
    action VARCHAR(255) NOT NULL,               
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    details TEXT,                                
    FOREIGN KEY (user_id) REFERENCES Users(user_id) 
);