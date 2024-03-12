from functions import remove_duplicates
from dbconnection import execute_sql_query

def initialization():
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
    return walkable_fields, boundaries, ChunksRange[0], ChunksRange[1]