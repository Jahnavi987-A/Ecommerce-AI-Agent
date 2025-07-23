import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_sql(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that writes SQLite SQL queries. "
                        "Note:\n"
                        "- SQLite does not support MONTH() or YEAR().\n"
                        "- Use strftime('%m', date_column) and strftime('%Y', date_column) instead.\n"
                        "- Use CURRENT_DATE or date('now') for current date operations.\n"
                        "- The ad_sales table has these columns: date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold.\n"
                        "- Use 'date' as the date column in ad_sales table.\n"
                        "- Always return only the SQL query without markdown or explanation."
                    )
                },
                {"role": "user", "content": question}
            ]
        )

        raw_sql = response.choices[0].message.content.strip()
        # Remove code blocks or extra formatting
        cleaned_sql = re.sub(r"```.*?\n|```", "", raw_sql, flags=re.DOTALL).strip()
        return cleaned_sql

    except Exception as e:
        return f"OpenRouter API Error: {e}"
