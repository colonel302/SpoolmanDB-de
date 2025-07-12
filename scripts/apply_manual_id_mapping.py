import json
import os

download_folder = "temp_download"
temp_file = os.path.join(download_folder, "temp_filaments.json")
mapping_file = os.path.join(download_folder, "id_mapping_manual.json")
final_file = os.path.join(download_folder, "filaments.json")

# Felder für die Zuordnung
MAPPING_FIELDS = ["name", "material", "manufacturer", "diameter", "weight", "density", "color_hex", "spool_type"]

if not os.path.exists(temp_file):
    print(f"Temporäre Datei nicht gefunden: {temp_file}")
    exit(1)

with open(temp_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Mapping laden (falls vorhanden)
if os.path.exists(mapping_file):
    with open(mapping_file, "r", encoding="utf-8") as f:
        manual_mapping = json.load(f)
else:
    manual_mapping = []

# Hilfsstruktur für schnellen Zugriff, nur plastic/cardboard
mapping_by_key = {
    tuple(entry.get(field) for field in MAPPING_FIELDS): entry["id"]
    for entry in manual_mapping
    if entry.get("spool_type") in ("plastic", "cardboard")
}

count_mapped = 0

for item in data:
    # Nur plastic/cardboard mappen
    if item.get("spool_type") not in ("plastic", "cardboard"):
        continue
    key = tuple(item.get(field) for field in MAPPING_FIELDS)
    if key in mapping_by_key:
        old_id = item.get("id")
        new_id = mapping_by_key[key]
        if old_id != new_id:
            item["id"] = new_id
            count_mapped += 1

with open(final_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"{count_mapped} IDs wurden anhand der id_mapping_manual.json überschrieben (nur plastic/cardboard).")
print(f"Die finale Datei liegt unter: {final_file}")
