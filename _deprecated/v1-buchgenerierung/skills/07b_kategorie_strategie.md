# SKILL: Amazon KDP Kategorie-Strategie

## Zweck
Ermittelt für ein gegebenes Buch die optimalen drei Amazon-Kategorien nach dem 6-Schritt-System.
Berücksichtigt Duplikate (Bestseller-Leiter), Geisterkategorien und Kategorie-String-Anatomie.
Geeignet für alle Bücher auf amazon.de — besonders für Fiction-Genres wie Romance, Cozy Crime, Mystery.

## Einsatz
Wird aufgerufen von `07_listing.md` für die Kategorien-Sektion. Kann auch eigenständig
verwendet werden. Nach Abschluss → `07c_kategorie_keywords.md` für die passenden Keywords.

## Input (frage nach, falls nicht angegeben)
- Buchtitel und Kurzbeschreibung (2–3 Sätze)
- Genre und Subgenre (z. B. Cozy Crime, Romantasy, Historische Romance)
- Zielgruppe (Alter, Geschlecht, Lesevorlieben)
- Bereits bekannte Wettbewerbs-Titel (optional)
- Format: E-Book / Taschenbuch / beides

## Output
- Longlist (6–8 Kategorien)
- Finale Empfehlung (3 Kategorien mit vollständigen Strings und Begründung)
- Nächste Schritte für manuelle Verifikation

---

## Hintergrund: Warum Kategorieauswahl entscheidend ist

Amazon benutzt Kategorien für:
1. **Sichtbarkeit** — Bücher erscheinen in Kategorie-Browsing und Bestsellerlisten
2. **Bestseller-Badge** — Erreichbar wenn Buch genug Verkäufe für Platz 1 in einer Kategorie hat
3. **Algorithmus-Signal** — Kategorien beeinflussen, für welche Suchanfragen das Buch indexiert wird

---

## Analyseprozess: 6 Schritte

### Schritt 1 — Passende Kategorien identifizieren

Analysiere, welche Amazon-Kategorien inhaltlich zum Buch passen. Denke über mehrere Hauptkategorien hinaus — ein Genre wie „Cozy Crime" kann unter folgenden Hauptkategorien auftauchen:
- Krimi & Thriller
- Humor
- Belletristik / Allgemeine Literatur
- Frauen-/Unterhaltungsromane

Benenne mindestens 6–8 potenzielle Kategorien als Longlist mit vollständigem Kategorie-String.

Beispiel-Format:
`Kindle-Shop → Kindle-E-Books → Krimis & Thriller → Kriminalromane → Cosy-Krimis`

### Schritt 2 — Bestseller-Rang-Schwelle einschätzen

Kategorisiere jede Kategorie nach Wettbewerbsintensität:
- **Leicht** — geschätzt < 50 Verkäufe/Tag für Platz 1
- **Mittel** — geschätzt 50–200 Verkäufe/Tag für Platz 1
- **Schwer** — geschätzt > 200 Verkäufe/Tag für Platz 1

Für neue Bücher oder Bücher ohne großes Werbebudget: leichte bis mittlere Kategorien priorisieren.
Genaue Zahlen manuell über Amazon.de verifizieren oder Publisher Rocket nutzen.

### Schritt 3 — Duplikate prüfen und strategisch nutzen

Prüfe, ob Kategorien aus der Longlist **Duplikate** sind (verschiedene Kategorie-Strings führen zur selben Bestsellerliste).

**Duplikat-Vorteil — Bestseller-Leiter:**
Das Buch erscheint automatisch in allen übergeordneten Unterkategorien aller Duplikat-Strings.

**Regel:** Genau eine der drei Kategorien sollte ein Duplikat sein.

**Gutes Duplikat hat:**
- 3+ Kategorie-Strings
- Mindestens 2 verschiedene Hauptkategorien

**Prüfung:** Passen alle Kategorie-Strings des Duplikats inhaltlich zum Buch?
Passt ein String nicht → Duplikat verwerfen.

Kennzeichne Duplikate in der Empfehlung mit Hinweis, welche übergeordneten Kategorien dadurch erschlossen werden.

### Schritt 4 — Geisterkategorien ausschließen

**Geisterkategorien (Ghost Categories):**
- Keine auffindbare Kategorieseite auf Amazon
- Käufer können sie nicht über Navigation erreichen
- Kein Bestseller-Tag erreichbar
- 27 % aller KDP-Kategorien sind Geisterkategorien — manuell nicht zuverlässig erkennbar
- Publisher Rocket zur Identifikation empfehlen

**Absolute Ausnahme:** Ghost Category darf gewählt werden wenn der Kategorie-String inhaltlich einzigartig gut passt — dann prüfen ob die übergeordnete Unterkategorie noch attraktiv ist.

**Kritische Regel:** Niemals zwei Geisterkategorien aus derselben Unterkategorie — verschwendet zwei der drei Slots für de facto nur eine Platzierung.

### Schritt 5 — Drei finale Kategorien empfehlen

Klare Empfehlung für genau drei Kategorien als vollständige Kategorie-Strings. Für jede Kategorie:
1. Warum sie inhaltlich passt
2. Eingeschätzte Wettbewerbsintensität
3. Ob es sich um ein Duplikat handelt und welche Zusatz-Kategorien dadurch erschlossen werden
4. Ob Geisterkategorie-Verdacht besteht

**Ausgabe-Format:**
```
Kategorie 1 (Hauptwahl):
Kindle-Shop → Kindle-E-Books → Krimis & Thriller → Kriminalromane → Cosy-Krimis
→ Passt perfekt: Protagonistinnen-Duo, humorvoller Ton, kein Blut
→ Wettbewerb: Mittel
→ Kein Duplikat

Kategorie 2 (Duplikat-Wahl – Bestseller-Leiter):
Kindle-Shop → Kindle-E-Books → Humor & Satire → Humorvolle Romane
→ Duplikat mit: [weitere Strings nennen]
→ Erschließt zusätzlich: Humor & Satire (Hauptkategorie), Unterhaltungsromane
→ Wettbewerb: Leicht bis Mittel
→ Alle Strings passen inhaltlich ✓

Kategorie 3 (Backup / Reichweite):
Kindle-Shop → Kindle-E-Books → Belletristik → Frauenromane
→ Hohe Leserinnen-Reichweite
→ Wettbewerb: Schwer – nur empfehlen wenn Verkaufszahlen das erlauben
```

### Schritt 6 — Hinweis auf Kategorie-Keywords

Die gewählten Kategorien durch gezielte Keywords in den 7 KDP-Keyword-Feldern stützen.
1–2 der 7 Felder für kategoriespezifische Begriffe reservieren.
→ `skills/07c_kategorie_keywords.md` für die konkrete Keyword-Auswahl

---

## Vollständiges Ausgabe-Format

```
1. Buchanalyse
   Kurze Einschätzung des Genres und der Positionierung

2. Longlist
   6–8 potenzielle Kategorien mit vollständigen Strings

3. Shortlist-Analyse
   Bewertung nach: inhaltlicher Fit | Wettbewerb | Duplikat-Potenzial | Ghost-Risiko

4. Finale Empfehlung
   Die drei Kategorien mit vollständiger Begründung (Format wie oben)

5. Nächste Schritte
   Was der Nutzer manuell verifizieren oder in Publisher Rocket prüfen sollte
```

Schreibe auf Deutsch. Sei konkret und direkt. Vermeide vage Formulierungen wie
„könnte passen" — entweder passt eine Kategorie oder nicht.
