-- script that creates the MySQL server user user_0d_1.
CREATE user IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVELEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
