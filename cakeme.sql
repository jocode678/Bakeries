DROP DATABASE IF EXISTS cakeme;

CREATE DATABASE cakeme;

USE cakeme;

CREATE TABLE address(
id INT PRIMARY KEY AUTO_INCREMENT,
house_number VARCHAR(10),
street VARCHAR(30),
town VARCHAR(20),
postcode VARCHAR(10) NOT NULL,
country VARCHAR(20));

INSERT INTO address (house_number, street, town, postcode, country) VALUES
("24", "Rose Street", "London", "WC2E 9EA", "UK"),
("28", "Greek Street", "London", "W1D 5DQ", "UK"),
("20", "Brewer Street", "London", "W1F 0SJ", "UK");

CREATE TABLE dietary(
id INT PRIMARY KEY AUTO_INCREMENT,
category VARCHAR(20) NOT NULL);

CREATE TABLE bakeries(
id INT PRIMARY KEY AUTO_INCREMENT,
shop_name VARCHAR(30) NOT NULL,
address_ref INTEGER,
opening_times VARCHAR(100),
phone VARCHAR(15),
website VARCHAR(50),
social_media VARCHAR(50),
dietary_ref INTEGER,
image LONGBLOB,
FOREIGN KEY (address_ref) REFERENCES address(id),
FOREIGN KEY (dietary_ref) REFERENCES dietary(id));

INSERT INTO bakeries (shop_name, address_ref, opening_times) VALUES
("Maison Bertaux", 1, "Mon-Sun: 9:30am-6pm"),
("Bageriet", 2, "Sun/Mon: closed, Tue-Fri: 10am-5:30pm, Sat: 10am-6pm"),
("Cutter & Squidge", 3, "Mon-Sun: 11am-7pm");

CREATE TABLE menu_items(
id INT PRIMARY KEY AUTO_INCREMENT,
item_name VARCHAR(20) NOT NULL,
item_type VARCHAR(20),
dietary_ref INTEGER,
FOREIGN KEY (dietary_ref) REFERENCES dietary(id));

CREATE TABLE customer_member(
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(20) NOT NULL,
user_password VARCHAR(20) NOT NULL,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL,
email VARCHAR(50),
postcode VARCHAR(10),
dietary_ref INTEGER,
favourite_ref INTEGER,
FOREIGN KEY (dietary_ref) REFERENCES dietary(id),
FOREIGN KEY (favourite_ref) REFERENCES bakeries(id));

CREATE TABLE administrator(
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(20) NOT NULL,
user_password VARCHAR(20) NOT NULL);

CREATE TABLE bakery_owner(
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(20) NOT NULL,
user_password VARCHAR(20) NOT NULL,
bakery_ref INTEGER,
FOREIGN KEY (bakery_ref) REFERENCES bakeries(id));

CREATE TABLE reviews(
id INT PRIMARY KEY AUTO_INCREMENT,
customer_ref INTEGER,
review VARCHAR(300),
stars INTEGER NOT NULL,
bakery_ref INTEGER,
image LONGBLOB,
FOREIGN KEY (bakery_ref) REFERENCES bakeries(id));