-- create table cities referencing state_id to table states id column

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL FOREIGN KEY (states) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
)
