CREATE TABLE buses (
    bus_id INT PRIMARY KEY AUTO_INCREMENT,
    bus_name VARCHAR(255) NOT NULL,
    bus_type VARCHAR(255) NOT NULL,
    total_seats INT NOT NULL
);

CREATE TABLE routes (
    route_id INT PRIMARY KEY AUTO_INCREMENT,
    source_ VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    fare INT NOT NULL
);

CREATE TABLE passengers (
    passenger_id INT PRIMARY KEY AUTO_INCREMENT,
    pass_name VARCHAR(255) NOT NULL,
    pass_email VARCHAR(255) NOT NULL,
    pass_phone VARCHAR(20) NOT NULL
);

CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    booking_date VARCHAR(100) NOT NULL,
    seat_number VARCHAR(2) NOT NULL,
    passenger_id INT,
    route_id INT,
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id) ON DELETE CASCADE,
    FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE
);

CREATE TABLE bus_route (
    bus_id INT,
    route_id INT,
    PRIMARY KEY (bus_id, route_id),
    FOREIGN KEY (bus_id) REFERENCES buses(bus_id) ON DELETE CASCADE,
    FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE
);

