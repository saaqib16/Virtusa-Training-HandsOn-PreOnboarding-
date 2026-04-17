INSERT into patients values
 (1, 'Amit', 30, 'Male'),
(2, 'Priya', 25, 'Female'),
(3, 'Rahul', 40, 'Male');


INSERT into Doctors values
(101, 'Dr. Sharma', 'Cardiology'),
(102, 'Dr. Mehta', 'Orthopedics'),
(103, 'Dr. Khan', 'General');

insert into appointments values
(1, 1, 101, '2026-04-01'),
(2, 2, 103, '2026-04-02'),
(3, 1, 101, '2026-04-10'),
(4, 3, 102, '2026-04-11');

insert into treatments values
(1, 1, 'Heart Disease', 5000),
(2, 2, 'Fever', 800),
(3, 3, 'Fracture', 3000),
(4, 1, 'Checkup', 1000);

