USE HospitalDB;

# Most Consulted Doctors
SELECT Doctors.name, COUNT(Appointments.appointment_id) AS total_visits
FROM Doctors
JOIN Appointments ON Doctors.doctor_id = Appointments.doctor_id
GROUP BY Doctors.name
ORDER BY total_visits DESC;

#Total Revenue Per Month
SELECT 
    DATE_FORMAT(a.date, '%Y-%m') AS month,
    SUM(t.cost) AS total_revenue
FROM Appointments a
JOIN Treatments t ON a.patient_id = t.patient_id
GROUP BY DATE_FORMAT(a.date, '%Y-%m');

#Most Common Diseases

SELECT diagnosis, COUNT(*) AS cases
from Treatments
GROUP BY diagnosis
ORDER BY cases DESC;

#Patient Visit Frequency
SELECT p.name, COUNT(a.appointment_id) AS visit_count
FROM Patients p
JOIN Appointments a ON p.patient_id = a.patient_id
GROUP BY p.name
ORDER BY visit_count DESC;

# Doctor Performance

SELECT d.name, SUM(t.cost) AS total_revenue
FROM Doctors d
JOIN Appointments a ON d.doctor_id = a.doctor_id
JOIN Treatments t ON a.patient_id = t.patient_id
GROUP BY d.name
ORDER BY total_revenue DESC;

#Frequent Patients

SELECT p.name, SUM(t.cost) AS total_spent
FROM Patients p
JOIN Treatments t ON p.patient_id = t.patient_id
GROUP BY p.name
ORDER BY total_spent DESC
LIMIT 1;

