-- States table
-- Creating Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Creating Table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
) ENGINE = INNOBD;