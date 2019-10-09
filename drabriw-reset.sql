USE drabriw;

CREATE TABLE drinks(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL);

CREATE TABLE person (
	id INT PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	id_fav_drink INT,
	FOREIGN KEY id_fav_drink REFERENCES drinks(id)
);

CREATE TABLE rounds(
	id INT PRIMARY KEY AUTO_INCREMENT,
	initiator_id INT NOT NULL,
	active TINYINT(1) DEFAULT 1,
	FOREIGN KEY initiator_id REFERENCES person(id)
);

CREATE TABLE rounds_users(
	round_id INT NOT NULL,
	person_id INT NOT NULL,
	drinks_id INT,
	FOREIGN KEY round_id REFERENCES rounds(id),
	FOREIGN KEY person_id REFERENCES person(id),
	FOREIGN KEY drinks_id REFERENCES drinks(id)
);
