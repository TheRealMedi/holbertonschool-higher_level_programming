-- CA Cities
-- Select cities where state_id corresponds to name 'california'
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'california') ORDER BY id ASC;