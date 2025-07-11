import requests
import json
import os

mapping_file = os.path.join(download_folder, "id_mapping.json")

# URLs der Dateien
url_original = "https://colonel302.github.io/SpoolmanDB-Multi/en/filaments.json"
url_de = "https://colonel302.github.io/SpoolmanDB-Multi/de/filaments.json"

download_folder = "temp_download"
os.makedirs(download_folder, exist_ok=True)

def download_json(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    filepath = os.path.join(download_folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return data

# Felder für den Vergleich
MATCH_FIELDS = ["manufacturer", "material", "color_hexes", "color_hex", "extruder_temp", "weight", "diameter", "spool_weight", "spool_type", "finish", "density", "translucent", "glow", "extruder_temp", "bed_temp"]

def make_key(item):
    key = []
    for field in MATCH_FIELDS:
        value = item.get(field)
        # Falls Wert eine Liste ist, in ein Tupel umwandeln (hashbar)
        if isinstance(value, list):
            value = tuple(value)
        key.append(value)
    return tuple(key)


# Download der Dateien
data_original = download_json(url_original, "original_filaments.json")
data_de = download_json(url_de, "de_filaments.json")

# Mapping: Key (technische Merkmale) -> id aus Originaldatei
lookup_original = {}
for item in data_original:
    key = make_key(item)
    lookup_original[key] = item.get("id")

# IDs in der übersetzten Datei ersetzen
count_replaced = 0
count_unmatched = 0
for item in data_de:
    key = make_key(item)
    if key in lookup_original:
        old_id = item.get("id")
        new_id = lookup_original[key]
        if old_id != new_id:
            item["id"] = new_id
            count_replaced += 1
    else:
        count_unmatched += 1

# Prüfen, ob Mapping-Datei existiert, sonst anlegen
if not os.path.exists(mapping_file):
    example_mapping = [
        {"name": "Weiß", "material": "PLA", "manufacturer": "extrudr", "id": "extrudr_pla_white"},
        {"name": "Transparent", "material": "PLA", "manufacturer": "extrudr", "id": "extrudr_pla_transparent"}
    ]
    with open(mapping_file, "w", encoding="utf-8") as f:
        json.dump(example_mapping, f, ensure_ascii=False, indent=2)
    print(f"Mapping-Datei wurde neu angelegt unter: {mapping_file}. Bitte ergänze die IDs und Werte nach Bedarf.")
    exit(0)

# Mapping-Datei laden
with open(mapping_file, "r", encoding="utf-8") as f:
    id_mapping = json.load(f)

# Hilfsstruktur für schnellen Zugriff: (name, material, manufacturer) -> id
mapping_by_key = {
    (entry["name"], entry["material"], entry["manufacturer"]): entry["id"]
    for entry in id_mapping
}

# IDs anhand der Mapping-Datei setzen (überschreiben)
count_mapping_replaced = 0
for item in data_de:
    key = (item.get("name"), item.get("material"), item.get("manufacturer"))
    if key in mapping_by_key:
        old_id = item.get("id")
        new_id = mapping_by_key[key]
        if old_id != new_id:
            item["id"] = new_id
            count_mapping_replaced += 1

print(f"{count_mapping_replaced} IDs wurden anhand der id_mapping.json überschrieben.")

# Speichern der korrigierten Datei
corrected_path = os.path.join(download_folder, "filaments.json")
with open(corrected_path, "w", encoding="utf-8") as f:
    json.dump(data_de, f, ensure_ascii=False, indent=2)

print(f"Fertig! {count_replaced} IDs wurden ersetzt. {count_unmatched} Einträge konnten nicht gematcht werden.")
print(f"Die korrigierte Datei liegt unter: {corrected_path}")
