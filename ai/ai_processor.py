from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def summarize_article(title, content):

    prompt = f"""
    You are a news analyst.

    Summarize this news article in 2 concise sentences. Be direct and do not show emotional and/or political tendency.

    TITLE:
    {title}

    ARTICLE:
    {content}

    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text