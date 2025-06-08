CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(255) NOT NULL
);

CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    specialization VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE SET NULL
);

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status VARCHAR(50) NOT NULL,
    doctor_id INT,
    patient_id INT,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE
);

INSERT INTO departments (name, location) VALUES
('Cardiology', 'Building A, Floor 2'),
('Neurology', 'Building B, Floor 3'),
('Orthopedics', 'Building C, Floor 1'),
('Pediatrics', 'Building D, Floor 4'),
('Dermatology', 'Building E, Floor 5');

INSERT INTO doctors (name, specialization, phone, department_id) VALUES
('Dr. Alice Rahman', 'Cardiologist', '01710001111', 1),
('Dr. Badrul Islam', 'Neurologist', '01710002222', 2),
('Dr. Shirin Akhter', 'Orthopedic Surgeon', '01710003333', 3),
('Dr. Farzana Yasmin', 'Pediatrician', '01710004444', 4),
('Dr. Kamrul Hasan', 'Dermatologist', '01710005555', 5);


INSERT INTO patients (name, age, gender, phone) VALUES
('Mahmud Hasan', 35, 'Male', '01820001111'),
('Sabina Khatun', 28, 'Female', '01820002222'),
('Rezaul Karim', 42, 'Male', '01820003333'),
('Nasima Begum', 15, 'Female', '01820004444'),
('Tariq Anwar', 60, 'Male', '01820005555');


INSERT INTO appointments (appointment_date, appointment_time, status, doctor_id, patient_id) VALUES
('2025-06-10', '10:00:00', 'Scheduled', 1, 1),
('2025-06-11', '11:30:00', 'Completed', 2, 2),
('2025-06-12', '09:00:00', 'Cancelled', 3, 3),
('2025-06-13', '14:00:00', 'Scheduled', 4, 4),
('2025-06-14', '15:30:00', 'Scheduled', 5, 5);
