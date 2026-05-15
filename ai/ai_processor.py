from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def summarize_article(articles_text):

    prompt = f"""
    Summarize each article in JSON format. Be direct and do not show emotional and/or political tendency. 
    After you summarized, translate title and summary into Turkish language. Add translated title into translated_title, summary into translated_summary.

    Example:
    [
    {{
        "title": "...",
        "translated_title": "...",
        "link": "...",
        "summary": "..."
        "translated_summary": "..."
    }}
    ]

    Articles:
    {articles_text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text