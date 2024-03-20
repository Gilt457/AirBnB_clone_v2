-- This script is used to set up a MySQL server for the project
-- Establish a project testing database named hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Generate a new user called hbnb_test with full access to the hbnb_test_db database
-- Set the password as hbnb_test_pwd if the user doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Provide the hbnb_test user with the SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Give the new user complete access to hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
