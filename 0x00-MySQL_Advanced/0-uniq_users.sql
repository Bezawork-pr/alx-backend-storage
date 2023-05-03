-- Create table
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email Varchar(255) NOT NULL UNIQUE,
	name Varchar(255)
);
