import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- 1. PAGE CONFIGURATION (ELITE SETTINGS) ---
st.set_page_config(
    page_title="Keqing Wang | Executive Portfolio",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CUSTOM CSS (DARK MODE & PREMIUM UI) ---
st.markdown("""
    <style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Dark Mode Background & Global Styles */
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Custom Metric Cards */
    [data-testid="stMetricValue"] {
        color: #00b894 !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #888 !important;
        font-size: 1rem !important;
    }
    
    /* Section Headers */
    .section-header {
        color: #00b894;
        font-size: 2rem;
        font-weight: 800;
        border-bottom: 2px solid #333;
        padding-bottom: 10px;
        margin-top: 40px;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Experience Cards (Glassmorphism) */
    .exp-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .exp-card:hover {
        transform: translateY(-5px);
        border-color: #00b894;
    }
    
    /* Custom Buttons */
    .stButton>button {
        background-color: #00b894 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        background-color: #00d1a0 !important;
        box-shadow: 0 4px 15px rgba(0, 184, 148, 0.4) !important;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #1a1a1a !important;
        border-right: 1px solid #333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATA PREPARATION ---
# Skills Data for Radar Chart
radar_data = pd.DataFrame({
    'Metric': ['Data Science', 'Finance', 'Engineering', 'Leadership', 'Strategy', 'Analytics'],
    'Value': [95, 92, 85, 90, 88, 94]
})

# Technical Stack for Bar Chart
tech_stack = pd.DataFrame({
    'Technology': ['Python', 'SQL', 'AWS', 'Tableau', 'Power BI', 'PySpark', 'NLP', 'Excel/VBA'],
    'Proficiency': [98, 95, 82, 90, 88, 85, 80, 96]
}).sort_values('Proficiency', ascending=True)

# Experience Data for Filtering
experience_data = [
    {"Year": 2024, "Role": "Data Science Intern", "Company": "IG Wealth Management", "Domain": "Data Science", "Details": "Merged 10M+ data points using Vertex AI & BigQuery. Built 5 ETL pipelines."},
    {"Year": 2024, "Role": "Data Analyst Intern", "Company": "ICBC", "Domain": "Finance", "Details": "Built logistic regression risk model. Automated reporting, saving 6 hours daily."},
    {"Year": 2023, "Role": "Investment Analyst Intern", "Company": "CITIC Securities", "Domain": "Finance", "Details": "Analyzed 1,000+ industry peers using PySpark. Identified operational risks."},
    {"Year": 2022, "Role": "Wealth Management Intern", "Company": "BMO", "Domain": "Finance", "Details": "Analyzed client portfolios using Power BI. Increased accuracy by 30%."}
]

# --- 4. HEADER SECTION ---
col_h1, col_h2 = st.columns([2, 1])
with col_h1:
    st.markdown("# KEQING (KATHERINE) WANG")
    st.markdown("### *Master of Management Analytics Candidate | Data Strategy Expert*")
    st.markdown("---")
    st.write("Expert in risk assessment, predictive modeling, and ETL pipeline engineering. Proven track record of handling 10M+ data points and delivering 92% precision in fraud detection.")

with col_h2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.metric("GPA", "3.75 / 4.0", delta="Honors")
    st.metric("Data Scale", "10M+ Points", delta="Big Data")

# --- 5. INTERACTIVE WIDGETS (SIDEBAR) ---
st.sidebar.title("💎 EXECUTIVE CONTROLS")
st.sidebar.markdown("---")

# Widget 1: Multi-select (Filter Roles)
selected_domains = st.sidebar.multiselect(
    "Filter Experience by Domain",
    options=["Data Science", "Finance"],
    default=["Data Science", "Finance"]
)

# Widget 2: Slider (Filter Years)
year_range = st.sidebar.slider(
    "Select Timeline Range",
    min_value=2022, max_value=2024, value=(2022, 2024)
)

# Widget 3: Checkbox (Show Technical Details)
show_details = st.sidebar.checkbox("Reveal Technical Deep-Dive", value=False)

st.sidebar.markdown("---")
st.sidebar.info("📧 keke.wang@rotman.utoronto.ca\n\n📍 Toronto, Canada")

# --- 6. DATA VISUALIZATION SECTION ---
st.markdown('<div class="section-header">Competency & Tech Stack</div>', unsafe_allow_html=True)
col_v1, col_v2 = st.columns(2)

with col_v1:
    # Plotly Radar Chart (Requirement: Radar/Line)
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=radar_data['Value'],
        theta=radar_data['Metric'],
        fill='toself',
        name='Competency',
        line_color='#00b894',
        fillcolor='rgba(0, 184, 148, 0.3)'
    ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color="#888", gridcolor="#333"),
            angularaxis=dict(color="#e0e0e0", gridcolor="#333"),
            bgcolor="rgba(0,0,0,0)"
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=450,
        margin=dict(t=40, b=40, l=40, r=40)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

with col_v2:
    # Plotly Bar Chart (Requirement: Bar Chart)
    fig_bar = px.bar(
        tech_stack, 
        x='Proficiency', y='Technology',
        orientation='h',
        color='Proficiency',
        color_continuous_scale=['#1a1a1a', '#00b894'],
        template="plotly_dark"
    )
    fig_bar.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=False,
        xaxis=dict(showgrid=False, range=[0, 100]),
        yaxis=dict(showgrid=False),
        height=450
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# --- 7. PROFESSIONAL EXPERIENCE (FILTERED) ---
st.markdown('<div class="section-header">Professional Journey</div>', unsafe_allow_html=True)

filtered_exp = [
    e for e in experience_data 
    if e['Domain'] in selected_domains and year_range[0] <= e['Year'] <= year_range[1]
]

if not filtered_exp:
    st.warning("No experiences match the selected filters.")
else:
    for exp in filtered_exp:
        st.markdown(f"""
        <div class="exp-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h3 style="color: #00b894; margin: 0;">{exp['Role']}</h3>
                <span style="background: #333; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem;">{exp['Year']}</span>
            </div>
            <h4 style="color: #888; margin-top: 5px;">{exp['Company']}</h4>
            <p style="margin-top: 15px; color: #ccc;">{exp['Details'] if show_details else "Click 'Reveal Technical Deep-Dive' in sidebar for details."}</p>
        </div>
        """, unsafe_allow_html=True)

# --- 8. DATA PRESENTATION (PANDAS STYLER TABLE) ---
st.markdown('<div class="section-header">Academic & Leadership Honors</div>', unsafe_allow_html=True)

honors_df = pd.DataFrame({
    "Achievement": ["Dean’s Honour List", "First-Class Scholarship", "Portfolio Simulation", "ETC Investment Club"],
    "Recognition": ["Academic Excellence", "$5,000 Award", "1st Place Winner", "President/Lead"],
    "Year": ["2022-2025", "2024", "2024", "2023-2025"],
    "Impact": ["Top 5% of Class", "Merit-based", "Outperformed 15 teams", "Led 100+ members"]
})

# Pandas Styler (Requirement: Formatted Table)
styled_df = honors_df.style.set_properties(**{
    'background-color': '#1a1a1a',
    'color': '#e0e0e0',
    'border-color': '#333'
}).set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#00b894'), ('color', 'white'), ('font-weight', 'bold')]},
    {'selector': 'tr:hover', 'props': [('background-color', '#252525')]}
]).hide(axis="index")

st.table(styled_df)

# --- 9. FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #555; font-size: 0.8rem; border-top: 1px solid #333; padding-top: 20px;">
        Designed by Manus Elite Dev Team for Keqing Wang | Built with Streamlit & Plotly
    </div>
    """, unsafe_allow_html=True)
