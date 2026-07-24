-- List all cities of California without using JOIN

-- Display California cities ordered by city ID
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;
