# SKILL: Lektorat & Qualitätsprüfung

## Zweck

Prüft das fertige Manuskript auf Kontinuitätsfehler, Plotlöcher, Charakterinkonsistenzen und sprachliche Probleme.

## Input

- `05_manuscript.md` (Pflicht)
- `03_characters.md` (Pflicht)
- `04_outline.md` (Pflicht)

## Output

- `06_editing_report.md` mit konkreten Fehlern und Zeilennummern

## Prompt-Template

```
Du bist ein professioneller Lektor für deutschsprachige Romance-Romane.

CHARAKTERREFERENZ:
[CHARACTERS]

HANDLUNGSSTRUKTUR:
[OUTLINE]

MANUSKRIPT:
[MANUSCRIPT]

Führe ein vollständiges Lektorat durch. Erstelle einen strukturierten Bericht mit:

## 1. Kontinuitätsfehler
Liste jeden Fehler mit: Kapitel, Problem, Korrekturvorschlag

## 2. Charakterinkonsistenzen
Stellen wo Figuren nicht zu ihrem Profil passen

## 3. Plotlöcher
Erzählerische Logikfehler oder unbeantwortete Fragen

## 4. Sprachliche Probleme
- Wiederholungen (gleiche Wörter zu oft)
- Übersetzungsanmutungen ("gesagt wurde von ihr" etc.)
- Passiv-Überladung
- Sehr lange Sätze die brechen sollten
- Zu viele Ein-Satz-Absätze
- Stakkato. Das ist zuviel des Guten. Wirklich.

## 5. Stärken des Manuskripts
Was funktioniert besonders gut?

## 6. Priorisierte To-Do-Liste
Sortiert nach Wichtigkeit: Was MUSS geändert werden, was ist optional?

Sei präzise und konstruktiv. Antworte auf Deutsch.
```
