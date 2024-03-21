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

        if result:
            return "Verbindung zur Datenbank erfolgreich hergestellt."

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

def table_exists(table_name):
    conn = psycopg2.connect(**DB_CONFIG)
    """
    Überprüft, ob die angegebene Tabelle in der Datenbank existiert.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s)", (table_name,))
    exists = cursor.fetchone()[0]
    cursor.close()
    return exists

def execute_sql_script(sql_file):
    conn = psycopg2.connect(**DB_CONFIG)
    """
    Führt ein SQL-Skript aus.
    """
    cursor = conn.cursor()
    with open(sql_file, 'r') as file:
        sql_script = file.read()
        cursor.execute(sql_script)
    conn.commit()
    cursor.close()
