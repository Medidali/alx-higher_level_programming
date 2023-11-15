-- script that creates the database hbtn_0d_usa and the table states

-- CREATE
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use database
USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL, `name` VARCHAR(256) NOT NULL); 
