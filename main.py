# feeds_db  > will call news, filter and adds to db if they haven't been.
# ai_preperation > must run after feeds_db. It fetches data including link and title. Gets main text from link and returns dict as {"title": title, "link": link, "content": main_text} This data is then ready to send to ai for translation.

from feeds_db import insert_news
from ai.ai_preperation import text_extraction



from ai.ai_processor import summarize_article

articles = text_extraction()

for article in articles:

    ai_summary = summarize_article(
        article["title"],
        article["content"]
    )

    article["ai_summary"] = ai_summary

    print(article)