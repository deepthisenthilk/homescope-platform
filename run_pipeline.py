from src.pipelines.analytics import build_affordability_table
from src.services.insights_service import generate_housing_insight


def run_all():
    print("\n🚀 HOME-SCOPE PIPELINE STARTING\n")

    # -----------------------------------
    # STEP 1: INGESTION (handled elsewhere)
    # -----------------------------------
    print("📡 Step 1: Ingestion assumed completed via control center / job")

    # -----------------------------------
    # STEP 2: ANALYTICS
    # -----------------------------------
    print("\n📊 Step 2: Building affordability analytics...")

    df = build_affordability_table()

    print("✅ Analytics completed successfully")

    # -----------------------------------
    # STEP 3: CLAUDE AI INSIGHTS
    # -----------------------------------
    print("\n🤖 Step 3: Generating Claude insights...\n")

    try:
        insight = generate_housing_insight(df)
        print(insight)
    except Exception as e:
        print("⚠️ Claude insight failed:", str(e))


# ---------------------------
# CLI ENTRY POINT
# ---------------------------
if __name__ == "__main__":
    run_all()