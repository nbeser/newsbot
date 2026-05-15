# 1 > feeds_db: gets new news and adds them into db
# 2 > ai_summary_db: gets main text [:1000] and sends ai. Ai summarises and translates. Then, data is sent to db. 

from feeds_db import insert_news
from ai_summary_db import app


def main():
    insert_news()
    app()

if __name__ == "__main__":
    main()    