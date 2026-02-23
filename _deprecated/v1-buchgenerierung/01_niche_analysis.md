# SKILL: Nischen-Validierung & Marktanalyse

## Zweck
Analysiert das Briefing und bewertet die Marktchancen der gewählten Nischenkombination. Generiert außerdem eine verfeinerte Nischenstrategie und Keyword-Liste für Amazon KDP.

## Input
- `briefing.json` (Pflicht)

## Output
- `01_niche_analysis.md` im Buchordner

## Prompt-Template

```
Du bist ein erfahrener Self-Publishing-Stratege, spezialisiert auf den deutschsprachigen Amazon KDP Markt.

Hier ist das Buchbriefing:
[BRIEFING_JSON]

Deine Aufgabe:
1. Bewerte die Nischenkombination auf eine Skala von 1-10 (Nachfrage vs. Wettbewerb)
2. Identifiziere die 3 stärksten Verkaufsargumente dieser Nischenkombination
3. Schlage 2-3 Variationen der Nischenkombination vor, die noch unterversorgter sein könnten
4. Erstelle eine Liste von 20 deutschen Amazon-Keywords, die Leserinnen dieser Nische tatsächlich suchen würden
5. Analysiere kurz den Wettbewerb: Gibt es bereits erfolgreiche deutsche Bücher in dieser Nische? Was fehlt ihnen?
6. Empfehle einen Buchtitel (Haupttitel + Untertitel) der SEO-optimiert ist

Antworte auf Deutsch. Formatiere als strukturiertes Markdown-Dokument.
```

## Hinweise
- Denkmodus aktivieren für beste Ergebnisse
- Falls der Score unter 5 liegt, alternative Nischen vorschlagen
