# SKILL: KDP Keywords — 5-Schritt-Prozess

## Zweck
Vollständiger KDP-Keyword-Prozess: Ideenfindung → Datenbewertung → strategische Platzierung
in allen relevanten Buchfeldern (Keyword-Boxen, Titel, Untertitel, Buchbeschreibung).

## Einsatz
Wird aufgerufen von `07_listing.md` für die Keyword-Sektion. Kann auch eigenständig
verwendet werden wenn gezielt Keyword-Recherche ohne vollständiges Listing gewünscht wird.

## Input
- Genre / Subgenre (Pflicht)
- Buchtitel und Kurzbeschreibung (Pflicht)
- Zielgruppe (optional)
- Bestehende Keywords zur Analyse (optional)
- Autortyp: `new` | `medium` | `experienced` (Standard: `new`)
- Publisher Rocket verfügbar: `ja` | `nein` (Standard: `nein`)

## Output
1. Keyword-Ideenliste (nach Kategorien gegliedert)
2. Bewertete Shortlist
3. Vorschlag für die 7 Kindle-Keyword-Boxen
4. Titelvorschlag mit integrierten Keywords
5. Phrasen für die Buchbeschreibung

---

## Hintergrund: Wie Amazon auf Keywords reagiert

- Platz 1 eines Keywords → 27 % aller Klicks | Platz 2 → 12 % | danach schnell fallend
- Amazon beobachtet Conversion: Buch verkauft gut → Amazon indexiert automatisch weitere verwandte Phrasen
- Ziel: Netz aus relevanten Phrasen, das diesen Kreislauf in Gang setzt — nicht ein einzelnes Top-Keyword

---

## Schritt 1: Keyword-Ideenliste aufbauen

### Fiction — 5 Kategorien

Käufer kombinieren typischerweise 2–3 dieser Kategorien bei der Suche.

| Kategorie | Beschreibung | Beispiele |
|---|---|---|
| Settings & Zeitperioden | Wo und wann spielt die Geschichte? | Victorian, Western, Gas Lamp, Post-Apokalyptisch, Caribbean |
| Charaktertypen & Rollen | Wer ist Protagonist oder Antagonist? | Alpha Male, Billionaire, Werewolf, Amish, Second Chance Romance |
| Plot & Thema | Was ist der zentrale Handlungsstrang? | Summer House Romance, Love Torn Apart by War, Revenge |
| Events & Situationen | Was löst die Geschichte aus? (Katalysator) | Plane Crash, Kidnapping, Disease, Civil War, Dragon Attack |
| Story Tone | Wie ist die emotionale Stimmung? | Christian Wholesome, Hot and Steamy, Gruesome Mystery, Cozy |

Alle plausiblen 2–3-Wort-Kombinationen aus diesen Kategorien erzeugen.

### Nonfiction — 4 Kategorien

| Kategorie | Beschreibung | Tiefe der Analyse |
|---|---|---|
| Pain Points | Das Problem, das den Käufer antreibt | Oberfläche → tieferliegende Emotion (z. B. „Übergewicht" → „fühle mich unwohl") |
| Results & Solutions | Das gewünschte Ergebnis | Direkt als Handlungsversprechen (z. B. Lose Weight, Be Rich, Learn Faster) |
| Emotional Amplifiers | Verstärker für das Versprechen | Zeitangaben (in one hour), Adverbien (fast, easily), Zahlen (13 Ways to...) |
| Demographics | Spezifische Zielgruppe | NUR wenn Marktrecherche reales Suchvolumen belegt (z. B. Over 50, Busy Moms) |

---

## Schritt 2: Keywords bewerten

Jeder Kandidat wird nach vier Kriterien bewertet — in dieser Priorität:

### Kriterium 1: Relevanz ⚡ (wichtigstes Kriterium)
Das Keyword MUSS inhaltlich zum Buch passen.

```
✅ Buch passt zum Keyword → Amazon indexiert, Käufer klicken, Verkäufe entstehen
❌ Buch passt nicht     → Amazon ignoriert ODER schlechte CTR → Ranking sinkt aktiv
```

### Kriterium 2: Monatliches Suchvolumen
- Minimum: > 100 Suchanfragen/Monat auf Amazon
- Bestätigt echte Käuferaktivität

```
mit Publisher Rocket:  Direkt ablesbar in der Ergebnisspalte
ohne Publisher Rocket: Amazon-Autocomplete → manuell einschätzen
```

### Kriterium 3: Verkaufsnachweis

Prüfen ob Bücher, die für dieses Keyword ranken, tatsächlich Umsatz erzielen:

```
Manuell:
  1. Keyword in Amazon eingeben → Top 5 Bücher öffnen
  2. Amazon Bestseller Rank (ABSR) notieren
  3. ABSR in Kindle Calculator eingeben → Tagesverkäufe
  4. Tagesverkäufe × Preis = Tagesumsatz
  5. Durchschnitt der 5 Bücher berechnen

Mit Publisher Rocket: Monatliche Verkaufszahlen direkt verfügbar

Sonderfall: Bücher trotz Suchanfragen keine Verkäufe
  → Grund analysieren: schlechte Cover? falsches Buch? → ggf. Chance
```

### Kriterium 4: Wettbewerbsscore

| Autortyp | Definition | Empfohlener Score |
|---|---|---|
| `new` | Erstes Buch, kein aktives Marketing | ≤ 40 |
| `medium` | Mehrere Bücher, Erfahrung vorhanden | ≤ 60 |
| `experienced` | Fanbase, E-Mail-Liste, Marketingkapazität | ≤ 90 |

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

Amazon indexiert 98,3 % aller Wortkombinationen aus einer Box,
inklusive Zwei- und Dreiwortkombinationen sowie Pluralformen.

**Von den Kombinations-Boxen (5–7): 1–2 Felder für Kategorie-Signalwörter reservieren**
→ Details: `skills/07c_kategorie_keywords.md`

### Technische Regeln

```
Zeichen pro Box:        50 (Buchstaben + Leerzeichen)
Wiederholungen:         schaden nicht, helfen nicht → nicht extra einbauen
Indexierung schlägt fehl wenn:
  - Amazon zeigt für diesen Begriff generell keine Suchergebnisse
  - Keyword passt inhaltlich nicht zum Buch
  - Begriff verstößt gegen Amazons Richtlinien
```

---

## Schritt 4: Titel und Untertitel optimieren

### Warum Titel/Untertitel so wichtig sind

```
Gewichtung vs. Keyword-Boxen:  +30 %
Indexierungsrate:               100 % wenn Keyword im Titel/Untertitel
Ranking-Steigerung:             +37 % gegenüber ohne Keyword in Titel
Amazon-Behandlung:              Titel und Untertitel als ein gemeinsamer Datenpunkt
```

### Goldene Regel: Natürlichkeit vor Keyword-Dichte

```
❌ FALSCH: „Sci-Fi Military Space Marine Battle Alien Invasion War Novel"
✅ RICHTIG: „Iron Vanguard: A Space Marine Epic in the Last Galactic War"
```

Keyword-Stuffing wirkt unseriös → Käufer klicken nicht → Conversion sinkt → Amazon senkt Rankings.

### Was Käufer im Titel/Untertitel entscheiden

**Nonfiction** — Titel muss drei Fragen beantworten:
```
Für wen ist das Buch?   (Demografik)
Worum geht es?          (Pain Point / Thema)
Was bringt es mir?      (Result / Solution)
```
Untertitel-Formel: `[Pain Point] → [Result] + [Amplifier] + [weiterer Result]`
Beispiel: „Upgrade Your Brain, Learn Anything Faster & Unlock Your Exceptional Life"

**Fiction** — Titel muss beantworten:
```
Ist das mein Genre / Sub-Genre?
Passt der Tone zu dem was ich suche?
```
Sub-Genre explizit nennen wenn das Cover es nicht eindeutig zeigt.
Beispiel: „A Lit RPG Gamelit Adventure" als Untertitel.

---

## Schritt 5: Buchbeschreibung keyword-bewusst verfassen

Amazon analysiert die Buchbeschreibung auf relevante Begriffe — identisch zur Auswertung von Rezensionen.

```
Schritt 1: Buchbeschreibung frei schreiben (Fokus: Emotion + Verkauf)
Schritt 2: Fertige Beschreibung mit Keyword-Liste abgleichen
Schritt 3: Passende Keywords dort einarbeiten wo sie natürlich passen
Schritt 4: Formulierungen so anpassen dass sie nach Zielgruppen-Sprache klingen

Doppelter Nutzen:
  Keywords in Beschreibung
    ├→ Amazon bestätigt Zuordnung → besseres Ranking
    └→ Zielgruppen-Sprache → höhere Conversion Rate
```

---

## Ausgabeformat

```
1. Keyword-Ideenliste
   Format: Tabelle oder Liste, gegliedert nach Kategorien
   Umfang: Mind. 5 Begriffe pro Kategorie

2. Bewertete Shortlist
   Format: Tabelle: Phrase | Relevanz | Volumen | Verkäufe | Score | Empfehlung
   Markierung: Spezifik-Box (S) oder Kombinations-Box (K)

3. Sieben Boxen Vorschlag
   Format: Box 1–7 mit konkretem Inhalt (copy-paste-fertig, inkl. Zeichenanzahl)
   Markierung: Spezifik (S) oder Kombination (K)
   Hinweis: Welche Box(en) für Kategorie-Keywords reserviert

4. Titelvorschlag
   Format: Haupttitel + Untertitel
   Nachweis: Welche Keywords wo eingebaut wurden

5. Beschreibungs-Hinweise
   Format: Liste konkreter Phrasen zum natürlichen Einbauen
   Umfang: Mind. 8–10 Phrasen
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
> Relevanz und Conversion — nicht allein das Suchvolumen.
