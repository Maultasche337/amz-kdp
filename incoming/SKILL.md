---
name: kdp-keywords
version: 1.0.0
description: >
  Entwickle und optimiere Keywords für Kindle Direct Publishing (KDP).
  Nutze diesen Skill wenn der User Keywords für sein KDP-Buch entwickeln,
  bewerten oder platzieren möchte – inklusive Keyword-Recherche, Auswahl
  der sieben Kindle-Keyword-Boxen, Titel/Untertitel-Optimierung und
  Buchbeschreibung.
author: KDP Keyword Expert
language: de
tags:
  - kdp
  - kindle
  - amazon
  - keywords
  - self-publishing
  - book-marketing
inputs:
  - name: book_type
    type: string
    required: true
    description: "Fiction oder Nonfiction"
    enum: [fiction, nonfiction]
  - name: genre
    type: string
    required: true
    description: "Genre oder Thema des Buches (z. B. Sci-Fi Military, Selbsthilfe, Kochbuch)"
  - name: target_audience
    type: string
    required: false
    description: "Zielgruppe des Buches (z. B. Frauen ab 50, Einsteiger, IT-Fachleute)"
  - name: existing_keywords
    type: list
    required: false
    description: "Bereits vorhandene Keywords oder Buchtitel zur Analyse"
  - name: author_level
    type: string
    required: false
    description: "Erfahrungsstufe des Autors"
    enum: [new, medium, experienced]
    default: new
  - name: has_publisher_rocket
    type: boolean
    required: false
    description: "Gibt an ob Publisher Rocket verfügbar ist"
    default: false
outputs:
  - name: keyword_ideas
    type: list
    description: "Keyword-Ideenliste nach Kategorien gegliedert"
  - name: shortlist
    type: list
    description: "Bewertete Shortlist der besten Keyword-Kandidaten"
  - name: seven_boxes
    type: list
    description: "Vorschlag für die 7 Kindle-Keyword-Boxen"
  - name: title_suggestion
    type: string
    description: "Titelvorschlag mit Untertitel inkl. natürlich integrierten Keywords"
  - name: description_hints
    type: list
    description: "Keyword-Phrasen zum Einbauen in die Buchbeschreibung"
tools_required: []
tools_optional:
  - name: publisher_rocket
    description: "Automatisiert Suchvolumen, Verkaufszahlen und Wettbewerbsscore"
  - name: amazon_autocomplete
    description: "Kostenloses Recherche-Tool über das Amazon-Suchfeld"
  - name: kindle_calculator
    description: "Kostenloser ABSR-Rechner, Google: 'Kindle Calculator'"
---

# KDP Keywords Skill

Dieser Skill führt durch den vollständigen KDP-Keyword-Prozess: von der
Ideenfindung über die Datenbewertung bis zur strategischen Platzierung
in allen relevanten Buchfeldern – Keyword-Boxen, Titel, Untertitel und
Buchbeschreibung.

## Hintergrund: Wie Amazon auf Keywords reagiert

Bevor Keywords entwickelt werden, ist das Verständnis der Amazon-Logik
entscheidend:

- Das Buch auf Platz 1 eines Keywords erhält 27 % aller Klicks, Platz 2
  nur 12 %, danach sinkt die Rate schnell weiter.
- Amazon beobachtet die Conversion: Wenn ein Buch für bestimmte Keywords
  gut verkauft, indexiert Amazon es automatisch für weitere verwandte
  Phrasen und erhöht die Rankings.
- Ziel ist nicht ein einzelnes starkes Keyword, sondern ein Netz aus
  relevanten Phrasen, das diesen Kreislauf in Gang setzt.

---

## Schritt 1: Keyword-Ideenliste aufbauen

### Fiction – 5 Kategorien

Käufer kombinieren typischerweise 2–3 dieser Kategorien bei der Suche.
Für jede Kategorie werden passende Begriffe gesammelt:

| Kategorie | Beschreibung | Beispiele |
|---|---|---|
| Settings & Zeitperioden | Wo und wann spielt die Geschichte? | Victorian, Western, Gas Lamp, Post-Apokalyptisch, Caribbean |
| Charaktertypen & Rollen | Wer ist Protagonist oder Antagonist? | Alpha Male, Billionaire, Werewolf, Amish, Second Chance Romance |
| Plot & Thema | Was ist der zentrale Handlungsstrang? | Summer House Romance, Love Torn Apart by War, Revenge |
| Events & Situationen | Was löst die Geschichte aus? (Katalysator) | Plane Crash, Kidnapping, Disease, Civil War, Dragon Attack |
| Story Tone | Wie ist die emotionale Stimmung? | Christian Wholesome, Hot and Steamy, Gruesome Mystery, Cozy |

Alle plausiblen 2–3-Wort-Kombinationen aus diesen Kategorien erzeugen.

### Nonfiction – 4 Kategorien

| Kategorie | Beschreibung | Tiefe der Analyse |
|---|---|---|
| Pain Points | Das Problem, das den Käufer antreibt | Oberfläche → tieferliegende Emotion (z. B. „Übergewicht" → „fühle mich unwohl", „werde nicht ernst genommen") |
| Results & Solutions | Das gewünschte Ergebnis | Direkt als Handlungsversprechen (z. B. Lose Weight, Be Rich, Learn Faster) |
| Emotional Amplifiers | Verstärker für das Versprechen | Zeitangaben (in one hour), Adverbien (fast, easily), Zahlen (13 Ways to...) |
| Demographics | Spezifische Zielgruppe | NUR wenn Marktrecherche reales Suchvolumen belegt (z. B. Over 50, Busy Moms, Lawyers) |

---

## Schritt 2: Keywords bewerten

Jeder Kandidat wird nach vier Kriterien bewertet – in dieser Priorität:

### Kriterium 1: Relevanz ⚡ (wichtigstes Kriterium)
Das Keyword MUSS inhaltlich zum Buch passen.

```
✅ Buch passt zum Keyword → Amazon indexiert, Käufer klicken, Verkäufe entstehen
❌ Buch passt nicht     → Amazon ignoriert ODER schlechte CTR → Ranking sinkt aktiv
```

### Kriterium 2: Monatliches Suchvolumen
- Minimum: **> 100 Suchanfragen/Monat** auf Amazon
- Dieser Wert bestätigt echte Käuferaktivität, keine leere Phrase

```yaml
recherche:
  mit_publisher_rocket: "Direkt ablesbar in der Ergebnisspalte"
  ohne_publisher_rocket: "Amazon-Autocomplete → manuell einschätzen"
```

### Kriterium 3: Verkaufsnachweis
Prüfen ob Bücher, die für dieses Keyword ranken, tatsächlich Umsatz
erzielen:

```yaml
manuell:
  schritt_1: "Keyword in Amazon eingeben → Top 5 Bücher öffnen"
  schritt_2: "Amazon Bestseller Rank (ABSR) notieren"
  schritt_3: "ABSR in Kindle Calculator eingeben → Tagesverkäufe"
  schritt_4: "Tagesverkäufe × Preis = Tagesumsatz"
  schritt_5: "Durchschnitt der 5 Bücher berechnen"
mit_publisher_rocket:
  ergebnis: "Monatliche Verkaufszahlen direkt verfügbar"
sonderfall:
  wenn: "Bücher trotz Suchanfragen keine Verkäufe"
  dann: "Grund analysieren – schlechte Cover? falsches Buch? → ggf. Chance"
```

### Kriterium 4: Wettbewerbsscore

| Autortyp | Definition | Empfohlener Score |
|---|---|---|
| `new` | Erstes Buch, kein aktives Marketing | ≤ 40 |
| `medium` | Mehrere Bücher, Erfahrung vorhanden | ≤ 60 |
| `experienced` | Fanbase, E-Mail-Liste, Marketingkapazität | ≤ 90 |

> Erfahrene Autoren können höhere Scores überwinden, weil sie durch
> aktives Marketing die Verkäufe und damit das Amazon-Ranking ankurbeln.

---

## Schritt 3: Die 7 Kindle-Keyword-Boxen befüllen

### Strategieprinzip: Tiefe vs. Breite

```
┌─────────────────────────────────────────────────────────┐
│  Box 1  │ ← Beste Phrase allein     → Maximales RANKING │
│  Box 2  │ ← Beste Phrase allein     → Maximales RANKING │
│  Box 3  │ ← Beste Phrase allein     → Maximales RANKING │
│ (Box 4) │ ← Ggf. vierte Top-Phrase → Maximales RANKING │
├─────────────────────────────────────────────────────────┤
│  Box 5  │ ← Viele Begriffe kombiniert → Breite INDEX.   │
│  Box 6  │ ← Viele Begriffe kombiniert → Breite INDEX.   │
│  Box 7  │ ← Viele Begriffe kombiniert → Breite INDEX.   │
└─────────────────────────────────────────────────────────┘
```

Amazon indexiert **98,3 %** aller Wortkombinationen aus einer Box,
inklusive Zwei- und Dreiwortkombinationen sowie Pluralformen.

### Technische Regeln

```yaml
zeichen_pro_box: 50  # Buchstaben + Leerzeichen
wiederholungen:
  schaden: false
  helfen: false
  empfehlung: "Nicht extra einbauen, aber auch nicht aufwändig entfernen"
indexierung_schlägt_fehl_wenn:
  - "Amazon zeigt für diesen Begriff generell keine Suchergebnisse"
  - "Keyword passt inhaltlich nicht zum Buch"
  - "Begriff verstößt gegen Amazons Richtlinien"
```

---

## Schritt 4: Titel und Untertitel optimieren

### Warum Titel/Untertitel so wichtig sind

```yaml
gewichtung_vs_keyword_boxen: "+30%"
indexierungsrate: "100% wenn Keyword im Titel/Untertitel"
ranking_steigerung: "+37% im Vergleich zu ohne Keyword in Titel"
amazon_behandlung: "Titel und Untertitel als ein gemeinsamer Datenpunkt"
```

### Goldene Regel: Natürlichkeit vor Keyword-Dichte

```
❌ FALSCH: „Sci-Fi Military Space Marine Battle Alien Invasion War Novel"
✅ RICHTIG: „Iron Vanguard: A Space Marine Epic in the Last Galactic War"
```

Keyword-Stuffing im Titel wirkt unseriös → Käufer klicken nicht →
Conversion sinkt → Amazon senkt Rankings.

### Was Käufer im Titel/Untertitel entscheiden

**Nonfiction** – Cover + Titel + Untertitel müssen drei Fragen
beantworten:

```yaml
frage_1: "Für wen ist das Buch?"        # Demografik
frage_2: "Worum geht es?"               # Pain Point / Thema
frage_3: "Was bringt es mir?"           # Result / Solution
```

Empfohlene Untertitel-Formel:
`[Pain Point] → [Result] + [Amplifier] + [weiterer Result]`

Beispiel: „Upgrade Your Brain, Learn Anything Faster & Unlock Your
Exceptional Life"

**Fiction** – Cover + Titel + Untertitel müssen beantworten:

```yaml
frage_1: "Ist das mein Genre / Sub-Genre?"
frage_2: "Passt der Tone zu dem was ich suche?"
```

Sub-Genre explizit nennen wenn das Cover es nicht eindeutig zeigt.
Beispiel: „A Lit RPG Gamelit Adventure" als Untertitel.

---

## Schritt 5: Buchbeschreibung keyword-bewusst verfassen

### Wie Amazon die Buchbeschreibung auswertet

Amazon analysiert die Buchbeschreibung auf relevante Begriffe – identisch
zur Auswertung von Rezensionen. Keywords in der Beschreibung bestätigen
Amazons Einschätzung, für welche Suchanfragen das Buch relevant ist.

### Vorgehen

```yaml
schritt_1: "Buchbeschreibung frei schreiben (Fokus: Emotion + Verkauf)"
schritt_2: "Fertige Beschreibung mit Keyword-Liste abgleichen"
schritt_3: "Passende Keywords dort einarbeiten wo sie natürlich passen"
schritt_4: "Formulierungen so anpassen dass sie nach Zielgruppen-Sprache klingen"
```

### Doppelter Nutzen

```
Keywords in Beschreibung
        │
        ├─→ Amazon bestätigt Zuordnung → besseres Ranking
        │
        └─→ Zielgruppen-Sprache → höhere Conversion Rate
```

---

## Ausgabeformat

Bei der Ausgabe immer alle fünf Bereiche liefern:

```yaml
ausgabe:
  1_keyword_ideenliste:
    format: "Tabelle oder Liste, gegliedert nach Kategorien"
    umfang: "Mind. 5 Begriffe pro Kategorie"

  2_bewertete_shortlist:
    format: "Tabelle: Phrase | Relevanz | Volumen | Verkäufe | Score | Empfehlung"
    markierung: "Spezifik-Box (S) oder Kombinations-Box (K)"

  3_sieben_boxen_vorschlag:
    format: "Box 1–7 mit konkretem Inhalt"
    markierung: "Spezifik (S) oder Kombination (K)"

  4_titelvorschlag:
    format: "Haupttitel + Untertitel"
    nachweis: "Welche Keywords wo eingebaut wurden"

  5_beschreibungs_hinweise:
    format: "Liste konkreter Phrasen zum natürlichen Einbauen"
    umfang: "Mind. 8–10 Phrasen"
```

---

## Das Amazon-Flywheel

```
Relevante Keywords
      ↓
Buch erscheint für richtige Suchanfragen
      ↓
Käufer klicken & kaufen → Amazon: dieses Buch konvertiert gut
      ↓
Amazon indexiert für weitere verwandte Phrasen
      ↓
Mehr Sichtbarkeit → mehr Verkäufe → noch mehr Phrasen
      ↓
Gleichgewicht → dauerhafter passiver Traffic
```

> Lieber 7+ relevante Keywords mit moderatem Volumen als ein einziger
> hochvolumiger Begriff mit starker Konkurrenz. Das System belohnt
> Relevanz und Conversion – nicht allein das Suchvolumen.
