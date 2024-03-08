CREATE TABLE
    user (
        user_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(25) NOT NULL,
        last_name VARCHAR(40) NOT NULL,
        email VARCHAR(40) NOT NULL,
        pass_word VARCHAR(30) NOT NULL,
        created_date DATE,
        is_active BOOLEAN,
        username VARCHAR(25) NOT NULL,
        UNIQUE (email, username)
    );

CREATE TABLE
    user_address (
        address_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        street_address VARCHAR(40),
        city VARCHAR(25),
        st VARCHAR(25),
        zip_code VARCHAR(10),
        country VARCHAR(30),
        CONSTRAINT fk_user_address_user_id FOREIGN KEY (user_id) REFERENCES user (user_id)
    );

CREATE TABLE
    driver_license (
        driver_license_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        driver_license_number INT NOT NULL,
        st VARCHAR(50) NOT NULL,
        expiration_date DATE NOT NULL,
        issue_date DATE NOT NULL,
        CONSTRAINT fk_driver_license_user_id FOREIGN KEY (user_id) REFERENCES user (user_id)
    );

CREATE TABLE
    vehicle (
        vehicle_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        vehicle_type VARCHAR(25) NOT NULL,
        make VARCHAR(25) NOT NULL,
        model VARCHAR(25) NOT NULL,
        production_year INT(4) NOT NULL,
        color VARCHAR(25) NOT NULL,
        CONSTRAINT fk_vehicle_user_id FOREIGN KEY (user_id) REFERENCES user (user_id)
    );

CREATE TABLE
    parking_info (
        parking_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        vehicle_id INT NOT NULL,
        floor INT NOT NULL,
        section VARCHAR(1) NOT NULL,
        bay_number INT NOT NULL,
        day_parked DATE NOT NULL,
        length_days INT NOT NULL,
        pick_up_time TIME NOT NULL,
        CONSTRAINT fk_parking_info_vehicle_id FOREIGN KEY (vehicle_id) REFERENCES vehicle (vehicle_id)
    );