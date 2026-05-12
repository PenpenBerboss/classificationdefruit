# Dockerfile
# Couche 1 : image de base Python legere
FROM python:3.11-slim
# Repertoire de travail dans le conteneur
WORKDIR /app
# Couche 2 : dependances ( copiees AVANT le code )
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --default-timeout=300 --no-cache-dir -r requirements.txt
# Couche 3 : code applicatif
COPY . .
# Port expose
EXPOSE 8000
# Demarrage (${ PORT : -8000} pour Cloud Run )
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}