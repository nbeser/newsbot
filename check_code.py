from db.connection import get_connection

def db_check():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM news;")
        files = [data[0] for data in cursor.fetchall()]
        for i in files:
            print(i)
        cursor.close()
        conn.close()
    except Exception as err:
        return err
db_check()