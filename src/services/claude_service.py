import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def explain_affordability(df):
    """
    Takes a pandas dataframe and returns Claude insights
    """

    sample_data = df.tail(15).to_dict(orient="records")

    prompt = f"""
You are a real estate data analyst.

Analyze this housing affordability dataset:

{sample_data}

Return:
1. Main trend (1-2 sentences)
2. Key drivers (rent, income, mortgage rate)
3. Simple explanation for a non-technical user
"""

    response = client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text