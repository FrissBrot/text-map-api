FROM debian:latest

# Installieren von benötigten Paketen
RUN apt-get update && apt-get install -y \
    python3 \
    python3-flask \
    python3-psycopg2 \
    python3-gunicorn \
    postgresql \
    postgresql-contrib \
    wget \
    tar && \
    apt-get clean

# Arbeitsverzeichnis setzen
WORKDIR /app

# Herunterladen und Entpacken des Codes
RUN wget https://github.com/FrissBrot/text-map-api/archive/refs/tags/v0.1.2.tar.gz && \
    tar -xzf v0.1.2.tar.gz && \
    rm v0.1.2.tar.gz

# PostgreSQL-Service starten
RUN service postgresql start

# Datenbank erstellen und Backup importieren
#RUN su postgres -c "createdb EuropaparkPlanerMap" && \
#    su postgres -c "psql -d EuropaparkPlanerMap -f /app/text-map-api-0.1.2/sql/backup.sql"
