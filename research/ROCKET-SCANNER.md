# Rocket-Scanner
*Skill: Verarbeitet Publisher Rocket CSV-Exporte und integriert sie in die Wissensbasis*

---

## Aufruf

Sage: **"Scanne die Rocket-Exporte"** oder **"Neue Rocket-Daten verarbeiten"**

Drop-Zone: `research/incoming/rocket/`

---

## Schritt 1: Inventar & Typ-Erkennung

Lese alle CSVs in `research/incoming/rocket/`.

Erkenne den Typ am Dateinamen:
- `ANALYZED KEYWORD SEARCH` → **Keyword-Suche**
- `COMPETITION ANALYZER` → **Konkurrenz-Analyse**

Erkenne das Format am Dateinamen:
- `BOOK` = Taschenbuch-Daten (höhere Preise, andere Schwierigkeit)
- `EBOOK` = eBook-Daten (niedrigere Preise, andere Konkurrenz)

⚠️ **Book vs. eBook NICHT direkt vergleichen!** Immer Typ kennzeichnen.

Zeige dem User:

| # | Datei | Typ | Format | Suchbegriff | Datum |
|---|-------|-----|--------|-------------|-------|

**PAUSE:** "X Exporte gefunden. Für welches Pseudonym/Thema sind die? (Lina Voss / Maja Sternberg / allgemein)"

---

## Schritt 2: Keyword-Suche auswerten

### CSV-Spalten (Keyword Search)
```
Schlagwort | Durchschnittliche Seitenzahl | Anzahl Der Konkurrenten |
Durchschnittspreis | Durchschnittliches Monatliches Einkommen |
Geschätzte Amazon-suchanfragen Pro Monat | Amazon Searches/Month Color |
Schwierigkeitsgrad Der Konkurrenz | Competitive Score Color
```

### Auswertungslogik

> ⚠️ **Empfehlung: Nur Keywords mit ≥ 1.000 Suchen/Monat sind ernsthaft verfolgbar.**
> Alles darunter ist Nische pur — kann funktionieren als Zusatz-Keyword, aber NICHT als Haupt-Keyword für ein Buch.

Für JEDES Keyword in der CSV:

**1. Goldkeyword-Check:**
```
Goldkeyword = Difficulty ≤ 40 (Green) UND Einkommen ≥ 200 €
            ODER Difficulty ≤ 40 UND Suchen ≥ 1.000 (grün)
```

**2. Finger-weg-Check:**
```
Finger weg = Difficulty ≥ 70
           ODER Konkurrenten ≥ 50.000 ohne grüne Difficulty
```

**3. Tier-Einstufung:**

| Tier | Kriterien |
|------|-----------|
| **Tier 1** | Diff. ≤ 40 🟢 UND (Einkommen ≥ 400 € ODER Suchen ≥ 1.000 🟢) |
| **Tier 2** | Diff. ≤ 60 🟡 UND Einkommen ≥ 200 € UND Suchen ≥ 1.000 |
| **Tier 3** | Diff. ≤ 40 🟢 UND Suchen < 1.000 (Nische — nur als Zusatz-Keyword) |
| **⛔ Finger weg** | Diff. ≥ 70 🔴 ODER irrelevant |

**4. Einkommen-Plausibilität:**
- Einkommen > 3.000 € → **Ausreißer-Warnung** (vermutlich Mega-Seller verzerrt Durchschnitt)
- Regionale Keywords (150-300 €) = realistisch
- Genre-Keywords (3.000+ €) = mit Vorsicht

**5. Duplikat-Check:**
- Prüfe ob das Keyword bereits in einer bestehenden `wissen/keywords-*.md` Datei steht
- Wenn ja: Werte vergleichen — haben sich Difficulty/Einkommen verändert?

### Output pro CSV

```markdown
## [Suchbegriff] ([Book/eBook], [Datum])

### Goldkeywords gefunden: X
| Keyword | Suchen | Einkommen | Konk. | Diff. | Tier |
|---------|--------|-----------|-------|-------|------|
...

### Finger weg: X
| Keyword | Problem |
|---------|---------|
...

### Neue Entdeckungen (nicht in Wissensbasis)
...

### Veränderte Werte (bereits bekannte Keywords)
| Keyword | Alter Wert | Neuer Wert | Veränderung |
...
```

---

## Schritt 3: Competition Analyzer auswerten

### CSV-Spalten (Competition)
```
Title | Subtitle | Review Score | Ratings | Author | Age |
ABSR | # Of Pages | KWT | Price | DY Sales | MO Sales | Sales Page
```

### Auswertungslogik

**1. Top-Seller identifizieren:** Sortiere nach MO Sales (absteigend)

**2. Für jeden Eintrag:**
- €/Mo berechnen (aus MO Sales Spalte)
- Alter in Tagen → Monate umrechnen
- KWT aktiv? (Ja/Nein)
- Untertitel analysieren: Enthält Trope? Enthält Keywords?

**3. Muster erkennen:**
- Preis-Cluster: Was ist der Sweet Spot?
- Seiten-Range: Was erwartet die Leserin?
- Review-Score: Wie hoch muss die Qualität sein?
- KWT-Quote: Wie viele schalten Ads?
- Serien vs. Standalone: Was performt besser?
- Tote Bücher (ABSR > 500.000 oder 0 €/Mo): Was machen sie falsch?

**4. Konkurrenz-Profil erstellen:**
```markdown
## Competition: [Suchbegriff]

### Markt-Überblick
- Bücher analysiert: X
- Durchschnitt €/Mo: X €
- Median €/Mo: X €
- Top-Seller: [Titel] mit X €/Mo
- Preis-Range: X-X €
- Seiten-Range: X-X

### Funktionierende Bücher (>100 €/Mo)
| Titel | Autorin | €/Mo | Preis | Warum es funktioniert |
...

### Gescheiterte Bücher (<50 €/Mo)
| Titel | €/Mo | Warum gescheitert |
...

### Lektionen
1. ...
2. ...
```

---

## Schritt 4: In Wissensbasis integrieren

### Keyword-Daten → passende wissen/-Datei

| Kontext | Ziel-Datei |
|---------|-----------|
| Workplace, Office, Büro, Grumpy, Sunshine | `wissen/keywords-lina-voss.md` |
| ab 40, Neuanfang, Heimat, Region | `wissen/keywords-maja-sternberg.md` |
| Pseudonym-übergreifend oder neue Tier-1 | `wissen/keywords-goldkeywords.md` |

### Competition-Daten → passende wissen/-Datei

| Kontext | Ziel-Datei |
|---------|-----------|
| Neue Autorin entdeckt | `wissen/konkurrenz-autorinnen.md` |
| Lina-Voss-Nische | `wissen/konkurrenz-lina-voss.md` |
| Trope-Erkenntnisse | `wissen/trope-analyse.md` |
| Markt-Signale | `wissen/markt-trends-2026.md` |

### Update-Regeln
- Neue Goldkeywords → in die passende Tier-Tabelle einfügen
- Veränderte Werte → alten Wert überschreiben, Datum aktualisieren
- Neue Konkurrenz-Autorinnen → eigene Sektion in konkurrenz-autorinnen.md
- Geschlossene Wissenslücken → aus WISSENSBASIS.md streichen

**PAUSE:** Zeige Zusammenfassung der Änderungen vor dem Speichern.

---

## Schritt 5: Archivierung

Verschiebe verarbeitete CSVs:
- Keyword-CSVs → `quellen/publisher-rocket/csv/keyword/`
- Competition-CSVs → `quellen/publisher-rocket/csv/competition/`

---

## Schritt 6: WISSENSBASIS aktualisieren

1. Betroffene Themen: Datum aktualisieren
2. Wissenslücken: Geschlossene abhaken, neue hinzufügen
3. Melde: **"Fertig. X Keywords ausgewertet, Y Goldkeywords gefunden, Z Konkurrenten analysiert."**

---

## Qualitätsregeln

- **Book vs. eBook IMMER kennzeichnen** — Werte sind nicht vergleichbar
- **Einkommen-Ausreißer markieren** — Einzelne Mega-Seller verzerren Durchschnitt massiv
- **Difficulty-Farben aus CSV nutzen:** Green = 🟢, Yellow = 🟡, Red = 🔴
- **Suchen-Farben:** Green = bestätigtes Volumen 🟢, Yellow = geschätzt 🟡, Red = <50 🔴
- **Minimum-Empfehlung: 1.000 Suchen/Monat** — Keywords darunter nur als Zusatz, nie als Haupt-Keyword
- **"heimatroman" vs. "heimat roman"** — Leerzeichen macht Diff. 70→38, IMMER prüfen
- **Perplexity-Daten NIE als Vergleich nutzen** — 200-300× übertrieben
