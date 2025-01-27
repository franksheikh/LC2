/*
UPDATE <table>
SET <property> = CASE <property> (no colon)
	WHEN <property1 THEN <new_property1>
	WHEN <property2 THEN <new_property2>
END;
*/
UPDATE Salary
SET sex = CASE sex
    WHEN 'm' THEN 'f'
    WHEN 'f' THEN 'm'
END;