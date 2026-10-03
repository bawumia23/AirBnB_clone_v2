-- Prepares a MySQL server for the dev environment of the AirBnB clone
-- project: creates the hbnb_dev_db database and the hbnb_dev user,
-- then grants that user the privileges the application needs.
-- Safe to run multiple times: every statement is idempotent.

-- Create the development database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the hbnb_dev user (localhost only) if it does not already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant hbnb_dev full privileges, but only on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant hbnb_dev read-only access to performance_schema, needed by
-- some tooling/tests, and nothing beyond SELECT
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the privilege changes immediately
FLUSH PRIVILEGES;
