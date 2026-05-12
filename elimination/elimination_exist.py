from db.connection import get_connection

def db_check(news_list):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT link FROM news;")
        files = [data[0] for data in cursor.fetchall()]
        filtered = [i for i in news_list if i["link"] not in files]
        cursor.close()
        conn.close()
        return filtered
    except Exception as err:
        return err