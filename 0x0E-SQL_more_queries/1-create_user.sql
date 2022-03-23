-- Creates an user
-- Creating the user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Granting Privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Flushing
FLUSH PRIVILEGES;