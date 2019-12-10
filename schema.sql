DROP TABLE if EXISTS games;

CREATE TABLE games(
	id INTEGER NOT NULL,
	game_title varchar(100) NOT NULL,
	platform varchar(100) NOT NULL,
	PRIMARY KEY (id)
);

DROP TABLE if EXISTS the_last_of_us;

CREATE TABLE lastDatabase(
	title varchar(100) NOT NULL,
	content varchar(10000) NOT NULL,
	descriptors varchar(150) NOT NULL
);
