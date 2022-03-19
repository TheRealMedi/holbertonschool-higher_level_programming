-- Creates 'second-table' and the fill it with id, names & scores.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- inserting rows
INSERT INTO second_table
VALUES (1, "Jhon", 10),
        (2, "Alex", 3),
        (3, "Bob", 14),
        (4, "George", 8);