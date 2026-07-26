use ecom;
-- SELECT * FROM clients;

INSERT INTO clients ( name, email, age, phone, is_active, signup_date, created_at, total_spent )
VALUES
('Amit Sharma', 'amit@gmail.com', 28, '9893179723', TRUE, '2025-01-10', '2025-01-10 10:30:00', 289283),
('Shubham Sharma', 'shuham@gmail.com', 25, '6293179723', TRUE, '2025-10-08', '2025-10-08 15:37:00', 2848238),
('Ankit Pandey', 'ankit@gmail.com', 23, '6205323586', TRUE, '2025-12-23', '2025-12-23 04:45:54', 10291008),
('Aditya Pandey', 'aditya@gmail.com', 22, '7903050471', FALSE, '2026-03-10', '2026-03-10 10:30:50', 10939373);
