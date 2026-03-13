# 1. Utiliser une image Python légère
FROM python:3.11-slim

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier le fichier des dépendances
COPY requirements.txt .

# 4. Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier tout le reste du code du projet
COPY . .

# 6. Définir les variables d'environnement pour Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# 7. Exposer le port 5000 (celui utilisé par Flask)
EXPOSE 5000

# 8. Commande pour démarrer l'application avec Gunicorn (plus robuste pour le cloud)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run.py:app"]
