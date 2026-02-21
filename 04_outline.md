# SKILL: Save-the-Cat Kapitelstruktur

## Zweck
Erstellt eine vollständige 15-Beat Save-the-Cat Storyline, aufgeteilt auf die Zielanzahl Kapitel aus dem Briefing.

## Input
- `briefing.json` (Pflicht)
- `02_ending.md` (Pflicht)
- `03_characters.md` (Pflicht)

## Output
- `04_outline.md` im Buchordner

## Die 15 Save-the-Cat Beats (Referenz)
1. Opening Image
2. Theme Stated
3. Set-Up
4. Catalyst
5. Debate
6. Break into Two
7. B Story
8. Fun and Games
9. Midpoint
10. Bad Guys Close In
11. All Is Lost
12. Dark Night of the Soul
13. Break into Three
14. Finale
15. Final Image

## Prompt-Template

```
Du bist eine erfahrene Romanautorin und Story-Strukturexpertin.

Hier sind alle Referenzdokumente:

BRIEFING:
[BRIEFING_JSON]

ENDING:
[ENDING]

CHARAKTERE:
[CHARACTERS]

Erstelle eine vollständige Save-the-Cat Storyline für diesen Roman mit exakt [CHAPTER_COUNT] Kapiteln.

Für jeden der 15 Beats:
- Erkläre wie dieser Beat in diesem spezifischen Roman aussieht
- Ordne ihn einem oder mehreren Kapiteln zu

Für jedes der [CHAPTER_COUNT] Kapitel:
- Kapitelnummer und Titel
- Welcher STC-Beat (falls zutreffend)
- POV (wessen Perspektive)
- Setting (Ort, Tageszeit, Stimmung)
- Hauptkonflikt des Kapitels
- Emotionaler Kern (was fühlt die Leserin am Ende dieses Kapitels?)
- Wichtige Szenen (2-4 Stichpunkte)
- Cliffhanger oder Überleitung zum nächsten Kapitel
- Geschätzte Wortanzahl: 2.500-3.500 Wörter

Stelle sicher dass:
- Die Tropes aus dem Briefing ([TROPES]) organisch eingebaut werden
- Das Ending aus dem Referenzdokument nahtlos erreicht wird
- Der Entwicklungsbogen aller Charaktere sich durch die Kapitel zieht

Antworte komplett auf Deutsch. Formatiere als detailliertes Referenz-Dokument.
```
