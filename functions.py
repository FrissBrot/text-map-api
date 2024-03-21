import pickle
import hashlib
import os
import heapq
from dbfunctions import db_get_shortest_path, db_save_path

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

#save data with pickle
def save_data(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

# Funktion zum Löschen des Dateiinhalts
def clear_file(filename):
    if os.path.exists(filename):
        with open(filename, 'w'):
            pass
    else: print("Die Datei existiert nicht.")
    
# Funktion zum Laden der Daten
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    else: print("Die Datei existiert nicht.")

#funktion zum Hashen von Daten
def hash(data_to_hash):
    hash_object = hashlib.sha256()
    hash_object.update(str(data_to_hash).encode('utf-8'))

    hash = hash_object.hexdigest()
    return hash

#funktion, um zu überprüfen, ob der path im cache ist
def get_shortest_path(start, target, grid, walkable_fields, boundaries):
    path = db_get_shortest_path(start, target)
    if path:
        return path
    else: 
        path = calculate_shortest_path(start, target, grid, walkable_fields, boundaries)
        return path

# Funktion zum Auffinden des kürzesten Pfads zwischen zwei Punkten auf einem Raster
def calculate_shortest_path(start, target, grid, walkable_fields, boundaries):
    def is_walkable(coord):
        return walkable_fields.get(coord, False)

    def has_boundary(coord1, coord2):
        return (coord1, coord2) in boundaries or (coord2, coord1) in boundaries

    open_list = [(0, start)]
    closed_set = set()
    came_from = {}
    g_values = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == target:
            path = []
            total_cost = 0  # Gesamtkosten des Weges
            while current in came_from:
                path.append(current)
                total_cost += walkable_fields.get(current, 0)  # Summe der Kosten
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, total_cost

        closed_set.add(current)

        for neighbor in [(current[0] + 1, current[1]), (current[0] - 1, current[1]),
                         (current[0], current[1] + 1), (current[0], current[1] - 1)]:
            if neighbor in grid and is_walkable(neighbor) and neighbor not in closed_set:
                if not has_boundary(current, neighbor):
                    tentative_g = g_values[current] + walkable_fields.get(neighbor, float('inf'))
                    if tentative_g < g_values.get(neighbor, float('inf')):
                        came_from[neighbor] = current
                        g_values[neighbor] = tentative_g
                        f_value = tentative_g + manhattan_distance(neighbor, target)
                        heapq.heappush(open_list, (f_value, neighbor))

    return None, 0  # Es konnte kein Weg gefunden werden