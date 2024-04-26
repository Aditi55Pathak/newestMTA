CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE IF NOT EXISTS mytable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO mytable (name) VALUES ('John'), ('Alice'), ('102');
INSERT INTO mytable (name) VALUES ('Aditi'), ('Pathak'), ('105');
INSERT INTO mytable (name) VALUES ('Aanya'), ('Malhotra'), ('106');
INSERT INTO mytable (name) VALUES ('Avani'), ('chaturvedi'), ('1109');
