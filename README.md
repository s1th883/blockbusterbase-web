## 🎬 `BlockbusterBase` – README.md

```markdown
# 🎬 BlockbusterBase

BlockbusterBase is a Hollywood movie analytics platform designed as part of a database systems project. It provides advanced querying, visual insights, and data exploration features over a large-scale custom relational database of movies, actors, awards, and studios.

---

## 🏗️ Project Highlights

- 📊 SQL-driven insights on movies, ratings, revenue, and actors
- ⚡ Deployed using Streamlit for interactive UI
- 📈 Visualizations built using Plotly and Chart.js
- 💾 PostgreSQL backend with >30,000 rows across 10+ tables

---

## 🧩 Database Schema Includes:

- Movies, Actors, Directors
- Studios, Genres, Awards
- Crew, Locations, Box Office

---

## 📁 Features

- Search and filter movies based on custom criteria
- Get top-k actors by revenue, awards, etc.
- View actor collaborations, genre trends, and more
- Plot revenue vs rating, yearly trends, and studio impact

---

## 🚀 Tech Stack

- PostgreSQL
- Python (psycopg2, pandas)
- Streamlit
- Plotly, Chart.js
- Bootstrap for styling

---

## 🖥️ Run Locally

1. Start PostgreSQL and ensure DB is configured
2. Update DB credentials in `app.py`
3. Run:

```bash
pip install -r requirements.txt
streamlit run app.py
