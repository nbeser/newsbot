from db.connection import get_connection


def data_fetch():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT translated_title, translated_summary, link FROM news WHERE is_translated=True AND is_shared=False;")
        files = [{"translated_title": translated_title, "translated_summary": translated_summary, "link": link} for translated_title, translated_summary, link in cursor.fetchall()]
        
        if not files:
            return []

        return files
    except Exception as err:
        print(err)
        return []
    
    finally:
        cursor.close()
        conn.close()