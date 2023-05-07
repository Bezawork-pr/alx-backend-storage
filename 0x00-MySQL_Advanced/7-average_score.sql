-- Write a SQL script that creates a stored procedure
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser(
IN user_id INT
)
BEGIN
	SELECT AVG(corrections.score) INTO @my_var
	FROM corrections
	JOIN users
       	ON users.id = corrections.user_id
	WHERE users.id = user_id;
	UPDATE users SET average_score = @my_var WHERE users.id = user_id;
END;
|
