-- create table with default and unique values

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE default 1,
    name VARCHAR(256)
)
