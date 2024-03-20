-- This script is designed to set up a MySQL server for the project
-- Establish a development database for the project named 'hbnb_dev_db'
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Set up a new user called 'hbnb_dev' with full access to the 'hbnb_dev_db' database
-- Assign the password 'hbnb_dev_pwd' if this user doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Give the new user all rights to the new database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Provide the 'hbnb_dev' user with the SELECT privilege on the 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
