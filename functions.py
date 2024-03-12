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