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
html, body {
    margin: 0 !important;
    padding: 0 !important;
}

.main .block-container {
    padding: 0 !important;
}
html { scroll-behavior: smooth; }

.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
    maxheight: 100% !important;
}

header, footer {visibility: hidden;}

[data-testid="stAppViewContainer"] {
    background: #0b1120;
}


/* ================= NAVBAR ================= */

.main > div {
    padding-top: 0rem !important;
}

[data-testid="stAppViewContainer"] {
    padding: 0 !important;
}
.navbar {
  
    top: 0;
    width: 100%;
}

.navbar {
   
    width: 100%;
    top: 0;
    z-index: 1000;
    background: rgba(11,17,32,0.95);
    backdrop-filter: blur(10px);
    padding: 18px 80px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    color: white;
    font-size: 22px;
    font-weight: 700;
}

.nav-links {
    display: flex;
}

.nav-links a {
    color: #cbd5e1;
    text-decoration: none;
    margin-left: 30px;
    font-weight: 500;
    font-size: 18px; 
    transition: 0.3s;
}

.nav-links a:hover {
    color: #38bdf8;
}



/* ================= HERO WITH BG IMAGE ================= */

.hero {
    min-height: 100vh;
    width: 100%;
    margin: 0;
    padding: 0;
    background-image: url("https://images.unsplash.com/photo-1600585154340-be6161a56a0c");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}
.hero::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6); /* Dark overlay */
}

.hero-overlay {
    position: relative;
    text-align: center;
    color: white;
    padding: 00px;
}

.hero-overlay h1 {
    font-size: 60px;
    font-weight: 800;
}



.hero-btn {
    margin-top: 10px;
    padding: 14px 40px;
    background: #38bdf8;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    color: black;
    display: inline-block;
    transition: 0.3s;
}

.hero-btn:hover {
    transform: scale(1.05);
}

/* Mobile */
@media (max-width: 900px) {

    .hero-overlay h1 {
        font-size: 36px;
    }

    .hero-overlay p {
        font-size: 18px;
    }
}


/* ================= SECTIONS ================= */


/* ================= SECTIONS ================= */



.section h2 {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    color: #38bdf8;   /* This will control heading color */
}

/* Animated underline for headings */
.section h2 {
    position: relative;
    display: inline-block;
}

.section h2::after {
    content: "";
    position: absolute;
    left: 50%;
    bottom: -10px;
    width: 0;
    height: 3px;
    background: #38bdf8;
    transition: all 0.4s ease;
    transform: translateX(-50%);
}

.section h2:hover::after {
    width: 80%;
}

/* Cards */
.card-container {
    display: flex;
    justify-content: center;
    gap: 40px;
    flex-wrap: wrap;
    margin-top: 60px;
}

.card {
    background: linear-gradient(145deg,#1e293b,#111827);
    padding: 30px;
    border-radius: 15px;
    width: 300px;
    transition: 0.3s;
    text-align: center;
    border: 1px solid rgba(56,189,248,0.15);
}

.card h3 {
    color: #38bdf8;
    font-weight: 700;
    margin-bottom: 15px;
}

.card p {
    color: #d1d5db;
    font-size: 15px;
    line-height: 1.6;
}

.card {
    transition: all 0.4s ease;
}

.card:hover {
    transform: translateY(-12px) scale(1.02);
    box-shadow: 0 25px 50px rgba(56,189,248,0.35);
    border: 1px solid #38bdf8;
}


/* Prediction */



.stButton>button {
    background: #38bdf8;
    color: blue;
    font-weight: 600;
    border-radius: 10px;
    width: 100%;
}

.result-card {
    margin-top: 30px;
    padding: 25px;
    background: linear-gradient(135deg,#38bdf8,#0ea5e9);
    border-radius: 15px;
    font-size: 26px;
    font-weight: 700;
    color: black;
}

/* Responsive */
@media (max-width: 900px) {

    .hero h1 { font-size: 36px; }

    .section { padding: 60px 20px; }

    .predict-box { padding: 30px; }
}
.section-dark h2 {
    background: linear-gradient(90deg,#38bdf8,#0ea5e9) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    opacity: 1 !important;
}

/* Fade-in animation */
@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.section {
    animation: fadeUp 1s ease;
}

.contact-box {
    max-width: 500px;
    margin: 30px auto;   
    background: linear-gradient(145deg,#1e293b,#111827);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid rgba(56,189,248,0.2);
    transition: 0.4s ease;
}

.contact-box p {
    color: #d1d5db;
    font-size: 18px;
    margin: 15px 0;
}

.contact-box:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(56,189,248,0.3);
}
/* ================= CLEAN FOOTER ================= */

.footer {
    margin-top: 6px;
    text-align: center;
}

.footer p {
    color: #94a3b8;
    font-size: 14px;
    margin: 6px 0;
}

.footer p:first-child {
    color: #38bdf8;
    font-weight: 600;
}
/* Change input label color */
label {
    color: #38bdf8 !important;
    font-weight: 600 !important;
}

/* ================= MOBILE FIX ================= */

@media (max-width: 768px) {

    [data-testid="column"] {
        width: 100% !important;
        flex: 100% !important;
        padding: 0 !important;
    }

    h2 {
        font-size: 32px !important;
    }

    .stNumberInput, .stSlider {
        width: 100% !important;
    }

    .hero-overlay h1 {
        font-size: 28px !important;
    }
}
</style>
""", unsafe_allow_html=True)
# ================= NAVBAR =================
# ================= NAVBAR =================

# ================= NAVBAR =================
# ================= NAVBAR =================

st.markdown("""
<style>
.top-nav {
    width: 100%;
    background: rgba(11,17,32,0.95);
    padding: 18px 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(56,189,248,0.2);
    margin-bottom: 30px;
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
    transition: 0.3s ease;
}

.top-nav a:hover {
    color: #38bdf8;
}
</style>

<div class="top-nav">
    <div class="logo">🏠 House Predictor</div>
    <div>
        <a href="#insights">Insights</a>
        <a href="#predict">Prediction</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero">
    <div class="hero-overlay">
        <h1>USA House Price Prediction</h1>
        <p>AI-powered real estate valuation system using machine learning</p>
        <a href="#predict" class="hero-btn">Start Prediction</a>
    </div>
</div>
""", unsafe_allow_html=True)
# ================= INSIGHTS =================
st.markdown('<div id="insights" class="section section-dark">', unsafe_allow_html=True)

st.markdown("""
<h2 style="color:#38bdf8; font-size:40px; font-weight:500;">
Market Insights
</h2>

<div class="card-container">
    <div class="card">
        <h3>📈 Growth Trend</h3>
        <p>Strong long-term appreciation in urban regions.</p>
    </div>
    <div class="card">
        <h3>💰 Income Factor</h3>
        <p>Median income significantly impacts property prices.</p>
    </div>
    <div class="card">
        <h3>🏠 Property Age</h3>
        <p>Newer properties generally command higher prices.</p>
    </div>
</div>
</div>
""", unsafe_allow_html=True)

# ================= PREDICTION =================
# ================= PREDICTION =================
st.markdown("""
<h2 style="
text-align:left;
font-size:40px;
font-weight:400;
color:#38bdf8;
margin:10px auto 30px auto;
margin-top: 30px;
padding:0;
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
        options=["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"],
        index=3
    )

if st.button("Predict Price"):
    try:
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
        st.markdown(f'<div class="result-card">Predicted Price: ${prediction:,.2f}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

# ================= CONTACT =================
st.markdown('<div id="contact" class="section section-dark">', unsafe_allow_html=True)

st.markdown("""
<h2 style="color:#38bdf8; font-size:40px; font-weight:500;">
Contact
</h2>

<div class="contact-box">
    <p>📧 <strong>Email:</strong> amanparashar.ai@gmail.com</p>
    <p>📞 <strong>Phone:</strong> +91 98765 43210</p>
    <p>🌍 <strong>Location:</strong> India</p>
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <p>© 2026 Aman Kumar | USA House Price Prediction</p>
</div>
""", unsafe_allow_html=True)