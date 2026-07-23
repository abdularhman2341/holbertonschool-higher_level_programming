-- Create the unique_id table with a unique default ID

-- Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
