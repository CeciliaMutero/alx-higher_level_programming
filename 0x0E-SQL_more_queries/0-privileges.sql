-- script that lists all privileges of the MySQL users user_0d_1 and user_0d_2
SELECT * FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';
SELECT * FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost';
