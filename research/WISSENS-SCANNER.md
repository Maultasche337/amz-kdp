# Wissens-Scanner
*Skill: Verarbeitet neues Material und integriert es in die Wissensbasis*

---

## Aufruf

Sage: **"Scanne den incoming-Ordner"** oder **"Neues Material verarbeiten"**

---

## Schritt 1: Inventar

Lese alle Dateien in `research/incoming/`.

Für jede Datei bestimme:
- Dateityp (.txt, .md, .csv, .pdf, .xlsx)
- Geschätzter Inhalt (Titel, erste Zeilen)
- Relevanz-Kategorie (siehe Kategorie-Schema unten)

Zeige dem User eine Übersicht:

| # | Datei | Typ | Geschätzter Inhalt | Kategorie |
|---|-------|-----|---------------------|-----------|

**PAUSE:** "X Dateien gefunden. Soll ich alle verarbeiten oder einzelne auswählen?"

---

## Schritt 2: Extraktion

### Text-Dateien (.txt, .md)
- Lese den gesamten Inhalt
- Extrahiere: Kernaussagen, Zahlen/Daten, Handlungsempfehlungen
- Notiere Quelle (Dateiname, Datum, vermuteter Autor/Kanal)

### CSV-Dateien (Publisher Rocket)
→ **Nicht hier verarbeiten!** CSVs nach `incoming/rocket/` verschieben und den **ROCKET-SCANNER** nutzen (`research/ROCKET-SCANNER.md`). Der hat die vollständige Auswertungslogik für Keyword Search und Competition Analyzer.

### PDF-Dateien
- Lese Inhalt (wenn möglich)
- Erstelle Zusammenfassung der Kernpunkte
- Falls nicht lesbar: Notiere für manuellen Review

---

## Schritt 3: Kategorisierung

Ordne jede Erkenntnis einer Wissens-Kategorie zu:

| Signalwörter | Ziel-Datei |
|-------------|-----------|
| Markt, Trend, Umsatz, Wachstum, 2026, Algorithmus | `wissen/markt-trends-2026.md` |
| Keyword, Suchvolumen, Schwierigkeit, KDP-Box, Goldkeyword | `wissen/keywords-*.md` |
| Layla Hagen, Susie Tate, Buck, Lana Stone, ABSR, Konkurrenz | `wissen/konkurrenz-*.md` |
| Review, ARC, Launch, Social Media, TikTok, BookTok, DRM, Sperrung | `wissen/launch-operationen.md` |
| Eifel, Allgäu, Tirol, Zillertal, Region, Setting, Heimat | `wissen/regionale-settings.md` |
| Trope, Grumpy, Sunshine, Second Chance, Enemies to Lovers | `wissen/trope-analyse.md` |
| Listing, Beschreibung, Kategorie, Untertitel, Trigger-Wörter | `wissen/kdp-listing-methodik.md` |
| Workplace, Office, Agentur, Büro + "Lina Voss" | `wissen/keywords-lina-voss.md` |
| ab 40, Neuanfang, Clean, Slow Burn + "Maja" | `wissen/keywords-maja-sternberg.md` |

Wenn eine Erkenntnis in keine Kategorie passt → **neue Kategorie vorschlagen**.

**PAUSE:** Zeige Zuordnung. "Passt die Zuordnung?"

---

## Schritt 4: Integration

Für jede betroffene Wissens-Datei:

1. Lese die aktuelle Datei
2. Prüfe auf Duplikate (gleiche Erkenntnis bereits vorhanden?)
3. Wenn neu: Füge unter der passenden Sektion hinzu
   - Markiere mit Quelle: `[Quelle: dateiname.txt, 2026-XX-XX]`
   - Bei Widerspruch zu bestehender Erkenntnis: Beide behalten, markieren
4. Aktualisiere "Letzte Aktualisierung" Datum
5. Prüfe ob Wissenslücken geschlossen wurden → aus WISSENSBASIS.md streichen

---

## Schritt 5: Archivierung

Für jede verarbeitete Datei:

| Dateityp | Aktion |
|----------|--------|
| .txt, .md (Transkripte) | `[scanned]_` Prefix + nach `quellen/launch-wissen/` |
| CSV (Keyword Search) | nach `quellen/publisher-rocket/csv/keyword/` |
| CSV (Competition) | nach `quellen/publisher-rocket/csv/competition/` |
| Perplexity-Ergebnisse | nach `quellen/perplexity/` |
| PDF/XLSX/ZIP | nach `quellen/kdp-ressourcen/` |

---

## Schritt 6: WISSENSBASIS aktualisieren

1. Öffne `research/WISSENSBASIS.md`
2. Aktualisiere "Letzte Aktualisierung" bei betroffenen Themen
3. Aktualisiere Wissenslücken (geschlossene abhaken, neue hinzufügen)
4. Melde: **"Fertig. X Erkenntnisse in Y Dateien integriert."**

---

## Qualitätsregeln

- Alle Texte in korrektem Deutsch (Umlaute, ß)
- Zahlen immer mit Quelle und Datum versehen
- Publisher Rocket: Immer Book/eBook-Typ angeben
- Perplexity-Suchvolumina: **IMMER** als "unzuverlässig" markieren (200-300× übertrieben)
- Widersprüchliche Daten: Beide behalten, Widerspruch markieren
