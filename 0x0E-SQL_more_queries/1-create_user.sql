-- script that creates the MySQL server user user_0d_1.
-- Check if user_0d_1 already exists, if not, create the user
CREATE user IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to user_0d_
GRANT ALL PRIVELEDGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
