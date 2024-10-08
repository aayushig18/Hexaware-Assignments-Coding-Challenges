CREATE DATABASE HospitalManagementSystem;
USE HospitalManagementSystem;

CREATE TABLE Patients (
    patientId INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    dateOfBirth DATE,
    gender CHAR(1),
    contactNumber VARCHAR(15),
    address VARCHAR(255)
);
CREATE TABLE Doctors (
    doctorId VARCHAR(10) PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    specialization VARCHAR(100),
    contactNumber VARCHAR(15),
    address VARCHAR(255)
);
CREATE TABLE Appointments (
    appointmentId INT PRIMARY KEY,
    patientId INT FOREIGN KEY REFERENCES Patients(patientId),
    doctorId VARCHAR(10) FOREIGN KEY REFERENCES Doctors(doctorId),
    appointmentDate DATETIME,
    description VARCHAR(255)
);

INSERT INTO Patients (patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address)
VALUES 
(1, 'Aman', 'Singh', '1990-05-12', 'M', '9876543213', '123 Street A, City'),
(2, 'Nisha', 'Khan', '1985-09-21', 'F', '9876543214', '456 Street B, City'),
(3, 'Suman', 'Patel', '2000-02-15', 'F', '9876543215', '789 Street C, City');
INSERT INTO Doctors (doctorId, firstName, lastName, specialization, contactNumber, address)
VALUES 
('D001', 'Shrey', 'Gupta', 'Dentist', '9876543210', 'Block A, Clinic Center, City'),
('D002', 'Priya', 'Mehta', 'Cardiologist', '9876543211', 'Block B, Hospital Complex, City'),
('D003', 'Raj', 'Sharma', 'Orthopedic', '9876543212', 'Block C, Health Plaza, City');
INSERT INTO Appointments (appointmentId, patientId, doctorId, appointmentDate, description)
VALUES 
(1, 1, 'D001', '2024-10-09 10:30', 'Dental checkup'),
(2, 2, 'D002', '2024-10-09 14:00', 'Heart checkup'),
(3, 3, 'D003', '2024-10-10 09:00', 'Back pain consultation');

