#!/usr/bin/python3

-- create the database hbtn_0d_usa and the table cities 
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE IF NTO EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
);