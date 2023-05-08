-- Write a SQL script that creates a view need_meeting
CREATE VIEW need_meeting AS
SELECT *
FROM students
WHERE score < 80 AND last_meeting IS NULL OR DATEDIFF(NOW(), last_meeting) > 31;
