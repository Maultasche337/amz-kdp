# SKILL: Kategorie-Keywords für KDP

## Zweck
Generiert kategoriespezifische Keywords für 1–2 der 7 KDP-Keyword-Felder.
Diese stärken die Amazon-Algorithmus-Zuordnung zu den gewählten Kategorien.

## Einsatz
Nach `07b_kategorie_strategie.md` (Kategorieauswahl). Ergebnis fließt in
die Kombinations-Boxen 5–7 des vollständigen Keyword-Plans (`07a_keywords.md`).

## Hintergrund: Warum Kategorie-Keywords entscheidend sind

Amazon prüft kontinuierlich anhand der Buch-Metadaten (Titel, Untertitel, Beschreibung,
Rezensionen, Look Inside und vor allem Keywords), ob ein Buch thematisch in die gewählten
Kategorien passt. Fehlen aussagekräftige Begriffe, kann Amazon das Buch aus einer Kategorie
entfernen — auch wenn der Autor sie korrekt gewählt hat.

**Faustregel:** 1–2 der 7 KDP-Keyword-Felder für kategoriespezifische Begriffe reservieren.

## Input (frage nach, falls nicht angegeben)
- Die drei gewählten Amazon-Kategorien (vollständige Kategorie-Strings)
- Buchtitel, Untertitel und Kurzbeschreibung
- Genre-spezifische Merkmale (z. B. Protagonistin 40+, Dorfsetting, Humor, kein Blut, Tierbegleiter)
- Bereits geplante Keywords in den anderen 5–6 Feldern (optional, zur Abstimmung)

---

## Analyseprozess: 4 Schritte

### Schritt 1 — Kategorie-Strings auswerten

Jeden Kategorie-String Wort für Wort durchgehen. Bedeutungstragende Begriffe aus dem
String selbst sind stärkste Signalwörter für den Algorithmus.

Beispiel:
`Kindle-Shop → Kindle-E-Books → Krimis & Thriller → Kriminalromane → Cosy-Krimis`

Signalwörter: `Cosy-Krimi`, `Cosy Crime`, `Cozy Mystery`, `Kriminalroman`, `Krimi`

Für alle drei Kategorien Signalwörter getrennt notieren.

### Schritt 2 — Genre-Konventions-Keywords ergänzen

Begriffe ergänzen, die Leser dieses Genres typischerweise suchen und inhaltlich zum Buch passen:

- **Tropes und Motifs** (z. B. für Cozy Crime: `amateur detective`, `village mystery`, `small town crime`, `female detective`, `whodunit`)
- **Setting-Keywords** (z. B. `Bayern`, `Alpen`, `Dorf`, `Kleinstadt`, `Provinz`)
- **Protagonisten-Keywords** (z. B. `Ermittlerin`, `Frauenroman`, `Protagonistin 40+`, `Frauenfreundschaft`)
- **Stimmungs-Keywords** (z. B. `humorvoll`, `leichte Lektüre`, `feel-good`, `entspannend`)
- **Serien-Keywords** falls zutreffend (z. B. `Krimi-Reihe`, `Ermittler-Duo`)

### Schritt 3 — Duplikat-Kategorie-Keywords priorisieren

Falls eine der drei Kategorien ein Duplikat mit mehreren Kategorie-Strings ist:
Signalwörter aus ALLEN zugehörigen Strings identifizieren, nicht nur dem gewählten.
Jedes Signalwort aus einem Duplikat-String stärkt die Präsenz in allen verknüpften
Kategorien gleichzeitig.

### Schritt 4 — Keyword-Felder befüllen

Konkrete Keyword-Vorschläge für genau 1–2 der 7 KDP-Felder erstellen (à max. 50 Zeichen).

**Priorisierungsregel:**
1. Zuerst: Wörter direkt aus den Kategorie-Strings
2. Dann: Starke Genre-Tropes und Motive
3. Zuletzt: Setting, Stimmung, Zielgruppe

Für jedes vorgeschlagene Keyword-Feld angeben:
- Den konkreten Inhalt (copy-paste-fertig)
- Die Zeichenanzahl
- Welche Kategorie(n) damit gestärkt werden

---

## Ausgabe-Format

### Kategorie-Analyse
Für jede der drei Kategorien: vollständiger String + extrahierte Signalwörter

### Keyword-Pool
Alle gesammelten relevanten Begriffe, gruppiert nach:
- Direkte Kategorie-Signalwörter
- Genre-Tropes & Motive
- Setting & Atmosphäre
- Zielgruppe & Protagonisten

### Finale Keyword-Felder (1–2 Felder)
```
Feld X: [konkreter Inhalt, kommagetrennt]
Zeichen: XX/50
Stärkt: Kategorie 1 + Kategorie 2
```

### Hinweise zur Integration
Kurze Empfehlung, wie die Kategorie-Keywords mit den verbleibenden 5–6 regulären
Keyword-Feldern harmonieren (keine Überschneidungen, sinnvolle Ergänzung).

---

## Qualitätskriterien

- Jeder Begriff muss inhaltlich zum Buch passen — kein Keyword-Stuffing
- Deutsche UND englische Begriffe verwenden (deutsche Amazon-Käufer suchen in beiden Sprachen)
  Beispiel: `Cozy Mystery` UND `Gemütlicher Krimi`
- Generische Begriffe ohne Kategoriebezug vermeiden (z. B. `Roman`, `Buch`, `lesen`)
- Zeichenlimit prüfen: Jedes Feld max. 50 Zeichen
- Auf Deutsch schreiben, Fachbegriffe wie `Cozy Crime`, `Trope`, `KDP` unübersetzt lassen

---

## Beispiel-Output

**Buch:** Cozy Crime, weibliches Ermittlungs-Duo, bayerisches Dorf, humorvoll, Protagonistinnen 50+

**Kategorie 1:** `Kindle-E-Books → Krimis & Thriller → Cosy-Krimis`
**Kategorie 2:** `Kindle-E-Books → Humor → Humorvolle Romane` (Duplikat)
**Kategorie 3:** `Kindle-E-Books → Frauen-Unterhaltungsromane`

**Feld 6 (Kategorie-Keywords):**
```
Cozy Mystery, Cosy-Krimi, Ermittlerinnen-Duo
Zeichen: 42/50
Stärkt: Kategorie 1 + 2
```

**Feld 7 (Kategorie-Keywords):**
```
Frauenfreundschaft, Bayern, Dorfkrimi, humorvoll
Zeichen: 47/50
Stärkt: Kategorie 2 + 3
```
