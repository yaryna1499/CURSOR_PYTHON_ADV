CREATE TABLE `user` (
	`ID` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`full_name` varchar(50) NOT NULL,
	`age` INT(3) NOT NULL DEFAULT '18',
	`descr` varchar(50),
	`register_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`password` VARCHAR(32) NOT NULL,
	`gender` varchar(10) NOT NULL,
	`email` varchar(10) NOT NULL UNIQUE,
	PRIMARY KEY (`ID`)
);


--to create PKs in tables below!--
CREATE TABLE `user_photo` (
	`user_ID` INT NOT NULL,
	`picture` blob NOT NULL
);

CREATE TABLE `location` (
	`user_ID` INT NOT NULL,
	`longitude` DECIMAL NOT NULL,
	`latitude` DECIMAL NOT NULL
);

CREATE TABLE `interaction` (
	`user_id_1` INT NOT NULL,
	`user_id_2` INT NOT NULL,
	`status` BOOLEAN NOT NULL DEFAULT '0',
	`matched_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`user_id_1`,`user_id_2`)
);

CREATE TABLE `message` (
	`user_id_1` BINARY NOT NULL,
	`user_id_2` BINARY NOT NULL,
	`message_text` TEXT(500) NOT NULL,
	`sent_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `user_settings` (
	`user_id` INT NOT NULL UNIQUE,
	`search_radius` INT NOT NULL,
	`preffered_gender` varchar(10) NOT NULL
);

ALTER TABLE `user_photo` ADD CONSTRAINT `user_photo_fk0` FOREIGN KEY (`user_ID`) REFERENCES `user`(`ID`);

ALTER TABLE `location` ADD CONSTRAINT `location_fk0` FOREIGN KEY (`user_ID`) REFERENCES `user`(`ID`);

ALTER TABLE `interaction` ADD CONSTRAINT `interaction_fk0` FOREIGN KEY (`user_id_1`) REFERENCES `user`(`ID`);

ALTER TABLE `interaction` ADD CONSTRAINT `interaction_fk1` FOREIGN KEY (`user_id_2`) REFERENCES `user`(`ID`);

ALTER TABLE `message` ADD CONSTRAINT `message_fk0` FOREIGN KEY (`user_id_1`) REFERENCES `interaction`(`user_id_1`);

ALTER TABLE `message` ADD CONSTRAINT `message_fk1` FOREIGN KEY (`user_id_2`) REFERENCES `interaction`(`user_id_2`);

ALTER TABLE `user_settings` ADD CONSTRAINT `user_settings_fk0` FOREIGN KEY (`user_id`) REFERENCES `user`(`ID`);






