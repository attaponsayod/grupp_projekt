FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]
