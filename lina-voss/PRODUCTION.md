# Roman-Produktion: Die Hartmann-Agentur
*Pseudonym: Lina Elise Voss | 6-Band-Serie | WIP*

> Dieses Produktionssystem ist für die Hartmann-Agentur-Serie optimiert.
> Es unterscheidet sich vom Standard-Workflow (CLAUDE.md) durch **mehr Kontrolle,
> vorgebaute Figuren und Serien-Kontinuität.**

---

## Sprache — PFLICHT

Alle Outputs MÜSSEN korrekte deutsche Rechtschreibung verwenden:
- **Immer echte Umlaute:** Ä Ö Ü ä ö ü — NIEMALS ae, oe, ue als Ersatz
- **Immer ß:** straße, großer, heißt — NIEMALS ss als Ersatz (außer nach kurzem Vokal: dass, muss, Schluss)
- Das gilt für ALLE .md-Dateien — Manuskript, Outline, Listing, Cover-Prompts

---

## Kernprinzip: Kontrolle statt Automatik

| Standard-Workflow (CLAUDE.md) | Dieser Workflow |
|-------------------------------|-----------------|
| Briefing → 10 Schritte automatisch | **Jeder Schritt braucht Freigabe** |
| Charaktere werden generiert | **Charaktere sind vorgebaut** (serie/figuren/) |
| Einzelnes Buch | **Serien-Kontext** fließt in jedes Kapitel |
| 3 Pause-Punkte | **Pause nach JEDEM Schritt** |
| Continuity innerhalb eines Buchs | **Continuity über die gesamte Serie** |

---

## Verzeichnisstruktur

```
lina-voss/
├── PRODUCTION.md                    ← diese Datei
├── serie/
│   ├── 00_serien_bibel.md           ← Serienüberblick, Bögen, Struktur
│   └── figuren/
│       ├── leon.md                   ← + alle weiteren Figuren
│       ├── leon_li.md (Nora)
│       ├── carla.md
│       ├── jakob.md
│       ├── maren.md
│       ├── nils.md
│       └── tom.md
├── band01/
│   ├── briefing.json
│   ├── 00_status.md
│   ├── 01_ending.md
│   ├── 02_outline.md
│   ├── 03_kapitelplan.md            ← NEU: detaillierter Plan pro Kapitel
│   ├── 04_continuity.md
│   ├── 05_manuscript.md
│   ├── 06_editing_report.md
│   ├── 07_kdp_listing.md
│   └── 08_cover_prompts.md
├── band02/
│   └── ...
└── serien_continuity.md             ← NEU: bandübergreifende Kontinuität
```

---

## Workflow pro Band

### PHASE 0: Vorbereitung
- Lese `serie/00_serien_bibel.md`
- Lese ALLE relevanten Figuren-Dateien für diesen Band
- Lese `serien_continuity.md` (ab Band 2)
- Erstelle `bandXX/00_status.md`
- Zeige dem User: „Figuren geladen, Serien-Stand gelesen. Bereit."

⚠️ **PAUSE:** Warte auf Freigabe.

---

### PHASE 1: Ending
- Lese `skills/02_ending.md`
- Generiere 3 Ending-Varianten basierend auf:
  - Figuren-Dateien (Protagonist + Love Interest)
  - Serien-Bibel (übergreifender Bogen)
  - Trope des Bands
- Speichere als `bandXX/01_ending.md`

⚠️ **PAUSE:** Zeige alle Varianten. Warte auf User-Auswahl.

---

### PHASE 2: Outline
- Lese `skills/04_outline.md`
- Erstelle Kapitelstruktur (3-Akt-Struktur) basierend auf:
  - Gewähltes Ending
  - Figuren-Wunden und Bögen
  - Serien-Teaser (welche Nebenfiguren brauchen Szenen für ihren eigenen Band?)
- Speichere als `bandXX/02_outline.md`

⚠️ **PAUSE:** Zeige Outline. User kann ändern, ergänzen, streichen.

---

### PHASE 3: Kapitelplan (NEU — gibt es im Standard-Workflow nicht)
- Erstelle für JEDES Kapitel einen Detailplan:
  - POV (wer erzählt?)
  - Anwesende Figuren
  - Emotionaler Kern (was fühlt die Leserin?)
  - Plot-Fortschritt
  - „Er hat es sich gemerkt"-Momente / subtile Details (wo relevant)
  - Serien-Teaser (wo relevant)
  - Steamy-Szene (wo relevant, mit emotionalem Anker)
- Speichere als `bandXX/03_kapitelplan.md`

⚠️ **PAUSE:** User reviewt jeden Kapitelplan. Änderungen werden eingearbeitet.

---

### PHASE 4: Schreiben

#### Context-Loading pro Kapitel
Jeder Kapitel-Agent bekommt:
1. `serie/00_serien_bibel.md` (Kurzversion — nur Bögen + Steaminess)
2. `serie/figuren/[protagonist].md` + `serie/figuren/[love_interest].md`
3. `serie/figuren/[nebenfiguren die im Kapitel vorkommen].md` (selektiv!)
4. `bandXX/02_outline.md` (Gesamtstruktur)
5. `bandXX/03_kapitelplan.md` (Detail für dieses Kapitel)
6. `bandXX/04_continuity.md` (aktueller Stand)
7. Letzte 500 Wörter des Vorkapitels (Ton-Übergang)

#### Schreibregeln
- **Mindestlänge:** 2.500 Wörter pro Kapitel (Ziel: 3.000)
- **Gesamtlänge Band:** 350–400 Seiten (~80.000–95.000 Wörter)
- **POV:** Dual POV (sie + er) im Wechsel, KEIN Head-Hopping innerhalb eines Kapitels
- **Subtilität:** „Er hat es sich gemerkt"-Momente werden NICHT erklärt. Kein Erzählerkommentar. Die Leserin soll es selbst entdecken.
- **Steamy-Szenen:** Emotional verankert. Keine Szene ohne vorherige Tension-Aufbau über mindestens 2 Kapitel.
- **Figurenstimmen:** Jeder Cousin spricht anders. Leon = kurze Sätze, keine Adjektive. Nora = wärmer, bildhafter. Carla = präzise, kontrolliert.

#### Session-Aufteilung
```
Session A: Kapitel 1–5 (Akt 1: Setup)
Session B: Kapitel 6–10 (Akt 2a: Annäherung + Komplikation)
Session C: Kapitel 11–15 (Akt 2b: Eskalation + Midpoint)
Session D: Kapitel 16–20 (Akt 3: Krise + Resolution)
```

⚠️ **PAUSE nach jedem Kapitel:** User liest und gibt Feedback. Änderungen werden vor dem nächsten Kapitel eingearbeitet.

⚠️ **PAUSE nach jedem Akt:** Continuity-Review. Alle Figuren-Auftritte, offene Fäden, Ton prüfen.

#### Continuity-Updates
- Nach JEDEM Kapitel: `bandXX/04_continuity.md` aktualisieren
- Nach jedem Akt: Review + Serien-Continuity prüfen
- Nach Abschluss des Bands: `serien_continuity.md` aktualisieren

---

### PHASE 5: Lektorat
- Lese `skills/06_editing.md`
- Prüfe auf:
  - Konsistenz (Namen, Orte, Zeitabläufe)
  - POV-Brüche
  - Wiederholungen (Wörter, Gesten, Beschreibungen)
  - Erzählerkommentare die Subtilität zerstören
  - Figurenstimmen-Konsistenz
  - Umlaute/ß
  - Kapitel-Länge (Minimum 2.500 Wörter)
- Speichere als `bandXX/06_editing_report.md`

⚠️ **PAUSE:** User entscheidet welche Korrekturen umgesetzt werden.

---

### PHASE 6: Testleserin
- Generiere Testleserin-Feedback aus 3 Perspektiven:
  - **Casual Reader:** Unterhaltungswert, Spannung, Lesbarkeit
  - **Romance-Kennerin:** Trope-Execution, Chemistry, Steamy-Balance
  - **Serien-Leserin:** Teaser-Wirkung, Lust auf Band X+1, Figuren-Neugier
- Speichere als `bandXX/06b_testleserin.md`

⚠️ **PAUSE:** User bewertet Feedback und entscheidet über Änderungen.

---

### PHASE 7: KDP Listing + Cover
- Lese `skills/07_listing.md` + `skills/07a_keywords.md` + `skills/07b_kategorie_strategie.md`
- Lese `research/publisher_rocket/keyword_auswertung_lina_voss.md`
- Erstelle Listing mit 7 Keyword-Boxen
- Erstelle 3 Cover-Konzepte/Prompts
- Speichere als `bandXX/07_kdp_listing.md` + `bandXX/08_cover_prompts.md`

⚠️ **PAUSE:** User wählt Cover-Variante und reviewt Listing.

---

### PHASE 8: Abschluss
- Aktualisiere `serien_continuity.md` mit allem aus diesem Band
- Aktualisiere `serie/00_serien_bibel.md` (Bögen fortschreiben)
- Erstelle `bandXX/FINAL_SUMMARY.md`
- Update Memory

---

## Serien-Continuity (bandübergreifend)

`serien_continuity.md` wird nach jedem Band aktualisiert und enthält:

```markdown
# Serien-Continuity: Die Hartmann-Agentur

## Beziehungsstatus aller Paare
- Leon & Nora: [Stand nach Band X]
- Jakob & [LI]: [Stand]
- etc.

## Familiendynamik
- Leon ↔ Carla: [aktueller Stand, letzte Interaktion]
- Leon ↔ Nils: [Konflikt-Level]
- etc.

## Laufende Plotfäden
- Opas Gesundheit: [Stand]
- Wer führt die Agentur: [Stand]
- Matthias' Entschuldigung: [noch nicht / passiert in Band X]

## Agentur-Status
- Kunden: [wer gewonnen/verloren]
- Mitarbeiter: [wer neu/weg]
- Finanziell: [stabil/krise]

## Running Gags / Motive
- Opas Werbesprüche: [Liste mit Band-Referenz]
- Leons 2-Uhr-Nächte → 18-Uhr-Bogen
- Sonntagsmail
- etc.

## Offene Teaser
- [Was angedeutet wurde] → muss in Band X aufgelöst werden
```

---

## Qualitätsregeln (PFLICHT)

### Subtilität
- KEINE Erzählerkommentare die erklären was die Figur fühlt statt es zu zeigen
- KEINE „sie merkte dass er sich verändert hatte"-Sätze → stattdessen: zeigen WAS sich verändert hat
- „Er hat es sich gemerkt"-Momente: Plant & Payoff ohne Spotlight. Niemand kommentiert es.
- Die Leserin soll sich schlauer fühlen als die Protagonistin

### Figurenstimmen
- **Leon:** Kurze Sätze. Wenig Adjektive. Handlung statt Worte. Wenn er redet, zählt jedes Wort.
- **Nora:** Wärmer, bildhafter, Humor. Aber wenn die Maske fällt: kürzer, ehrlicher, verletzlich.
- **Carla:** Präzise, kontrolliert, professionell. Innerer Monolog = Selbstkritik auf Dauerschleife.
- **[weitere Stimmen werden ergänzt wenn Figuren entwickelt sind]**

### Steamy-Szenen
- Jede Szene braucht einen emotionalen Auslöser (nicht: „es passierte einfach")
- Minimum 2 Kapitel Tension-Aufbau vor der ersten Szene
- Sprache: sinnlich aber nicht klinisch. Keine Euphemismen, aber auch kein Porno.
- Referenz-Level: Nalini Singh (Psy-Changeling Serie) — steamy, emotional verankert, nie gratuitous

### Anti-Patterns (VERBOTEN)
- ❌ Mary Sue (keine Figur die alles kann, bei allen beliebt ist und keine echten Schwächen hat)
- ❌ Manic Pixie Dream Girl (Nora existiert nicht um Leon zu retten)
- ❌ Bella-Swan-Syndrom (Eigenschaften als Label statt als Verhalten)
- ❌ Insta-Love (jede Annäherung muss verdient sein)
- ❌ Big Misunderstanding als einziger Akt-3-Konflikt
- ❌ Billionaire/CEO-Klischee (Leon ist Chef, kein Milliardär. Alter Audi, keine Penthouse-Suite.)
- ❌ „Er hat es sich gemerkt" als expliziten Dialog oder Erzählerkommentar
- ❌ Deus Ex Machina / Zufälle die den Plot lösen

---

## Status: WIP

- [x] Serien-Bibel erstellt
- [x] Figur: Leon (komplett)
- [x] Figur: Nora (komplett)
- [x] Figur: Carla (komplett inkl. Band-1-Szenen)
- [ ] Figur: Jakob
- [ ] Figur: Maren
- [ ] Figur: Nils
- [ ] Figur: Tom
- [ ] Love Interests Band 2–6
- [ ] Briefing Band 1
- [ ] Produktion Band 1
