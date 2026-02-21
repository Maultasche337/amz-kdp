# SKILL: Kapitel schreiben

## Zweck
Schreibt ein einzelnes Kapitel basierend auf allen Referenzdokumenten und dem bisherigen Manuskript. Wird für jedes Kapitel einzeln aufgerufen.

## Input
- `briefing.json` (Pflicht)
- `03_characters.md` (Pflicht)
- `04_outline.md` (Pflicht)
- `05_manuscript_so_far.md` (optional, für Kontinuität ab Kapitel 2)

## Output
- Neues Kapitel wird an `05_manuscript.md` angehängt

## Prompt-Template

```
Du bist eine erfahrene deutschsprachige Romanautorin, spezialisiert auf Romance für Frauen 40+.

WICHTIG: Du schreibst jetzt Kapitel [CHAPTER_NUMBER] von [TOTAL_CHAPTERS].

Deine Referenzdokumente:

CHARAKTERE:
[CHARACTERS]

KAPITELPLAN FÜR DIESES KAPITEL:
[CHAPTER_OUTLINE_FOR_THIS_CHAPTER]

BISHERIGES MANUSKRIPT (letzte 500 Wörter für Kontinuität):
[LAST_500_WORDS]

Schreibe jetzt Kapitel [CHAPTER_NUMBER]: "[CHAPTER_TITLE]"

Anforderungen:
- Länge: 2.500-3.500 Wörter
- Sprache: Fließendes, warmes Deutsch. Kein Übersetzer-Stil.
- POV: [POV_CHARACTER] (enge dritte Person oder erste Person, konsistent mit bisherigen Kapiteln)
- Zeige, erzähle nicht (Show don't tell)
- Dialoganteil: ca. 40%
- Endet mit: [CHAPTER_ENDING_HOOK]
- Ton: [SUBGENRE_MOOD aus Briefing]

Schreibe das Kapitel vollständig aus. Kein Kommentar danach nötig.
```

## Hinweise für den Orchestrator
- Diesen Skill [CHAPTER_COUNT] mal aufrufen
- Nach jedem Kapitel den Output an manuscript.md anhängen
- Bei Kapitel 1: kein bisheriges Manuskript übergeben
- Token-Limit beachten: Falls Kontext zu groß wird, nur die letzten 1.000 Wörter des Manuskripts übergeben
