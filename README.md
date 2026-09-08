# 🤖 NewsBot: AI-Powered Automated News Aggregator

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)
![Celery](https://img.shields.io/badge/Task%20Queue-Celery-green.svg)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-4169E1.svg)
![Redis](https://img.shields.io/badge/Broker-Redis-DC382D.svg)

An automated backend pipeline that aggregates RSS news feeds, processes and summarizes the content using AI models, stores structured records in PostgreSQL, and dispatches real-time updates to Telegram channels.

---

## 🏗 System Architecture & Workflow

The platform runs on a containerized environment powered by Docker Compose:

1. **Ingestion:** Continuously fetches global RSS news items.
2. **AI Summarization:** Uses AI models to generate Turkish summaries and titles.
3. **Task Queue & Scheduling:** Managed asynchronously via **Celery** with **Redis** as a message broker.
4. **Persistence:** Stores structured articles in a **PostgreSQL** relational database.
5. **Distribution:** Automatically dispatches updates via **Telegram Bot API**.

---

## 🚀 Quick Start (Dockerized)

Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.

### 1. Clone the repository
```bash
git clone [https://github.com/nbeser/newsbot.git](https://github.com/nbeser/newsbot.git)
cd newsbot

2. Configure Environment
Set up your environment variables or Database credentials as configured in docker-compose.yml

3. Run with Docker Compose
Spin up the Python worker, Redis message broker, and PostgreSQL database with a single command:
docker-compose up --build



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# NewsBot 🌍📰

A fully automated global news bot that fetches news from RSS feeds, summarizes articles using AI, translates them into Turkish, and publishes formatted posts directly to Telegram.

## Features

* Fetches news from RSS feeds (currently BBC)
* Filters and processes incoming articles
* Stores articles in PostgreSQL
* AI-powered article summarization
* Automatic Turkish translation
* Direct Telegram publishing
* JSON-based AI processing pipeline
* Scalable architecture for future integrations

---

## Demo

### Telegram Channel

👉 https://t.me/newsbot_global

---

## Screenshots

### Telegram Output

![Telegram Demo](assets/telegram_demo_1.png)
![Telegram Demo](assets/telegram_demo_2.png)
![Telegram Demo](assets/telegram_demo_3.png)

### Development Environment

![Code Environment](assets/newsbot_1.png)

---

## Tech Stack

* Python
* PostgreSQL
* RSS Feeds
* Telegram Bot API
* Gemini 2.5 Flash
* AI Summarization & Translation

---

## How It Works

```text
RSS Feed
   ↓
Article Fetching
   ↓
Filtering & Processing
   ↓
PostgreSQL Storage
   ↓
AI Summarization
   ↓
Turkish Translation
   ↓
Telegram Publishing
```

---

## Project Structure

```bash
newsbot/
│
├── config/
├── elimination/
├── db/
├── ai/
├── telegram/
├── ai_summary_db.py
├── feeds_db.py
├── main.py
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/nbeser/newsbot.git
cd newsbot
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
DB_HOST="your host"
DB_PORT="your port"
DB_NAME="your database name"
DB_USER="your database user"
DB_PASSWORD="your database password"

GEMINI_API_KEY="your key"

CHANNEL_ID="your telegram channel id"
BOT_TOKEN="your telegram bot token"
```

---

🛠 Tech Stack
Language: Python 3.11

Database: PostgreSQL (with Auto-schema initialization)

Task Automation: Celery & Redis

Containerization: Docker & Docker Compose

Notification System: Telegram Bot API


### Future Improvements

* One article → one AI request
* Markdown (.md) article formatting
* Multi-language support
* Twitter/X integration
* Web dashboard
* Categorization & analytics
* AI SKILLS pipeline

---

## Scalability

The infrastructure is designed for expansion and continuous execution.

Possible future integrations:

* Multiple RSS providers
* Real-time analytics
* Web interface
* Queue systems
* Multi-platform publishing


---

## Author


Nurettin Beşer - [https://www.instagram.com/zcodingsolutions/](https://www.instagram.com/zcodingsolutions/)

Project Link: [https://github.com/nbeser/newsbot/](https://github.com/nbeser/newsbot/)


Contributer : [https://github.com/nbeser](https://github.com/nbeser)

Linkedin : [https://www.linkedin.com/in/nurettin-beser-arcnbsr23](https://www.linkedin.com/in/nurettin-beser-arcnbsr23)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
