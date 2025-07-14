# SpoolmanDB-de

**SpoolmanDB mit deutscher Übersetzung**

## Projektbeschreibung

Dieses Repository enthält eine deutsche Version der SpoolmanDB-Datenbank für 3D-Druck-Filamente. 
Die Grundlage für dieses Projekt bildet die [SpoolmanDB-Multi](https://github.com/colonel302/SpoolmanDB-Multi), in der die eigentliche Übersetzung der Filamentdaten stattfindet. 
In diesem Repository werden ausschließlich die IDs der Filamente technisch getauscht, sodass eine konsistente Zuordnung zwischen den verschiedenen Sprachversionen gewährleistet wird.

**Wichtiger Hinweis:**  
Die Übersetzungen selbst werden **nicht** in diesem Repository gepflegt, sondern ausschließlich in [SpoolmanDB-Multi](https://github.com/colonel302/SpoolmanDB-Multi). 
Dieses Projekt übernimmt die ID-Anpassung und stellt die deutschsprachigen JSON-Dateien bereit.

## Funktionsweise

- Herunterladen der Original- und Übersetzungsdateien aus SpoolmanDB-Multi
- Technisches Tauschen der IDs, um eine eindeutige Zuordnung sicherzustellen
- Reporting und Mapping von doppelten IDs
- Anwendung manueller ID-Mappings, falls notwendig
- Bereitstellung der finalen Filamentdaten als JSON

Die Automatisierung erfolgt über GitHub Actions und Python-Skripte. Die wichtigsten Skripte sind:
- `change_id.py`: Tauscht die IDs anhand technischer Merkmale.
- `find_duplicates.py`: Findet und meldet doppelte IDs.
- `apply_manual_id_mapping.py`: Wendet ein manuelles Mapping an, da einige technische Merkmale bis auf den Namen identisch sind.

## Hinweise & Danksagungen

Ein besonderer Dank geht an das [Originalprojekt SpoolmanDB von Donkie](https://github.com/Donkie/SpoolmanDB), 
das als zentrale Datenbank für 3D-Druck-Filamente dient und die Basis für dieses sowie das Multi-Language-Projekt bildet.

Die Übersetzungen und die Multi-Language-Unterstützung werden im Projekt [SpoolmanDB-Multi](https://github.com/colonel302/SpoolmanDB-Multi) gepflegt. 
Dieses Repository basiert direkt auf den dort bereitgestellten Daten.

## Hinweise zur Nutzung

- Dieses Repository stellt ausschließlich die deutschsprachigen, ID-konsistenten Filamentdaten bereit.
- Für andere Sprachen oder die Pflege von Übersetzungen siehe [SpoolmanDB-Multi](https://github.com/colonel302/SpoolmanDB-Multi).
- Die technische Basis und das Datenformat stammen von [SpoolmanDB](https://github.com/Donkie/SpoolmanDB).

## Haftungsausschluss

Ich bin kein erfahrener Programmierer. Die Skripte und Automatisierungen wurden von einer KI (Perplexity AI) erstellt, von mir aber geprüft und getestet. 
Fehler oder Verbesserungsvorschläge sind jederzeit willkommen!

---

**Vielen Dank für die Nutzung und viel Spaß beim Drucken!**
