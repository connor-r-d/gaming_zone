DROP TABLE if EXISTS games;

CREATE TABLE games(
	id INTEGER NOT NULL,
	game_title varchar(100) NOT NULL,
	platform varchar(100) NOT NULL,
	PRIMARY KEY (id)
);
