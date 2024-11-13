FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
EXPOSE 5000

# Använd PORT-miljövariabeln från Azure om den finns, annars port 5000
CMD ["sh", "-c", "python -m http.server ${PORT:-5000}"]

