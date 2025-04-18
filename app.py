import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px


st.set_page_config(page_title="BlockbusterBase Dashboard", layout="wide", page_icon="🎬")
st.markdown("<h1 style='text-align: center; color: #D63384;'>🎬 BlockbusterBase: Hollywood Analytics</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Dive deep into the data behind blockbuster movies</p>", unsafe_allow_html=True)
st.markdown("---")


@st.cache_resource
conn = psycopg2.connect(
    host=st.secrets["postgres"]["host"],
    port=st.secrets["postgres"]["port"],
    database=st.secrets["postgres"]["database"],
    user=st.secrets["postgres"]["user"],
    password=st.secrets["postgres"]["password"]
)

def run_query(query):
    return pd.read_sql(query, conn)


col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Top 10 Grossing Movies")
    df1 = run_query("""
        SELECT m.title, (b.domestic_revenue + b.international_revenue) AS total_revenue
        FROM Movies m
        JOIN Box_Office b ON m.movie_id = b.movie_id
        ORDER BY total_revenue DESC LIMIT 10
    """)
    fig1 = px.bar(df1, x='total_revenue', y='title', orientation='h', color='total_revenue',
                  color_continuous_scale='Viridis', labels={"total_revenue": "Revenue ($)"})
    st.plotly_chart(fig1, use_container_width=True)
    st.caption("Franchise films dominate revenue charts — sequels rule the box office.")

with col2:
    st.subheader("🎭 Genre Popularity")
    df2 = run_query("SELECT genre, COUNT(*) AS count FROM Movies GROUP BY genre ORDER BY count DESC")
    fig2 = px.pie(df2, values='count', names='genre', hole=0.4,
                  color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("Action and Drama are the dominant genres in our dataset.")

col3, col4 = st.columns(2)

with col3:
    st.subheader("🎬 Movies Released Over Time")
    df3 = run_query("SELECT release_year, COUNT(*) AS count FROM Movies GROUP BY release_year ORDER BY release_year")
    fig3 = px.area(df3, x='release_year', y='count', line_shape="spline", color_discrete_sequence=['#1f77b4'])
    st.plotly_chart(fig3, use_container_width=True)
    st.caption("A major surge post-2000s suggests the rise of digital platforms and streaming.")

with col4:
    st.subheader("📊 Avg Revenue per Genre")
    df4 = run_query("""
        SELECT genre, ROUND(AVG(b.domestic_revenue + b.international_revenue)) AS avg_revenue
        FROM Movies m JOIN Box_Office b ON m.movie_id = b.movie_id
        GROUP BY genre ORDER BY avg_revenue DESC
    """)
    fig4 = px.bar(df4, x='genre', y='avg_revenue', color='avg_revenue',
                  color_continuous_scale='Teal', labels={'avg_revenue': 'Average Revenue'})
    st.plotly_chart(fig4, use_container_width=True)
    st.caption("Sci-Fi and Action films tend to generate the highest average revenue.")


col5, col6 = st.columns(2)

with col5:
    st.subheader("🎬 Most Prolific Directors")
    df5 = run_query("""
        SELECT d.name, COUNT(*) AS count
        FROM Directors d JOIN Movie_Directors md ON d.director_id = md.director_id
        GROUP BY d.name ORDER BY count DESC LIMIT 10
    """)
    fig5 = px.bar(df5, x='count', y='name', orientation='h', color='count', color_continuous_scale='Bluered')
    st.plotly_chart(fig5, use_container_width=True)
    st.caption("These directors have consistently worked on major productions.")

with col6:
    st.subheader("🏢 Top Movie Studios")
    df6 = run_query("""
        SELECT s.name, COUNT(*) AS count
        FROM Studios s JOIN Movie_Studios ms ON s.studio_id = ms.studio_id
        GROUP BY s.name ORDER BY count DESC LIMIT 10
    """)
    fig6 = px.bar(df6, x='count', y='name', orientation='h', color='count', color_continuous_scale='Sunset')
    st.plotly_chart(fig6, use_container_width=True)
    st.caption("Top studios dominate production volume across years.")


col7, col8 = st.columns(2)

with col7:
    st.subheader("📺 Streaming Platform Coverage")
    df7 = run_query("""
        SELECT sp.name, COUNT(*) AS count
        FROM Streaming_Platforms sp JOIN Movie_Streaming ms ON sp.platform_id = ms.platform_id
        GROUP BY sp.name ORDER BY count DESC
    """)
    fig7 = px.pie(df7, values='count', names='name', hole=0.4, title='Movies per Platform',
                  color_discrete_sequence=px.colors.qualitative.Safe)
    st.plotly_chart(fig7, use_container_width=True)
    st.caption("Netflix and Amazon Prime lead the platform content race.")

with col8:
    st.subheader("⭐ Highest Rated Movies")
    df8 = run_query("""
        SELECT m.title, ROUND(AVG(r.rating),2) AS avg_rating
        FROM Movies m JOIN Reviews r ON m.movie_id = r.movie_id
        GROUP BY m.title ORDER BY avg_rating DESC LIMIT 10
    """)
    fig8 = px.bar(df8, x='avg_rating', y='title', orientation='h', color='avg_rating',
                  color_continuous_scale='IceFire')
    st.plotly_chart(fig8, use_container_width=True)
    st.caption("These movies earned the highest praise from viewers.")


col9, col10 = st.columns(2)

with col9:
    st.subheader("🏆 Most Award-Winning Movies")
    df9 = run_query("""
        SELECT m.title, COUNT(*) AS award_count
        FROM Movies m JOIN Awards a ON m.movie_id = a.movie_id
        GROUP BY m.title ORDER BY award_count DESC LIMIT 10
    """)
    fig9 = px.bar(df9, x='award_count', y='title', orientation='h', color='award_count',
                  color_continuous_scale='Magma')
    st.plotly_chart(fig9, use_container_width=True)
    st.caption("These movies swept awards across various festivals.")

with col10:
    st.subheader("👨‍🎤 Most Featured Actors")
    df10 = run_query("""
        SELECT a.name, COUNT(*) AS count
        FROM Actors a JOIN Movie_Actors ma ON a.actor_id = ma.actor_id
        GROUP BY a.name ORDER BY count DESC LIMIT 10
    """)
    fig10 = px.bar(df10, x='count', y='name', orientation='h', color='count',
                   color_continuous_scale='Cividis')
    st.plotly_chart(fig10, use_container_width=True)
    st.caption("Highly active actors consistently appear across genres.")


