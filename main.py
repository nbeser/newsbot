# 1 > feeds_db: gets new news and adds them into db
# 2 > ai_summary_db: gets main text [:1000] and sends ai. Ai summarises and translates. Then, data is sent to db. 
# 3 > telegram: it posts news on telegram of which have is_shared = False. The it updates data as is_shared = True after posting

from feeds_db import insert_news
from ai_summary_db import app
from telegram.telegram import telegram



def main():
    insert_news()
    app()
    telegram()

if __name__ == "__main__":
    main()    