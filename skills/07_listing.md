# SKILL: Amazon KDP Listing erstellen

## Zweck
Erstellt ein vollständig SEO-optimiertes Amazon KDP Listing auf Deutsch: Titel, Untertitel, Beschreibung, Keywords und Kategorien.

## Input
- `briefing.json` (Pflicht)
- `01_niche_analysis.md` (Pflicht)
- `04_outline.md` (Pflicht, für Inhaltsbeschreibung)

## Output
- `07_kdp_listing.md`

## Verwandte Sub-Skills
- `skills/07a_keywords.md` — vollständiger 5-Schritt-Keyword-Prozess (Ideenliste → Bewertung → 7 Boxen → Titel → Beschreibung)
- `skills/07b_kategorie_strategie.md` — 6-Schritt-Kategorieauswahl inkl. Duplikate & Geisterkategorien
- `skills/07c_kategorie_keywords.md` — Kategorie-Keywords für die 7 KDP-Felder

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

## Referenz: Die 7 KDP-Keyword-Boxen (vollständige Methodik)

→ Detailprozess in `skills/07a_keywords.md`. Kernregeln hier:

### Amazon-Flywheel verstehen
- Platz 1 eines Keywords → 27 % aller Klicks, Platz 2 → 12 %
- Amazon beobachtet Conversion: gute Verkäufe → automatisch mehr verwandte Phrasen indexiert
- Ziel: Netz aus relevanten Phrasen, nicht ein einziges Top-Keyword

### Strategieprinzip: Tiefe vs. Breite
```
Box 1–3  → je eine starke Ziel-Phrase allein → maximales Ranking
Box 5–7  → viele Begriffe kombiniert → breite Indexierung
```
Amazon indexiert 98,3 % aller Wortkombinationen aus einer Box.

### Technische Regeln
- Max. 50 Zeichen pro Box (Buchstaben + Leerzeichen)
- Wiederholungen schaden/helfen nicht — nicht extra einbauen
- Keyword versagt wenn: Amazon zeigt dafür keine Ergebnisse / inhaltlich nicht passend / Richtlinienverstoß

### Bewertungskriterien (Priorität)
1. **Relevanz** — muss inhaltlich passen (wichtigstes Kriterium)
2. **Suchvolumen** — mind. > 100 Suchanfragen/Monat auf Amazon
3. **Verkaufsnachweis** — ABSR der Top-5-Bücher → Kindle Calculator → Tagesumsatz
4. **Wettbewerbsscore** — neuer Autor: ≤ 40 | mittel: ≤ 60 | erfahren: ≤ 90

### Fiction Keywords — 5 Kategorien
| Kategorie | Beispiele |
|---|---|
| Settings & Zeitperioden | Victorian, Western, Post-Apokalyptisch, Caribbean |
| Charaktertypen & Rollen | Alpha Male, Werewolf, Second Chance Romance, Amish |
| Plot & Thema | Summer House Romance, Love Torn Apart by War, Revenge |
| Events & Situationen | Plane Crash, Kidnapping, Dragon Attack, Civil War |
| Story Tone | Christian Wholesome, Hot and Steamy, Cozy, Gruesome Mystery |

### Keyword-Gewichtung im Titel/Untertitel
- Titel/Untertitel-Keywords: +30 % Gewichtung vs. Backend-Boxen
- Indexierungsrate: 100 % wenn Keyword im Titel
- Ranking-Steigerung: +37 % gegenüber ohne Keyword im Titel
- **Goldene Regel:** Natürlichkeit vor Keyword-Dichte — Stuffing senkt Conversion und Rankings

---

## Referenz: Kategorie-Strategie (Kurzfassung)

→ Vollständiger 6-Schritt-Prozess in `skills/07b_kategorie_strategie.md`

### Kernprinzipien
- **3 Kategorien wählen**, davon **genau 1 Duplikat** (= Bestseller-Leiter)
- **Duplikat-Vorteil:** Buch erscheint automatisch in allen übergeordneten Unterkategorien aller Duplikat-Strings
- **Geisterkategorien (Ghost Categories):** 27 % aller KDP-Kategorien — haben keine navigierbare Seite, kein Bestseller-Tag. Nie zwei Ghost Categories aus derselben Unterkategorie.
- **Wettbewerbsintensität:** neues Buch → leichte bis mittlere Kategorien bevorzugen

### Kategorie-Keywords (1–2 der 7 Felder)
→ Detail-Methodik in `skills/07c_kategorie_keywords.md`
- 1–2 der 7 KDP-Felder für kategoriespezifische Signalwörter reservieren
- Signalwörter direkt aus den Kategorie-Strings extrahieren (höchste Algorithmus-Wirkung)
- Deutsche UND englische Begriffe einsetzen (z. B. `Cozy Mystery` + `Gemütlicher Krimi`)

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

Wende das Tiefe-vs-Breite-Prinzip an:
- Box 1–3: je eine starke Ziel-Phrase (Fiction: Kombination aus 2-3 der 5 Kategorien)
- Box 4: optional vierte Top-Phrase
- Box 5–7: Kombinations-Boxen mit mehreren Begriffen für breite Indexierung
  → 1–2 dieser Boxen für Kategorie-Signalwörter reservieren (siehe 07c_kategorie_keywords)

## Empfohlene Kategorien (3 Stück)

Wähle nach dem 6-Schritt-System (Details: 07b_kategorie_strategie):
- Kategorie 1: Hauptwahl (inhaltlich stärkste Passung)
- Kategorie 2: Duplikat-Wahl (Bestseller-Leiter) — kennzeichne welche Zusatz-Kategorien erschlossen werden
- Kategorie 3: Backup / Reichweite

Vollständige Kategorie-Strings angeben (z. B. Kindle-Shop → Kindle-E-Books → Krimis & Thriller → Cosy-Krimis)

## A+ Content Idee
(kurze Idee für erweiterten Buchbeschreibungsbereich, z.B. Charakter-Zitat, Stimmungsbild)

---

Achte auf: Keine Spoiler, Tropes dezent andeuten (nicht erklären), Zielgruppe direkt ansprechen.
```
