import json
import os
from collections import defaultdict

download_folder = "temp_download"
filaments_file = os.path.join(download_folder, "filaments.json")
mapping_file = os.path.join(download_folder, "id_mapping.json")

if not os.path.exists(filaments_file):
    print(f"Datei {filaments_file} nicht gefunden.")
    exit(1)

with open(filaments_file, "r", encoding="utf-8") as f:
    data = json.load(f)

id_to_items = defaultdict(list)
for item in data:
    id_to_items[item.get("id")].append(item)

duplicates = [items for items in id_to_items.values() if len(items) > 1]

mapping_entries = []
for items in duplicates:
    for entry in items:
        mapping_entries.append({
            "id": entry.get("id"),
            "name": entry.get("name"),
            "material": entry.get("material"),
            "manufacturer": entry.get("manufacturer"),
            # Optional: weitere Felder ergänzen
            "weight": entry.get("weight"),
            "color_hex": entry.get("color_hex"),
            "density": entry.get("density"),
            "diameter": entry.get("diameter")
        })

with open(mapping_file, "w", encoding="utf-8") as f:
    json.dump(mapping_entries, f, ensure_ascii=False, indent=2)

print(f"{len(mapping_entries)} doppelte IDs wurden in {mapping_file} exportiert.")
