🏡 HomeScope — AI-Powered Housing Intelligence Platform

An end-to-end data engineering + AI analytics system that ingests housing and macroeconomic data, computes affordability metrics, and generates AI-driven insights using Claude.

🚀 Overview

HomeScope is a full-stack data platform that analyzes housing affordability trends across U.S. ZIP codes by combining:

📊 Housing datasets (rent, income, home prices)
📡 FRED API mortgage rate data
🧠 AI-powered insights (Claude)
📈 Interactive Streamlit dashboard

It simulates a real-world data product pipeline used in fintech, proptech, and analytics platforms.

🧱 Architecture
FRED API + Housing Data
        ↓
   ETL Pipeline (Python)
        ↓
 PostgreSQL Database
        ↓
 Analytics Layer (Affordability Metrics)
        ↓
 Streamlit Dashboard
        ↓
 Claude AI Insight Engine 🤖
⚙️ Features
📡 Data Engineering
Automated ingestion from FRED API (mortgage rates)
Housing dataset processing (rent, income, home prices)
PostgreSQL warehouse integration
📊 Analytics Engine
Affordability index computation
Rent-to-income ratio modeling
Time-series ZIP-level analysis
🤖 AI Insights (Claude)
Automated housing trend analysis
Risk detection (affordability stress signals)
Natural language economic summaries
📈 Dashboard
ZIP code selector
Affordability trend visualization
Rent vs income comparison
Raw data explorer
AI insights panel
🛠 Tech Stack
Python
Pandas
PostgreSQL
SQLAlchemy
Streamlit
Plotly
Claude API (Anthropic)
FRED API
dotenv
🧪 How to Run
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run full pipeline
python main.py

# 3. Launch dashboard
python -m streamlit run app/dashboard.py
📊 Example Output
Affordability trends by ZIP code
Mortgage rate impact over time
Income vs rent divergence analysis
AI-generated housing market insights
🧠 Claude Insight Example

“ZIP 30040 shows improving affordability due to stagnant rent growth despite rising income levels. However, mortgage rate volatility introduces medium-term risk to housing accessibility.”

🔥 Key Highlights
End-to-end data pipeline (API → Warehouse → Analytics → UI)
AI integration for real-world decision support
Modular, production-style architecture
Designed as a scalable housing intelligence system
📁 Project Structure
homescope-platform/
│
├── app/                  # Streamlit dashboard
├── src/
│   ├── pipelines/        # ETL + analytics
│   ├── services/         # API integrations (FRED, Claude)
│   ├── core/             # schema/contracts
│   ├── jobs/             # ingestion jobs
│
├── data/
├── main.py
├── run_pipeline.py
├── requirements.txt
└── README.md
🚀 Future Improvements
Multi-city comparison dashboard
Real-time streaming ingestion
Deployment (Streamlit Cloud / AWS)
Forecasting model for affordability trends
