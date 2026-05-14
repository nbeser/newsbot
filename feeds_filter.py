import feedparser
from config.topics import TOPICS
from elimination.elimination_keys import elimination
from elimination.elimination_exist import db_check

# feeds = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")
feeds = feedparser.parse("https://feeds.bbci.co.uk/news/world/rss.xml")

def news():
    bbc = []
    for i in feeds.entries:
        new = f"Title: {i.title} Summary: {i.summary}"
        if elimination(new, TOPICS):
            bbc.append({"published": i.published, "title": i.title, "summary": i.summary, "link": i.id, "is_shared": False, "source": "bbc", "is_translated": False})
    print(bbc)
    return db_check(bbc)
