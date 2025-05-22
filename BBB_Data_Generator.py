import psycopg2
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="BlockbusterBase",
    user="postgres",
    password="sql123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Generate Bulk Data
num_records = 3000

# Insert Studios
for _ in range(num_records):
    cursor.execute("""
        INSERT INTO Studios (name, founded_year, location)
        VALUES (%s, %s, %s)
    """, (fake.company(), random.randint(1900, 2023), fake.city()))

# Insert Directors
for _ in range(num_records):
    cursor.execute("""
        INSERT INTO Directors (name, birthdate, nationality)
        VALUES (%s, %s, %s)
    """, (fake.name(), fake.date_of_birth(minimum_age=25, maximum_age=80), fake.country()))

# Insert Movies
for _ in range(num_records):
    cursor.execute("""
        INSERT INTO Movies (title, genre, release_year, budget, revenue)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        fake.sentence(nb_words=3),
        random.choice(['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance', 'Thriller']),
        random.randint(1950, 2023),
        random.randint(1000000, 300000000),
        random.randint(5000000, 3000000000)
    ))

# Insert Actors
for _ in range(num_records):
    cursor.execute("""
        INSERT INTO Actors (name, birthdate, nationality)
        VALUES (%s, %s, %s)
    """, (fake.name(), fake.date_of_birth(minimum_age=18, maximum_age=80), fake.country()))

# Insert Streaming Platforms
platforms = ['Netflix', 'Amazon Prime', 'Disney+', 'HBO Max', 'Apple TV', 'Hulu']
for platform in platforms:
    cursor.execute("INSERT INTO Streaming_Platforms (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (platform,))

# Link Movies to Studios
cursor.execute("SELECT movie_id FROM Movies")
movie_ids = [row[0] for row in cursor.fetchall()]
cursor.execute("SELECT studio_id FROM Studios")
studio_ids = [row[0] for row in cursor.fetchall()]
for movie_id in movie_ids:
    cursor.execute("INSERT INTO Movie_Studios (movie_id, studio_id) VALUES (%s, %s)", (movie_id, random.choice(studio_ids)))

# Link Movies to Directors
cursor.execute("SELECT director_id FROM Directors")
director_ids = [row[0] for row in cursor.fetchall()]
for movie_id in movie_ids:
    cursor.execute("INSERT INTO Movie_Directors (movie_id, director_id) VALUES (%s, %s)", (movie_id, random.choice(director_ids)))

# Link Movies to Actors
cursor.execute("SELECT actor_id FROM Actors")
actor_ids = [row[0] for row in cursor.fetchall()]
for movie_id in movie_ids:
    for _ in range(random.randint(1, 5)):
        cursor.execute("INSERT INTO Movie_Actors (movie_id, actor_id) VALUES (%s, %s) ON CONFLICT DO NOTHING", (movie_id, random.choice(actor_ids)))

# Link Movies to Streaming Platforms
cursor.execute("SELECT platform_id FROM Streaming_Platforms")
platform_ids = [row[0] for row in cursor.fetchall()]
for movie_id in movie_ids:
    for _ in range(random.randint(1, 3)):
        cursor.execute("INSERT INTO Movie_Streaming (movie_id, platform_id) VALUES (%s, %s) ON CONFLICT DO NOTHING", (movie_id, random.choice(platform_ids)))

# Insert Reviews
for movie_id in movie_ids:
    for _ in range(random.randint(1, 5)):
        cursor.execute("""
            INSERT INTO Reviews (movie_id, rating, review_text)
            VALUES (%s, %s, %s)
        """, (movie_id, round(random.uniform(1, 10), 1), fake.sentence()))

# Insert Box Office Data
for movie_id in movie_ids:
    cursor.execute("""
        INSERT INTO Box_Office (movie_id, domestic_revenue, international_revenue)
        VALUES (%s, %s, %s)
    """, (movie_id, random.randint(1000000, 500000000), random.randint(1000000, 1500000000)))

# Insert Awards
award_names = ['Oscar', 'Golden Globe', 'BAFTA', 'Cannes', 'Critics Choice']
for movie_id in movie_ids:
    for _ in range(random.randint(0, 3)):
        cursor.execute("""
            INSERT INTO Awards (name, year, movie_id)
            VALUES (%s, %s, %s)
        """, (random.choice(award_names), random.randint(1950, 2023), movie_id))

# Commit and Close Connection
conn.commit()
cursor.close()
conn.close()

print("Database populated with large dataset successfully!")
