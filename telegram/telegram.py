from .telegram_poster import send_to_telegram
from .telegram_preperation import data_fetch

from html import escape

import requests

import time

from db.dbmanager import DbManager

db = DbManager()




def format_message(article):

    title = escape(article["translated_title"])
    summary = escape(article["translated_summary"])

    return f"""
    <b>{title}</b>

    {summary}

    🔗 {article['link']}
    """


def telegram():
    files = data_fetch()
    # print(files)
    posted_files = []
    try:
        for i in files:
            telegram_message = format_message(i)
            send_to_telegram(telegram_message)
            posted_files.append(i["link"])
            time.sleep(2)
        print(posted_files)
        db.telegram_shared(posted_files)
    except requests.exceptions.RequestException as err:
        print(err)



if __name__ == "__telegram__":
    telegram()    