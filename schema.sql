DROP TABLE if EXISTS games;

CREATE TABLE games(
	id INTEGER NOT NULL,
	game_title varchar(100) NOT NULL,
	platform varchar(100) NOT NULL,
	PRIMARY KEY (id)
);

DROP TABLE if EXISTS lastDatabase;

CREATE TABLE lastDatabase(
	title varchar(100) NOT NULL,
	content varchar(10000) NOT NULL,
	descriptors varchar(150) NOT NULL
);

DROP TABLE if EXISTS massDatabase;

CREATE TABLE massDatabase(
	title varchar(100) NOT NULL,
	content varchar(10000) NOT NULL,
	descriptors varchar(150) NOT NULL
);

DROP TABLE if EXISTS thelegendDatabase;

CREATE TABLE thelegendDatabase(
	title varchar(100) NOT NULL,
	content varchar(10000) NOT NULL,
	descriptors varchar(150) NOT NULL
);

DROP TABLE if EXISTS haloDatabase;

CREATE TABLE haloDatabase(
	title varchar(100) NOT NULL,
	content varchar(10000) NOT NULL,
	descriptors varchar(150) NOT NULL
);

DROP TABLE if EXISTS witcherDatabase;

CREATE TABLE witcherDatabase(
	title varchar(100) NOT NULL,
	content varchar(10000) NOT NULL,
	descriptors varchar(150) NOT NULL
);

DROP TABLE if EXISTS darkDatabase;

CREATE TABLE darkDatabase(
	title varchar(100) NOT NULL,
	content varchar(10000) NOT NULL,
	descriptors varchar(150) NOT NULL
);
