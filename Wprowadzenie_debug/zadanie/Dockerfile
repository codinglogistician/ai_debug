FROM python:3.10-slim

WORKDIR /app

# Zainstaluj zależności systemowe (ffmpeg potrzebny do audio)
RUN apt-get update && apt-get install -y ffmpeg git && rm -rf /var/lib/apt/lists/*

# Zainstaluj wymagane biblioteki
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj aplikację
COPY . app/

# Uruchom Gradio
CMD ["python", "app.py"]
