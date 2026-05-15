from db.dbmanager import DbManager

import json

from ai.ai_preperation import text_extraction
from ai.ai_processor import summarize_article

insert_ai_summaries = DbManager()

def ai_summaries():

    articles = text_extraction()

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

    return json.loads(clean_json(summaries))



def clean_json(text):
    text = text.strip()
    text = text.replace("```json", "").replace("```", "")
    return text



def app():

    summaries = ai_summaries()
    # print("TYPE:", type(summaries))
    # print("FIRST ITEM:", summaries[0])
    db = DbManager()

    db.insert_ai_summaries(summaries)


if __name__ == "__app__":
    app()    