-- Prepares a MySQL server for the project test environment

-- Creates the database hbnb_test_db if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates the user hbnb_test with password hbnb_test_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grants SELECT privilege on performance_schema to hbnb_test
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Flushes privileges to apply changes immediately
FLUSH PRIVILEGES;
