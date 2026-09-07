import requests
from dotenv import load_dotenv
import os

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")


def send_to_telegram(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, json=payload, timeout=45)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.Timeout:
        print("Telegram request timed out. The server took too long to respond.")
        return {"ok": False, "error": "Timeout"}
        
    except requests.exceptions.RequestException as e:
        print(f"A network error occurred: {e}")
        return {"ok": False, "error": str(e)}