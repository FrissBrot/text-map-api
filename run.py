import heapq
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

#dupplikate aus einer Liste entfernen
def remove_duplicates(arr):
    unique_pairs = set()
    result = []
    
    for pair in arr:
        pair = tuple(sorted(pair))  # Sortiere die Koordinaten, um die Reihenfolge zu normalisieren
        if pair not in unique_pairs:
            unique_pairs.add(pair)
            result.append(pair)
    
    return result

# Funktion zur Berechnung der Manhattan-Distanz zwischen zwei Punkten
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# Funktion zum Auffinden des kürzesten Pfads zwischen zwei Punkten auf einem Raster
def find_shortest_path(start, target, grid):
    # Funktion zur Überprüfung der Begehbarkeit eines Feldes
    def is_walkable(coord):
        return walkable_fields.get(coord, False)

    # Funktion zur Überprüfung, ob eine Grenze zwischen zwei Feldern existiert
    def has_boundary(coord1, coord2):
        return (coord1, coord2) in boundaries or (coord2, coord1) in boundaries

    # Initialisierung der offenen Liste und der geschlossenen Liste
    open_list = [(0, start)]  # Prioritätswarteschlange, die die Knoten basierend auf ihrem f-Wert enthält
    closed_set = set()  # Menge, die die bereits untersuchten Knoten enthält
    came_from = {}  # Dictionary zur Nachverfolgung des Weges
    g_values = {start: 0}  # Dictionary zur Verfolgung der g-Werte

    # A*-Algorithmus
    while open_list:
        _, current = heapq.heappop(open_list)  # Entferne den Knoten mit dem niedrigsten f-Wert aus der Warteschlange

        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        closed_set.add(current)

        for neighbor in [(current[0] + 1, current[1]), (current[0] - 1, current[1]),
                         (current[0], current[1] + 1), (current[0], current[1] - 1)]:
            if neighbor in grid and is_walkable(neighbor) and neighbor not in closed_set:
                if not has_boundary(current, neighbor):  # Überprüfung, ob es eine Grenze zwischen current und neighbor gibt
                    tentative_g = g_values[current] + 1  # Kosten von aktuellen Knoten zu Nachbarn
                    if tentative_g < g_values.get(neighbor, float('inf')):
                        came_from[neighbor] = current
                        g_values[neighbor] = tentative_g
                        f_value = tentative_g + manhattan_distance(neighbor, target)
                        heapq.heappush(open_list, (f_value, neighbor))

    return None  # Es konnte kein Weg gefunden werden

#Auslesen des Rasters aus der DB
query = "SELECT x, y FROM \"map\".chunks ORDER BY X, y ASC;"
response  = execute_sql_query(query)
response_array = []
for entry in response:
    response_array.append(list(entry))
    
ChunksRange = response_array[(len(response_array) - 1)]

# Definition des Rasters und der Begehbarkeit der Felder
walkable_fields = {(x, y): True for x in range(ChunksRange[0]) for y in range(ChunksRange[1])}

#Felder welche nicht begehbar sind aus detenbank auslesen
query = "SELECT x, y FROM \"map\".chunks WHERE json_array_length(borders_on) = 0;"
response  = execute_sql_query(query)
response_array = []
for entry in response:
    response_array.append(list(entry))

for chunk in response_array:
    walkable_fields[tuple(chunk)] = False


# Definition der Grenzen zwischen den Feldern
boundaries = []
query = "SELECT x, y, borders_on, id FROM \"map\".chunks WHERE json_array_length(borders_on) > 0;"
response  = execute_sql_query(query)
response_array = []
for entry in response:
    response_array.append(list(entry))

for entry in response_array:
    neighbors = []

    # Nachbarfelder hinzufügen, wobei Koordinaten die nicht existieren ignoriert werden
    if entry[0] - 1 >= 0 and entry[0] - 1 <= ChunksRange[0]:
        neighbors.append((entry[0] - 1, entry[1]))  # Links
    if entry[0] + 1 >= 0 and entry[0] + 1 <= ChunksRange[0]:
        neighbors.append((entry[0] + 1, entry[1]))  # Rechts
    if entry[1] - 1 >= 0 and entry[0] - 1 <= ChunksRange[1]:
        neighbors.append((entry[0], entry[1] - 1))  # Oben
    if entry[1] + 1 >= 0 and entry[0] + 1 <= ChunksRange[1]:
        neighbors.append((entry[0], entry[1] + 1))  # Unten
    
    neighborIDS = []
    for chunk in neighbors:
        query = "SELECT id FROM \"map\".chunks WHERE x = {} AND y = {};".format(chunk[0], chunk[1])
        response  = execute_sql_query(query)
        for IDentry in response:
            neighborIDS.append(list(IDentry))
    

    # Flach machen der verschachtelten Liste neighborIDS
    flattened_neighborIDS = [item for sublist in neighborIDS for item in sublist]
    border_int = [int(x) for x in entry[2]]

    for neighbor in flattened_neighborIDS:
        if neighbor not in border_int:
            query = "SELECT x, y FROM \"map\".chunks WHERE id = {};".format(neighbor)
            response = execute_sql_query(query)
            # Stellen Sie sicher, dass response eine Liste enthält, bevor Sie sie mit anderen Listen verknüpfen
            if response:
                # Extrahieren Sie die Koordinaten aus der Datenbankabfrage
                coordinates_from_response = (response[0][0], response[0][1])
                # Koordinaten aus entry[0] und entry[1]
                coordinates_from_entry = (entry[0], entry[1])
                # Fügen Sie die Koordinaten in das gewünschte Format hinzu
                boundaries.append((coordinates_from_entry, coordinates_from_response))  

#Liste aufräumen und alle Duplikate enfernen
boundaries = remove_duplicates(boundaries)

# Definition der Liste grid unter Berücksichtigung der Begehbarkeit der Felder
grid = [(x, y) for x in range(10) for y in range(10) if walkable_fields.get((x, y), False)]

# Beispielanwendung des A*-Algorithmus
start = (3, 6)
target = (6, 5)

path = find_shortest_path(start, target, grid)
if path:
    print("Kürzester Pfad gefunden:", path)
else:
    print("Kein Pfad gefunden.")
