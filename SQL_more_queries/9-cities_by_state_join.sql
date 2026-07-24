-- List all cities with their corresponding state names

-- Display city IDs, city names, and state names ordered by city ID
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
