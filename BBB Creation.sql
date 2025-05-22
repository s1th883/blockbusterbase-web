-- Delete all tables 
DROP TABLE IF EXISTS Movie_Streaming;
DROP TABLE IF EXISTS Movie_Actors;
DROP TABLE IF EXISTS Movie_Directors;
DROP TABLE IF EXISTS Movie_Studios;
DROP TABLE IF EXISTS Box_Office;
DROP TABLE IF EXISTS Awards;
DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS Streaming_Platforms;
DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Actors;
DROP TABLE IF EXISTS Directors;
DROP TABLE IF EXISTS Studios;




CREATE TABLE Movies (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    release_year INT,
    budget BIGINT,
    revenue BIGINT
);

-- 2. Actors Table
CREATE TABLE Actors (
    actor_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthdate DATE,
    nationality VARCHAR(100)
);

-- 3. Directors Table
CREATE TABLE Directors (
    director_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthdate DATE,
    nationality VARCHAR(100)
);

-- 4. Studios Table
CREATE TABLE Studios (
    studio_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    founded_year INT,
    location VARCHAR(255)
);

-- 5. Box Office Table
CREATE TABLE Box_Office (
    box_office_id SERIAL PRIMARY KEY,
    movie_id INT UNIQUE,
    domestic_revenue BIGINT,
    international_revenue BIGINT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) ON DELETE CASCADE
);

-- 6. Awards Table
CREATE TABLE Awards (
    award_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    year INT,
    movie_id INT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) ON DELETE CASCADE
);

-- 7. Reviews Table
CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY,
    movie_id INT,
    rating DECIMAL(3,1) CHECK (rating BETWEEN 0 AND 10),
    review_text TEXT,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) ON DELETE CASCADE
);

-- 8. Streaming Platforms Table
CREATE TABLE Streaming_Platforms (
    platform_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

-- 9. Movie_Actors 
CREATE TABLE Movie_Actors (
    movie_id INT,
    actor_id INT,
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY (actor_id) REFERENCES Actors(actor_id) ON DELETE CASCADE
);

-- 10. Movie_Streaming 
CREATE TABLE Movie_Streaming (
    movie_id INT,
    platform_id INT,
    PRIMARY KEY (movie_id, platform_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY (platform_id) REFERENCES Streaming_Platforms(platform_id) ON DELETE CASCADE
);

-- 11. Movie_Directors 
CREATE TABLE Movie_Directors (
    movie_id INT,
    director_id INT,
    PRIMARY KEY (movie_id, director_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY (director_id) REFERENCES Directors(director_id) ON DELETE CASCADE
);

-- 12. Movie_Studios 
CREATE TABLE Movie_Studios (
    movie_id INT,
    studio_id INT,
    PRIMARY KEY (movie_id, studio_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY (studio_id) REFERENCES Studios(studio_id) ON DELETE CASCADE
);




INSERT INTO Studios (name, founded_year, location) VALUES
('Warner Bros', 1923, 'Burbank, CA'),
('Universal Pictures', 1912, 'Universal City, CA'),
('Paramount Pictures', 1912, 'Hollywood, CA');

-- Directors
INSERT INTO Directors (name, birthdate, nationality) VALUES
('Christopher Nolan', '1970-07-30', 'British-American'),
('Steven Spielberg', '1946-12-18', 'American'),
('Quentin Tarantino', '1963-03-27', 'American');

-- Movies
INSERT INTO Movies (title, genre, release_year, budget, revenue) VALUES
('Inception', 'Sci-Fi', 2010, 160000000, 829895144),
('Jurassic Park', 'Adventure', 1993, 63000000, 1043840663),
('Pulp Fiction', 'Crime', 1994, 8000000, 214179088);

-- Movie Directors
INSERT INTO Movie_Directors (movie_id, director_id) VALUES
(1, 1), 
(2, 2), 
(3, 3); 

-- Actors
INSERT INTO Actors (name, birthdate, nationality) VALUES
('Leonardo DiCaprio', '1974-11-11', 'American'),
('Sam Neill', '1947-09-14', 'New Zealander'),
('John Travolta', '1954-02-18', 'American');

-- Movie Actors
INSERT INTO Movie_Actors (movie_id, actor_id) VALUES
(1, 1), 
(2, 2), 
(3, 3); 

-- Streaming Platforms
INSERT INTO Streaming_Platforms (name) VALUES
('Netflix'),
('Amazon Prime'),
('Disney+');

-- Movie Streaming
INSERT INTO Movie_Streaming (movie_id, platform_id) VALUES
(1, 1), 
(2, 2), 
(3, 3); 

-- Reviews
INSERT INTO Reviews (movie_id, rating, review_text) VALUES
(1, 9.0, 'A mind-bending thriller with stunning visuals.'),
(2, 8.5, 'A classic adventure with groundbreaking effects.'),
(3, 9.3, 'A masterpiece of storytelling and dialogue.');

select * from Actors;


select current_user,now()








-- Verify if all tables are dropped
SELECT tablename FROM pg_tables WHERE schemaname = 'public';

-- Query to get row count for each table
SELECT 'Movies' AS table_name, COUNT(*) FROM Movies
UNION ALL
SELECT 'Actors', COUNT(*) FROM Actors
UNION ALL
SELECT 'Directors', COUNT(*) FROM Directors
UNION ALL
SELECT 'Studios', COUNT(*) FROM Studios
UNION ALL
SELECT 'Box_Office', COUNT(*) FROM Box_Office
UNION ALL
SELECT 'Awards', COUNT(*) FROM Awards
UNION ALL
SELECT 'Reviews', COUNT(*) FROM Reviews
UNION ALL
SELECT 'Streaming_Platforms', COUNT(*) FROM Streaming_Platforms
UNION ALL
SELECT 'Movie_Actors', COUNT(*) FROM Movie_Actors
UNION ALL
SELECT 'Movie_Streaming', COUNT(*) FROM Movie_Streaming
UNION ALL
SELECT 'Movie_Directors', COUNT(*) FROM Movie_Directors
UNION ALL
SELECT 'Movie_Studios', COUNT(*) FROM Movie_Studios;

