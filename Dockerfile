FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
EXPOSE 443

# Start a simple HTTP server to serve static files
CMD ["python", "-m", "http.server", "443"]
