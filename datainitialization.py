# -*- coding: utf-8 -*-
from functions import remove_duplicates, save_data, clear_file, load_data, hash
from dbfunctions import db_clear_table, db_get_costs, get_chunk_id
from dbconnection import execute_sql_query
import os

filename = 'data.pickle'

def get_db_hash():
    #Auslesen der Updates aus der Datenbank
    query = "SELECT relname, n_tup_ins as inserts, n_tup_upd as updates, n_tup_del as deletes FROM pg_stat_all_tables WHERE relname = 'chunk';"
    response  = execute_sql_query(query)

    hash_id = hash(response)
    return hash_id

def initialization():
    print("start datainitialization ...")
    #Auslesen des Rasters aus der DB
    query = "SELECT x, y FROM \"public\".chunk ORDER BY X, y ASC;"
    response  = execute_sql_query(query)
    response_array = []
    for entry in response:
        response_array.append(list(entry))
        
    ChunksRange = response_array[(len(response_array) - 1)]

    # Definition des Rasters und der Begehbarkeit der Felder
    walkable_fields = {(x, y): db_get_costs(get_chunk_id(x, y)) for x in range(ChunksRange[0] + 1) for y in range(ChunksRange[1] + 1)}

    #Felder welche nicht begehbar sind aus detenbank auslesen
    #query = "SELECT x, y FROM \"public\".chunk WHERE jsonb_array_length(border_on) = 0;"
    #response  = execute_sql_query(query)
    #response_array = []
    #for entry in response:
    #    response_array.append(list(entry))

    #for chunk in response_array:
    #    walkable_fields[tuple(chunk)] = False


    # Definition der Grenzen zwischen den Feldern
    boundaries = []
    query = "SELECT x, y, border_on, id FROM \"public\".chunk WHERE jsonb_array_length(border_on) > 0;"
    response  = execute_sql_query(query)
    response_array = []
    for entry in response:
        response_array.append(list(entry))

    for entry in response_array:
        neighbors = []

        # Nachbarfelder hinzufügen, wobei Koordinaten die nicht existieren ignoriert werden
        if entry[0] + 1 <= ChunksRange[0]:
            neighbors.append((entry[0] + 1, entry[1]))  # Rechts
        if entry[0] - 1 >= 0:
            neighbors.append((entry[0] - 1, entry[1]))  # Links
        if entry[1] + 1 <= ChunksRange[1]:
            neighbors.append((entry[0], entry[1] + 1))  # Oben
        if entry[1] - 1 >= 0:
            neighbors.append((entry[0], entry[1] - 1))  # Links

        neighborIDS = []
        for chunk in neighbors:
            query = "SELECT id FROM \"public\".chunk WHERE x = {} AND y = {};".format(chunk[0], chunk[1])
            response  = execute_sql_query(query)
            for IDentry in response:
                neighborIDS.append(list(IDentry))
        

        # Flach machen der verschachtelten Liste neighborIDS
        flattened_neighborIDS = [item for sublist in neighborIDS for item in sublist]
        border_int = [int(x) for x in entry[2]]

        for neighbor in flattened_neighborIDS:
            if neighbor not in border_int:
                query = "SELECT x, y FROM \"public\".chunk WHERE id = {};".format(neighbor)
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

    print(walkable_fields)
    #SQL Cache Tabelle leeren
    db_clear_table("savedRoute")
    #Daten in cache speichern
    hash_id = get_db_hash()

    data_to_save = hash_id, walkable_fields, boundaries, ChunksRange

    if os.path.exists(filename):
        clear_file(filename)
    save_data(data_to_save, filename)
    return walkable_fields, boundaries, ChunksRange

def check_cache():
    if os.path.exists(filename):
        loaded_data = load_data(filename)
        hashid_cache = loaded_data[0]
        hashid_db = get_db_hash()
        if hashid_cache == hashid_db: return True
        else: return False
    else: return False

def get_map():
    if check_cache():
        loaded_data = load_data(filename)
        walkable_fields = loaded_data[1]
        boundaries = loaded_data[2]
        ChunksRange = loaded_data[3]
        return walkable_fields, boundaries, ChunksRange
    
    else: return initialization()