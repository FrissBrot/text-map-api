import heapq
from flask import Flask, request, jsonify
from datainitialization import get_map
from functions import manhattan_distance
from dbfunctions import db_save_path

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    # Die Daten von der Anfrage erhalten
    data = request.get_json()

    # Überprüfen, ob die erforderlichen Felder vorhanden sind
    if 'start' in data and 'target' in data:

        start = tuple(data['start']) 
        target = tuple(data['target'])

        walkable_fields, boundaries, rangefromdb = get_map()

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
                            tentative_g = g_values[current] + 1 # Kosten von aktuellen Knoten zu Nachbarn
                            if tentative_g < g_values.get(neighbor, float('inf')):
                                came_from[neighbor] = current
                                g_values[neighbor] = tentative_g
                                f_value = tentative_g + manhattan_distance(neighbor, target)
                                heapq.heappush(open_list, (f_value, neighbor))

            return None  # Es konnte kein Weg gefunden werden

        # Definition der Liste grid unter Berücksichtigung der Begehbarkeit der Felder
        grid = [(x, y) for x in range(rangefromdb[0] + 1) for y in range(rangefromdb[1] + 1) if walkable_fields.get((x, y), False)]

        # Aufruf des A*-Algorithmus
        path = find_shortest_path(start, target, grid)
        if path:
            print("Kürzester Pfad gefunden:", path)
            db_save_path(start, target, path)
        else:
            print("Kein Pfad gefunden.")

        # Das Ergebnis als JSON zurückgeben
        return jsonify({'result': path})
    else:
        # Fehlermeldung zurückgeben, wenn nicht alle erforderlichen Felder vorhanden sind
        return jsonify({'error': 'Not all required fields provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)

