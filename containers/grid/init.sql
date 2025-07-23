```sql
CREATE DATABASE IF NOT EXISTS selfconcept;

USE selfconcept;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- testing data
INSERT INTO users (username, email, password)
VALUES 
  ('admin', 'admin@example.com', '$2y$10$ZZZzzZzzzzZZZzz.zzZZzZuzzzz.zzZzZZzZzZZzZzZzZzZzZzZ'), -- bcrypt
  ('test', 'test@example.com', '$2y$10$abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabca'); -- bcrypt
