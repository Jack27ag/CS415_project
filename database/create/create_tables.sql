CREATE TABLE
    user (
        user_id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255),
        created_date DATETIME,
        is_active BOOLEAN,
        username VARCHAR(255)
    );

CREATE TABLE
    user_address (
        address_id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        street_address VARCHAR(255),
        city VARCHAR(255),
        state VARCHAR(255),
        zip_code VARCHAR(255),
        country VARCHAR(255),
        CONSTRAINT fk_user_address_user_id FOREIGN KEY (user_id) REFERENCES user (user_id)
    );

CREATE TABLE
    driver_license (
        driver_license_id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        driver_license_number INT,
        state_or_province VARCHAR(255),
        expiration_date DATE,
        issue_date DATE,
        CONSTRAINT fk_driver_license_user_id FOREIGN KEY (user_id) REFERENCES user (user_id)
    );

CREATE TABLE
    vehicle (
        vehicle_id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        vehicle_type VARCHAR(255),
        make VARCHAR(255),
        model VARCHAR(255),
        year YEAR,
        color VARCHAR(255),
        CONSTRAINT fk_vehicle_user_id FOREIGN KEY (user_id) REFERENCES user (user_id)
    );

CREATE TABLE
    parking_info (
        parking_id INT PRIMARY KEY AUTO_INCREMENT,
        vehicle_id INT,
        floor INT NOT NULL,
        section VARCHAR(255) NOT NULL,
        bay_number INT NOT NULL,
        day_parked DATE NOT NULL,
        length_days INT NOT NULL,
        pick_up_time TIME NOT NULL,
        CONSTRAINT fk_parking_info_vehicle_id FOREIGN KEY (vehicle_id) REFERENCES vehicle (vehicle_id)
    );