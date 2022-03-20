--
-- Creating database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creating User2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Granting Privileges
GRANT SELECT ON hbtn_0d_2* TO 'user_0d_2'@'localhost';