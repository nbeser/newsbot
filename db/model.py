class News:

    def __init__(self, published, title, summary, link, is_shared, source, is_translated, translated_title=None, translated_summary=None, id=None):
        
        self.id = id
        self.published = published
        self.title = title
        self.summary = summary
        self.link = link
        self.is_shared = is_shared
        self.source = source
        self.is_translated = is_translated
        self.translated_title = translated_title
        self.translated_summary = translated_summary
    
    @staticmethod
    def createNews(obj):
        liste = []
        if isinstance(obj, dict):
            obj = [obj]
        for i in obj:
            liste.append(News(
                id=None,
                published=i.get("published"),
                title=i.get("title"),
                summary=i.get("summary", None),
                link=i.get("link"),
                is_shared=i.get("is_shared", False),
                source=i.get("source"),
                is_translated=i.get("is_translated")
            ))
        return liste