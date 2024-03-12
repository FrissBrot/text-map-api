import psycopg2
from config import DB_CONFIG

def execute_sql_query(query):
    conn = None
    cursor = None

    try:
        # Verbindung herstellen
        conn = psycopg2.connect(**DB_CONFIG)

        # Optional: Cursor erstellen
        cursor = conn.cursor()

        # SQL-Abfrage ausführen
        cursor.execute(query)

        # Ergebnisse abrufen
        result = cursor.fetchall()

        return result

    except (Exception, psycopg2.Error) as error:
        return None

    finally:
        # Cursor und Verbindung schließen
        try:
            if cursor:
                cursor.close()
        except psycopg2.Error as e:
            print("Fehler beim Schließen des Cursors:", e)

        try:
            if conn:
                conn.close()
        except psycopg2.Error as e:
            print("Fehler beim Schließen der Verbindung:", e)