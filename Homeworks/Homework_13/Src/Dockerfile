FROM python:3.11-slim

WORKDIR /app

COPY Students.csv app.py requirements.txt results.txt test_requests.py /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
