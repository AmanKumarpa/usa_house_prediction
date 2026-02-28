import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(layout="wide", page_title="USA House Price Predictor")

# ================= LOAD MODEL =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))

# ================= GLOBAL CSS =================
st.markdown("""
<style>
html { scroll-behavior: smooth; }

[data-testid="stAppViewContainer"] {
    background: #0b1120;
}

/* NAVBAR */
.top-nav {
    width: 100%;
    background: rgba(11,17,32,0.95);
    padding: 18px 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(56,189,248,0.2);
}

.top-nav .logo {
    color: white;
    font-size: 22px;
    font-weight: 700;
}

.top-nav a {
    color: #cbd5e1;
    text-decoration: none;
    margin-left: 30px;
    font-size: 16px;
}

.top-nav a:hover {
    color: #38bdf8;
}

/* HERO */
.hero {
    min-height: 100vh;
    background-image: url("https://images.unsplash.com/photo-1600585154340-be6161a56a0c");
    background-size: cover;
    background-position: center;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero::before {
    content: "";
    position: absolute;
    width:100%;
    height:100%;
    background: rgba(0,0,0,0.6);
}

.hero-overlay {
    position: relative;
    color: white;
    text-align:center;
}

.hero-btn {
    padding:14px 40px;
    background:#38bdf8;
    border-radius:8px;
    text-decoration:none;
    font-weight:600;
    color:black;
}
</style>
""", unsafe_allow_html=True)

# ================= NAVBAR =================
st.markdown("""
<div class="top-nav">
    <div class="logo">🏠 House Predictor</div>
    <div>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#insights">Insights</a>
        <a href="#predict">Prediction</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= HOME =================
st.markdown("""
<div id="home" class="hero">
    <div class="hero-overlay">
        <h1>USA House Price Prediction</h1>
        <p>AI-powered real estate valuation system using machine learning</p>
        <a href="#predict" class="hero-btn">Start Prediction</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= ABOUT (FIXED) =================
st.markdown("""
<div id="about" style="padding:60px; color:white;">
    <h2 style="color:#38bdf8;">About This Project</h2>
    <div style="
        max-width:900px;
        margin:auto;
        background:rgba(30,41,59,0.6);
        padding:40px;
        border-radius:20px;
        border:1px solid rgba(56,189,248,0.3);
        color:#d1d5db;
    ">
        This project uses Machine Learning to predict house prices
        based on geographical and socio-economic factors.

        <br><br>

        Built with Python, Scikit-learn, and deployed as an interactive
        web application, it demonstrates a complete ML workflow —
        from data preprocessing to model deployment.
    </div>
</div>
""", unsafe_allow_html=True)

# ================= INSIGHTS =================
st.markdown("""
<div id="insights" style="padding:60px; color:white;">
<h2 style="color:#38bdf8;">Market Insights</h2>
<p>Strong long-term appreciation in urban regions.</p>
</div>
""", unsafe_allow_html=True)

# ================= PREDICTION (FIXED) =================
st.markdown("""
<h2 id="predict" style="
text-align:left;
font-size:40px;
color:#38bdf8;
margin-top:70px;
">
Prediction Model
</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    longitude = st.number_input("Longitude", value=-122.23)
    housing_median_age = st.slider("Housing Median Age", 1, 100, 41)
    total_bedrooms = st.number_input("Total Bedrooms", value=129)

with col2:
    latitude = st.number_input("Latitude", value=37.88)
    total_rooms = st.number_input("Total Rooms", value=880)
    households = st.number_input("Households", value=126)

with col3:
    population = st.number_input("Population", value=322)
    median_income = st.number_input("Median Income", value=8.32)
    ocean_proximity = st.selectbox(
        "Ocean Proximity",
        ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
    )

if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Price: ${prediction:,.2f}")

# ================= CONTACT =================
st.markdown("""
<div id="contact" style="padding:60px; color:white;">
<h2 style="color:#38bdf8;">Contact</h2>
<p>📧 amanparashar.ai@gmail.com</p>
<p>📞 +91 98765 43210</p>
</div>
""", unsafe_allow_html=True)