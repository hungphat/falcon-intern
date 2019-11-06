-- Create Table
DROP  TABLE IF EXISTS customers;
CREATE TABLE customers(
	id int PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	birth DATE NOT NULL ,
	update_at timestamp
);


