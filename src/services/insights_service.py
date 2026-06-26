import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def generate_housing_insight(df):
    """
    Takes affordability dataframe and returns AI explanation
    """

    sample = df.tail(15).to_dict(orient="records")

    prompt = f"""
You are a senior housing market analyst.

Analyze this affordability dataset:

{sample}

Return:
1. Key trend in housing affordability
2. What is driving changes (rent, income, mortgage rate)
3. A simple explanation for non-technical users
4. One actionable insight for policymakers or renters
"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=600,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text