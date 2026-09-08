import os
from celery import Celery
from main import main

# Redis 
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

# Celery 
celery_app = Celery('newsbot_tasks', broker=REDIS_URL, backend=REDIS_URL)

# Task
@celery_app.task
def run_news_pipeline_task():
    print("--- Celery Görevi Başladı: RSS Çekiliyor ve AI İle Özetleniyor ---")
    
    main()
    
    return "İşlem Tamamlandı!"