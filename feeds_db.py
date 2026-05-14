from feeds_filter import news
from db.dbmanager import DbManager
from db.model import News


def insert_news():
    db = DbManager()
    data = news()
    if isinstance(data, dict):
        data = [data]
    new_objects = []
    for i in data:
        new_objects.append(
            News(
                id=None,
                published=i.get("published"),
                title=i.get("title"),
                summary=i.get("summary"),
                link=i.get("link"),
                is_shared=i.get("is_shared", False),
                source=i.get("source"),
                is_translated=i.get("is_translated", False),
                translated_title=i.get("translated_title"),
                translated_summary=i.get("translated_summary")
            )
        ) 
    db.save_news(new_objects)


# insert_news()