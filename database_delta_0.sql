drop table if exists Movie;

create table Movie(
	movie_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(50),
    movie_format ENUM('VHS', 'DVD', 'Streaming'),
    length INT,
    release_year INT,
    rating INT,
    PRIMARY KEY ( movie_id )
);