FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["sh", "-c", "gunicorn -w 1 -b 0.0.0.0:$PORT run:app"]