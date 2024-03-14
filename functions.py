import pickle
import hashlib
import os

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
