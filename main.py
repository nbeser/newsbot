# feeds_db  > will call news, filter and adds to db if they haven't been.
# ai_preperation > must run after feeds_db. It fetches data including link and title. Gets main text from link and returns dict as {"title": title, "link": link, "content": main_text} This data is then ready to send to ai for translation.

from feeds_db import insert_news
from ai.ai_preperation import text_extraction
from ai.ai_processor import summarize_article

def main():

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

    print(summaries)


if __name__ == "__main__":
    main()
