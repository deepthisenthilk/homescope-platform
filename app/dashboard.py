import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from anthropic import Anthropic

# -----------------------------
# CONFIG
# -----------------------------
load_dotenv()

engine = create_engine(
    "postgresql://homescope_user:homescope_pass@localhost:5432/homescope"
)

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

st.set_page_config(page_title="HomeScope Dashboard", layout="wide")

st.title("🏡 HomeScope Housing Intelligence Dashboard")


# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_sql("SELECT * FROM housing_affordability", engine)
    df["date"] = pd.to_datetime(df["date"])
    return df


df = load_data()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
zip_codes = df["zip_code"].unique()
selected_zip = st.sidebar.selectbox("Select ZIP Code", zip_codes)

filtered = df[df["zip_code"] == selected_zip]

# -----------------------------
# METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Avg Rent", f"${filtered['median_rent'].mean():,.0f}")
col2.metric("Avg Income", f"${filtered['median_income'].mean():,.0f}")
col3.metric("Affordability Index", f"{filtered['affordability_index'].mean():.2f}")

# -----------------------------
# CHART 1: AFFORDABILITY TREND
# -----------------------------
fig1 = px.line(
    filtered,
    x="date",
    y="affordability_index",
    title="Affordability Trend Over Time"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# CHART 2: RENT VS INCOME
# -----------------------------
fig2 = px.bar(
    filtered,
    x="date",
    y=["median_rent", "median_income"],
    barmode="group",
    title="Rent vs Income"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# RAW DATA
# -----------------------------
st.subheader("📊 Raw Data")
st.dataframe(filtered)


# -----------------------------
# CLAUDE INSIGHTS PANEL
# -----------------------------
st.subheader("🤖 Claude Housing Insights")

if st.button("Generate Insight"):

    prompt = f"""
    You are a housing data analyst.

    Analyze this dataset for ZIP code {selected_zip}:

    {filtered.to_string(index=False)}

    Provide:
    1. Key trend insight
    2. Any affordability risks
    3. One actionable recommendation
    Keep it concise.
    """

    with st.spinner("Claude is analyzing..."):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=500,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

    st.write(response.content[0].text)