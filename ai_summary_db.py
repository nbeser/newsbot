from db.dbmanager import DbManager

import json

from ai.ai_preperation import text_extraction
from ai.ai_processor import summarize_article





def clean_json(text):
    text = text.strip()
    text = text.replace("```json", "").replace("```", "")
    return text


def ai_summaries():

    articles = text_extraction()

    if not articles:
        return []

    articles_text = ""

    for idx, article in enumerate(articles):

        articles_text += f"""
        ARTICLE {idx + 1}

        LINK:
        {article["link"]}

        TITLE:
        {article["title"]}

        CONTENT:
        {article["content"]}

        """

    summaries = summarize_article(articles_text)

    cleaned = clean_json(summaries)

    try:
        return json.loads(cleaned)

    except json.JSONDecodeError as e:
        print("JSON ERROR:", e)
        print(cleaned)
        return []



def app():

    summaries = ai_summaries()
    
    if not summaries:
        print("No summaries returned")
        return

    db = DbManager()

    db.insert_ai_summaries(summaries)


if __name__ == "__app__":
    app()    