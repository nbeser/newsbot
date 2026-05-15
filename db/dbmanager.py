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

        try:
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

        
            self.connection.commit()
            
        except psycopg2.Error as err:
            print(err)

        finally:
            self.cursor.close()
            self.connection.close()


    def insert_ai_summaries(self, summaries):
        sql = """
        UPDATE news 
        SET summary = %s, 
            is_translated = %s, 
            translated_title = %s, 
            translated_summary = %s 
        WHERE link = %s
        """
        values = []
        for item in summaries:
            is_translated = True
            value_to_append = (
                item["summary"],
                is_translated,
                item["translated_title"],
                item["translated_summary"],
                item["link"]
            )
            values.append(value_to_append)
            
        try:
            self.cursor.executemany(sql, values)
            self.connection.commit()
            
        except psycopg2.Error as err:
            print(err)

        finally:
            self.cursor.close()
            self.connection.close()