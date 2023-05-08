-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users,
    		(SELECT users.id, SUM(corrections.score * projects.weight) / SUM(projects.weight) AS average_score
    		FROM users
    		JOIN corrections ON corrections.user_id=users.id
    		JOIN projects ON projects.id=corrections.project_id GROUP BY users.id) AS query_result
    	SET users.average_score=query_result.average_score
 	WHERE users.id=query_result.id;
END;
|


