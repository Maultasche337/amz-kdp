# SKILL: Amazon KDP Listing erstellen

## Zweck
Erstellt ein vollständig SEO-optimiertes Amazon KDP Listing auf Deutsch: Titel, Untertitel, Beschreibung, Keywords und Kategorien.

## Input
- `briefing.json` (Pflicht)
- `01_niche_analysis.md` (Pflicht)
- `04_outline.md` (Pflicht, für Inhaltsbeschreibung)

## Output
- `07_kdp_listing.md`

---

## Referenz: Fiction Description Formula (Kindlepreneur)

**Reihenfolge für Buchbeschreibung:**
1. **First Sentence Hook** — 80% der Energie hier investieren. Spannend, knapp, sofort neugierig.
2. **Keine Details-Flut** — kein Plot-Report. Nur das emotionale Versprechen.
3. **Stakes erhöhen** — Was verliert die Protagonistin, wenn sie scheitert?
4. **Kurze Absätze** — Große Textblöcke schrecken ab. Max. 3-4 Sätze pro Block.
5. **Wenig Formatierung** — Bei Fiction: kein Bold, keine Listen (anders als Sachbücher).
6. **Comparison Point** — Vergleich zu bekanntem Autor/Buch/Genre erhöht Glaubwürdigkeit.
7. **Mic Drop Moment** — Letzte 2 Sätze: Antagonist oder ultimativer Konflikt, maximale Spannung.
8. **CTA** — "Jetzt kaufen und [emotionaler Benefit]" → nachweislich +3,7% Konversion.

---

## Referenz: Emotionale Trigger-Wörter (nach Kategorie)

Gezielt in Titel, Untertitel und Beschreibung einsetzen:

| Kategorie | Funktion | Beispiele (Deutsch anpassen) |
|-----------|----------|------------------------------|
| **Romance** | Verlangen, Leidenschaft | Verboten, Leidenschaft, Sehnsucht, Verführung, unvergesslich |
| **Mystery** | Neugier, Geheimnis | Geheim, verborgen, verboten, Insider, unbekannt, verhüllt |
| **Energy** | Triumph, Stärke | Episch, legendär, unvergesslich, mutig, magisch, unglaublich |
| **Fear** | Spannung, Bedrohung | Gefahr, Schicksal, Dunkel, Verhängnis, Verrat, Abgrund |
| **Trust** | Vertrauen, Echtheit | Bewährt, authentisch, wahr, verlässlich, aufrichtig |
| **Anger** | Konflikt, Ungerechtigkeit | Lüge, Verrat, böse, Rache, Ausbeutung, korrupt |
| **Greed** | Schnäppchen, Wert | Kostenlos, Schatz, Reichtum, Gewinn, Geheimtipp, exklusiv |

**Genre-Mapping für Romance (Frauen 40+):**
- Primär: Romance + Mystery (Sehnsucht + Geheimnis = maximaler Hook)
- Sekundär: Trust (Verlässlichkeit, echte Gefühle — wichtig für ältere Zielgruppe)
- Vermeiden: Fear/Anger zu stark (passt nicht zur Cozy-Stimmung)

---

## Referenz: Titel-Entwicklung & Validierung (5-Schritt-System)

**Schritt 1 — Brainstorming-Elemente:**
- Setting-Name, Jahreszeit, Ort
- Charaktername oder Beziehungstyp
- Zentrales Thema / Emotion
- Genre-Trope als Andeutung
- SEO-Keyword natürlich integrieren

**Schritt 2 — Trigger Word ergänzen** (aus Tabelle oben)

**Schritt 3 — Validierungscheckliste:**
- [ ] Titel nicht bereits von populärem Buch besetzt?
- [ ] Keine ungewollten Bedeutungen in anderen Sprachen?
- [ ] Passt zum Cover? (max. 4-5 Wörter für Lesbarkeit)
- [ ] Taugt als Domain / Social-Media-Handle?
- [ ] Weckt sofort das Genre-Gefühl?

**Schritt 4 — Untertitel als Keyword-Träger:**
- Explizitere Keywords rein, die im Haupttitel nicht passen
- Zielgruppe ansprechen: "Ein Liebesroman für starke Frauen"
- Serien-Nummer falls vorhanden: "Die Alpenrose-Saga, Band 1"

---

## Prompt-Template

```
Du bist ein Amazon KDP SEO-Experte für den deutschsprachigen Markt.

BRIEFING:
[BRIEFING_JSON]

NISCHENANALYSE & KEYWORDS:
[NICHE_ANALYSIS]

HANDLUNGSÜBERSICHT:
[OUTLINE_SUMMARY]

Erstelle ein vollständiges Amazon KDP Listing auf Deutsch.

---

## Buchtitel
Haupttitel (max. 60 Zeichen, Keyword-optimiert, max. 4-5 Wörter für Cover-Lesbarkeit)

## Untertitel
(max. 200 Zeichen, weitere Keywords, emotionaler Nutzen, ggf. Serien-Hinweis)

## Buchbeschreibung (für Amazon)

Struktur nach Fiction Description Formula:
1. **First-Sentence-Hook** — sofort packend, keine Einleitung (2-3 Sätze max.)
2. Protagonistin + ihre Ausgangssituation (2-3 Sätze, emotional, keine Details-Liste)
3. Liebesinteresse + erste Spannung / Konflikt (2-3 Sätze)
4. Stakes — Was steht auf dem Spiel? Was verliert sie, wenn sie scheitert? (1-2 Sätze)
5. Comparison Point — optionaler Hinweis auf Genre/Autorin als Referenz (1 Satz)
6. Mic Drop Moment — letzter Satz: Antagonist oder ultimativer innerer Konflikt
7. Call to Action: "Jetzt lesen und [emotionaler Benefit]." (1 Satz)

Gesamtlänge: 150-400 Wörter
Absätze: max. 3-4 Sätze, keine Aufzählungen, kaum Fettdruck
Sprache: Emotional, warm, für Frauen 40+, kein Übersetzer-Stil

Verwende 2-3 Trigger-Wörter aus diesen Kategorien passend zum Ton:
- Romance: Sehnsucht, verboten, unvergesslich, Leidenschaft
- Mystery: verborgen, Geheimnis, Schatten, unbekannt
- Trust: wahr, aufrichtig, echte Gefühle

## 7 KDP Backend-Keywords (je max. 50 Zeichen)
(Amazon Backend-Keywords — nicht im Listing sichtbar)

## Empfohlene Kategorien
(2 Amazon-Buchkategorien auf Deutsch — so spezifisch wie möglich)

## A+ Content Idee
(kurze Idee für erweiterten Buchbeschreibungsbereich, z.B. Charakter-Zitat, Stimmungsbild)

---

Achte auf: Keine Spoiler, Tropes dezent andeuten (nicht erklären), Zielgruppe direkt ansprechen.
```
