-- Creates 'second-table' and the fill it with id, names & scores.
USECREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- inserting rows
INSERT INTO 'second_table' ('id','name','score') VALUES (1, "John", 10);
INSERT INTO 'secont_table' ('id','name','score') VALUES (2, "Alex", 3);
INSERT INTO 'second_table' ('id','name','score') VALUES (3, "Bob", 14);
INSERT INTO 'second_table' ('id','name','score') VALUES (4, "George", 8);
