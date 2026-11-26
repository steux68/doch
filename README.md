# DOCH! Deutsche Grammatik

Lern-App (PWA) zur deutschen Grammatik. Live: https://steux68.github.io/doch/

Eine Datei `index.html`, Symbole und `manifest.webmanifest`. Die Patch-Skripte in `src/` stammen aus dem früheren Ordner `deutsch/` im Repo Dressuraufgaben (Pfad dort `deutsch/index.html`; hier liegt die Datei im Hauptordner).

## Versions-Check (seit 26.11.2026)
Die App prüft beim Öffnen nur `version.txt` (eine Zeile). Nach jeder Änderung von `<meta name="app-version">` in `index.html`: `python3 src/version_sync.py`, sonst erkennen installierte Apps die neue Version nicht.
