# SKILL: Story-Ending generieren

## Zweck
Erstellt 10 mögliche Story-Endings basierend auf Briefing und Nischenanalyse. Das beste Ending wird ausgewählt und vollständig ausgearbeitet.

## Input
- `briefing.json` (Pflicht)
- `01_niche_analysis.md` (Pflicht)

## Output
- `02_ending.md` im Buchordner

## Prompt-Template

```
Du bist eine erfahrene Romanautorin im deutschsprachigen Raum, spezialisiert auf Romance-Fiction für Frauen 40+.

Hier ist das Buchbriefing:
[BRIEFING_JSON]

Hier ist die Nischenanalyse:
[NICHE_ANALYSIS]

Schritt 1: Erstelle 10 verschiedene mögliche Story-Endings für diesen Roman. Jedes Ending soll:
- Emotional befriedigend sein (HEA wenn im Briefing angegeben)
- Die spezifischen Tropes aus dem Briefing erfüllen
- Zur Zielgruppe passen
- Einen einzigartigen emotionalen Kern haben
- Ca. 3-5 Sätze beschreiben

Schritt 2: Wähle selbst das stärkste Ending aus (begründe kurz warum) und arbeite es vollständig aus:
- Vollständige Szene (500-800 Wörter)
- Thematische Notizen: Was löst dieses Ending emotional aus?
- Welche Story-Threads müssen im Verlauf des Buches aufgebaut werden damit dieses Ending funktioniert?

Antworte komplett auf Deutsch. Formatiere als Markdown.
```

## Hinweise
- Denkmodus aktivieren
- Das ausgearbeitete Ending wird als Anker für alle weiteren Schritte verwendet
