-- script that creates a table second_tables

-- CREATETABLE
CREATE TABLE IF NOT EXISTS second_table (`id` INT, `name` VARCHAR(256), `score` INT);
-- insertrecord
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'BOB', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
