from db.connection import get_connection
import trafilatura
import json



def data_fetch():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title, link FROM news WHERE is_translated=False LIMIT 3;")
        files = [{"title": title, "link": link} for title, link in cursor.fetchall()]
        cursor.close()
        conn.close()

        if not files:
            return []

        return files
    except Exception as err:
        print(err)
        return []

def text_extraction():
    pre_data = data_fetch()
    try:
        for i in pre_data:
            url = i["link"]
            downloaded = trafilatura.fetch_url(url)
            output = trafilatura.extract(downloaded, output_format="json", with_metadata=True)
            text = f"{json.loads(output).get('text')[:1000]}"
            i["content"] = text
        return pre_data
    except Exception as err:
        print(err)
        return []