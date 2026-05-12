from .connection import get_connection
from .model import News
import psycopg2

class DbManager():

    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor()
    
    def save_news(self, news):
        sql = """
        INSERT INTO news (published, title, summary, link, is_shared, source, is_translated, translated_title, translated_summary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (link) DO NOTHING
        """
        if isinstance(news, News):
            news = [news]
        for new in news:
            values = (
                new.published,
                new.title,
                new.summary,
                new.link,
                new.is_shared,
                new.source,
                new.is_translated,
                new.translated_title,
                new.translated_summary
            )
            self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        except psycopg2.Error as err:
            print(err)

    def update_news():
        pass