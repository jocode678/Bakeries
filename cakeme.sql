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
("20", "Brewer Street", "London", "W1F 0SJ", "UK"),
("279", "Grays Inn Road", "London", "WC1X 8QF", "UK"),
("1", "Kingly Ct, Carnaby St", "London", "W1B 5PW", "UK"),
("57", "Warren St", "London", "W1T 5NR", "UK"),
("76", "Landor Road", "London", "SW9 9PH", "UK"),
("396", "Mentmore Terrace", "London", "E8 3PH", "UK"),
("385", "Geffrye St", "London", "E2 8HZ", "UK"),
("115", "Queensway", "London", "W2 4SJ", "UK");


CREATE TABLE dietary(
id INT PRIMARY KEY AUTO_INCREMENT,
category VARCHAR(30) NOT NULL);

INSERT INTO dietary (category) VALUES ("gluten free and coeliac"), ("dairy free and lactose free"), ("vegetarian"), ("vegan"), ("peanut free"), ("soy free"), ("eggs free"), ("fish and shellfish free"), ("kosher"), ("halal");

CREATE TABLE bakeries(
id INT PRIMARY KEY AUTO_INCREMENT,
shop_name VARCHAR(30) NOT NULL,
address_ref INTEGER NOT NULL,
opening_times VARCHAR(100),
phone VARCHAR(15),
website VARCHAR(50),
social_media VARCHAR(50),
image longblob,
gluten VARCHAR(5),
dairy_lactose VARCHAR(5),
vegetarian VARCHAR(5),
vegan VARCHAR(5),
peanut VARCHAR(5),
soy VARCHAR(5),
eggs VARCHAR(5),
fish_shell VARCHAR(5),
kosher VARCHAR(5),
halal VARCHAR(5),
FOREIGN KEY (address_ref) REFERENCES address(id));

INSERT INTO bakeries (image, shop_name, address_ref, opening_times, website, gluten, dairy_lactose, vegetarian, vegan, peanut, soy, eggs, fish_shell, kosher, halal) VALUES
("images/bakeries/maisonbertaux.jpg", "Maison Bertaux", 1, "Mon-Sun: 9:30am-6pm", "http://www.maisonbertaux.com/", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No"),
("\Bakeries\cakemeapp\application\static\images\bakeries\bageriet.jpg", "Bageriet", 2, "Sun/Mon: closed, Tue-Fri: 10am-5:30pm, Sat: 10am-6pm", "https://www.bageriet.co.uk/", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No"),
("\Bakeries\cakemeapp\application\static\images\bakeries\cutterandsquidge.PNG", "Cutter & Squidge", 3, "Mon-Sun: 11am-7pm", "https://cutterandsquidge.com/", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No"),
("\Bakeries\cakemeapp\application\static\images\bakeries\auxpainsdepapy.PNG", "Aux Pains de Papy", 4, "Mon-Fri: 7am-4pm, Sat: 8am-12pm, Sun: closed", "https://www.auxpainsdepapy.co.uk/", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No"),
("\Bakeries\cakemeapp\application\static\images\bakeries\crumbsanddoilies.jpg", "Crumbs & Doilies", 5, "Mon-Sat: 11am-7pm, Sun: 12-6pm", "https://www.crumbsanddoilies.co.uk/", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No"),
("\Bakeries\cakemeapp\application\static\images\bakeries\mielbakery.jpg", "Miel Bakery", 6, "Mon-Sun: 8am-6pm", "http://oldpostofficebakery.co.uk/,", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No"),
("images/bakeries/theoldpostofficebakery.jpg", "The Old Post Office Bakery", 7, "Mon-Sat: 7am-4pm, Sun: 7am-2pm", "http://oldpostofficebakery.co.uk/", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No"),
("\Bakeries\cakemeapp\application\static\images\bakeries\e5bakehouse.jpg", "E5 Bakehouse", 8, "Mon-Fri: 7:30am-4:30pm, Sat/Sun: 8am-5pm", "https://e5bakehouse.com/", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No"),
("\Bakeries\cakemeapp\application\static\images\bakeries\fabriquebakeryhoxton.jpg", "Fabrique Bakery Hoxton", 9, "Mon-Fri: 8am-5pm, Sat/Sun: 9am-6pm", "https://fabrique.co.uk/", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No"),
("\Bakeries\cakemeapp\application\static\images\bakeries\granierbakerycafe.jpg", "Granier Bakery Cafe", 10, "Mon-Sun: 6am-9pm", "https://pansgranier.com/", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No");

CREATE TABLE menu_items(
id INT PRIMARY KEY AUTO_INCREMENT,
item_name VARCHAR(20) NOT NULL,
item_type VARCHAR(20),
dietary_ref INTEGER,
FOREIGN KEY (dietary_ref) REFERENCES dietary(id));

INSERT INTO menu_items (item_name, item_type) VALUES
("victoria sponge cake", "sponge cake"),
("chocolate cake", "sponge cake"),
("angel cake", "sponge cake"),
("lemon tart", "tart"),
("raspberry tart", "tart");

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

INSERT INTO customer_member (username, user_password, first_name, last_name, email, postcode) VALUES
("user1", "password1", "Betty", "Smith", "betty.smith@email.com", "E6 5TA"),
("user2", "password2", "Rachel", "Jane", "rachel.jane@email.com", "E2 0QL"),
("user3", "password3", "Ryan", "Black", "ryan.black@email.com", "NW9 6PN");

CREATE TABLE administrator(
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(20) NOT NULL,
user_password VARCHAR(20) NOT NULL);

INSERT INTO administrator (username, user_password) VALUES ("admin1", "password1");

CREATE TABLE bakery_owner(
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(20) NOT NULL,
user_password VARCHAR(20) NOT NULL,
bakery_ref INTEGER,
FOREIGN KEY (bakery_ref) REFERENCES bakeries(id));

INSERT INTO bakery_owner (username, user_password, bakery_ref) VALUES 
("baker1", "password1", 1),
("baker2", "password2", 2);

CREATE TABLE reviews(
id INT PRIMARY KEY AUTO_INCREMENT,
review VARCHAR(300),
stars INTEGER NOT NULL,
bakery_ref INTEGER NOT NULL,
image LONGBLOB, 
FOREIGN KEY (bakery_ref) REFERENCES bakeries(id));

INSERT INTO reviews (review, stars, bakery_ref) VALUES
("Quite tasty pastries!", 5, 7);

-- CREATE USER "admin2"@"localhost" IDENTIFIED BY "password2";
-- GRANT ALL ON cakeme.* TO "admin2"@"localhost";

-- CREATE USER "baker1"@"localhost" IDENTIFIED BY "password1";
-- GRANT SELECT, INSERT, UPDATE ON cakeme.bakeries TO "baker1"@"localhost";

-- CREATE SCHEMA permissions;
-- SELECT schema();

-- CREATE FUNCTION dbo.fn_cakemeaccess (@id AS sysname)
-- RETURNS TABLE
-- WITH SCHEMABINDING
-- AS
-- RETURN SELECT 1 AS AccessRight
-- 	WHERE @id = USER_NAME() OR USER_NAME() = "baker1"
-- ;

select * from bakeries;