-- Creates a table *second_table* in the database *hbtn_0c_0* in my MySQL server and add multiples rows.
-- second_table description: id INT - name VARCHAR(256) - score INT
-- The database name will be passed as an argument to the mysql command
-- If the table second_table already exists, your script should not fail
-- Not allowed to use the SELECT and SHOW statements
-- The script should create these records:
--	id = 1, name = “John”, score = 10
--	id = 2, name = “Alex”, score = 3
--	id = 3, name = “Bob”, score = 14
--	id = 4, name = “George”, score = 8

CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "JOHN", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "ALEX", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "BOB", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "GEORGE", 8);

-- alternatively: insert into second_table (id, name, scre) values (1, JOHN, 10), (2, ALEX, 3), (3, BOB, 14), (4, GEORGE, 8)
