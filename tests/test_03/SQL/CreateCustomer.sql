-- Create Table
DROP  TABLE IF EXISTS customers;
CREATE TABLE customers(
	id int PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	dob DATE NOT NULL ,
	updated_at timestamp
);


