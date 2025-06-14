FROM python:latest

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir python-dotenv discord.py Pillow

ADD Bot.py .
ADD AuroraToolbox.py .
ADD .env .

VOLUME [ "/_media" ]

CMD ["python3", "Bot.py"] 