-- script that lists all privileges of the MySQL users user_0d_1 and user_0d_2
USE mysql;
SELECT * FROM user  WHERE user  = 'user_0d_1';
SELECT *FROM user WHERE user = 'user_0d_2';
