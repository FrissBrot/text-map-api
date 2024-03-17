from flask import Flask, request, jsonify
from datainitialization import get_map
from functions import get_shortest_path
from dbfunctions import get_coordinate_from_id

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    # Die Daten von der Anfrage erhalten
    data = request.get_json()

    # Überprüfen, ob die erforderlichen Felder vorhanden sind
    if 'start' in data and 'target' in data:

        start = get_coordinate_from_id(int(data['start']))
        target = get_coordinate_from_id(int(data['target']))

        if start == False:
            return jsonify({'result': None})

        walkable_fields, boundaries, rangefromdb = get_map()

        # Definition der Liste grid unter Berücksichtigung der Begehbarkeit der Felder
        grid = [(x, y) for x in range(rangefromdb[0] + 1) for y in range(rangefromdb[1] + 1) if walkable_fields.get((x, y), False)]

        # Aufruf des A*-Algorithmus
        path = get_shortest_path(start, target, grid, walkable_fields, boundaries)
        if path:
            print("Kürzester Pfad gefunden:", path)
        else:
            print("Kein Pfad gefunden.")

        # Das Ergebnis als JSON zurückgeben
        return jsonify({'result': path})
    else:
        # Fehlermeldung zurückgeben, wenn nicht alle erforderlichen Felder vorhanden sind
        return jsonify({'error': 'Not all required fields provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)

