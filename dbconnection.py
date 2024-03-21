# -*- coding: utf-8 -*-
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

def execute_sql_insert(query):
    conn = None
    cursor = None

    try:
        # Verbindung herstellen
        conn = psycopg2.connect(**DB_CONFIG)

        # Optional: Cursor erstellen
        cursor = conn.cursor()

        # SQL-Abfrage ausführen
        cursor.execute(query)

        # Transaktion bestätigen
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print("Fehler beim Ausführen der SQL-Abfrage:", error)

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


def test_connection(query):
    conn = None
    cursor = None

    try:
        # Verbindung herstellen
        conn = psycopg2.connect(**DB_CONFIG)
        print("Verbindung erfolgreich hergestellt")

        # Optional: Cursor erstellen
        cursor = conn.cursor()

        # SQL-Abfrage ausführen
        cursor.execute(query)

        # Ergebnisse abrufen
        result = cursor.fetchall()

        return result

    except (Exception, psycopg2.Error) as error:
        print("Fehler beim Herstellen der Verbindung zur PostgreSQL-Datenbank:", error)
        return None

    finally:
        # Cursor und Verbindung schließen
        try:
            if cursor:
                cursor.close()
                print("Cursor geschlossen")
        except psycopg2.Error as e:
            print("Fehler beim Schließen des Cursors:", e)

        try:
            if conn:
                conn.close()
                print("Verbindung geschlossen")
        except psycopg2.Error as e:
            print("Fehler beim Schließen der Verbindung:", e)

print(test_connection("SELECT * FROM \"public\".chunk;"))