FROM python:latest

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir python-dotenv discord.py Pillow

CMD ["python3", "Bot.py"] 