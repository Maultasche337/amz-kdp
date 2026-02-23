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

### PHASE 0.5: Cover-Ästhetik & Figuren-Optik (VOR dem Schreiben!)
Muss VOR dem Schreiben passieren — die Optik der Figuren beeinflusst die Prosa (Beschreibungen, erste Eindrücke, steamy Szenen).

- **Bei Band 1:** Cover-Stil festlegen (illustriert, Farbpalette, Komposition). Test-Cover generieren via Replicate/FLUX. Figuren-Optik aller Hauptfiguren definieren und in die Figurendateien eintragen.
- **Ab Band 2:** Prüfen ob der Serien-Stil beibehalten wird. Nur neue Figuren (Love Interest) optisch definieren.
- Cover-Prompts speichern als `bandXX/08_cover_prompts.md` (Entwürfe — finale Cover nach Lektorat)
- Figuren-Optik in `serie/figuren/[name].md` unter Sektion "Optik" eintragen

⚠️ **PAUSE:** User prüft Cover-Tests und bestätigt Figuren-Optik.

---

### Cover-Qualitätscheckliste (gilt für Phase 0.5 UND Phase 7)

#### Die 5 Cover-Todsünden
1. **Für niemanden designt** — Die Zielleserin (Frauen 25–45, Spicy Romance) muss in 3 Sekunden denken: „Das ist für MICH." Kein generisches Cover das jeden ansprechen will und niemanden trifft.
2. **Thumbnail-Fail** — Das Cover MUSS bei 100px Breite funktionieren (so groß ist es auf Amazon). Titel lesbar? Bild erkennbar? Wenn nicht → zurück ans Reißbrett.
3. **Klon-Falle** — Trends kennen, aber differenzieren. Wenn das Cover im Amazon-Suchergebnis neben der Konkurrenz untergeht, verkauft es nicht. Auffallen durch eigenen Stil, nicht durch Kopie.
4. **Typografie-Fehler** — Max 2 Fonts. Klare Hierarchie: Titel dominant → Autorin → Untertitel/Reihe. Font-Ton muss zum Genre passen. Kein Comic Sans, kein Papyrus, keine unleserlichen Script-Fonts.
5. **Kompositions-Chaos** — Auge muss wissen wohin: Titel zuerst, dann Rest. Balance prüfen (kein schwerer Rand). Busy ≠ schlecht — aber nur wenn Hierarchie stimmt.

#### 2 Goldene Regeln vor dem Publish
1. **Thumbnail-Test:** Cover auf 100px verkleinern + Screenshot der Amazon-Suchergebnis-Seite machen + eigenes Cover reinsetzen. Fällt es auf? Ist der Titel lesbar?
2. **Squint-Test:** Augen zusammenkneifen und aufs Cover schauen. Was sieht man zuerst? Wenn die Antwort nicht „Titel" ist → Hierarchie anpassen.

#### Serien-spezifisch (Hartmann-Agentur)
- Wiedererkennbarer Serien-Stil über alle 6 Bände
- Farbcodierung pro Band möglich (vgl. Susie Tate)
- Autorinnen-Name „Lina Elise Voss" konsistent positioniert
- Serien-Branding: „Die Hartmann-Agentur" als Dachmarke erkennbar

---

### PHASE 1: Ending
- *(Ending-Methodik aus v1 deprecated — interaktiv erarbeiten)*
- Generiere 3 Ending-Varianten basierend auf:
  - Figuren-Dateien (Protagonist + Love Interest)
  - Serien-Bibel (übergreifender Bogen)
  - Trope des Bands
- Speichere als `bandXX/01_ending.md`

⚠️ **PAUSE:** Zeige alle Varianten. Warte auf User-Auswahl.

---

### PHASE 2: Outline
- *(Outline-Methodik aus v1 deprecated — interaktiv erarbeiten)*
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
- **Prosa-Stil:** KEIN Stakkato. Kapitel müssen sich lesen wie ein Roman, nicht wie eine Aufzählung kurzer Sätze. Absätze wie in Büchern üblich — Fließtext mit natürlichem Rhythmus. Kurze Sätze sind EIN Stilmittel (Leon-POV, Schockmomente), nicht der Standardton. Variation im Satzbau ist Pflicht: kurze Sätze für Wirkung, längere für Atmosphäre und innere Welt. Absatzwechsel bei Sprecherwechsel, Perspektivwechsel oder Stimmungswechsel — nicht nach jedem Satz.

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
- *(Lektorat-Methodik aus v1 deprecated — interaktiv erarbeiten)*
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
- Lese `research/wissen/kdp-listing-methodik.md` (Listing-Methodik + Amazon-Mechanik)
- Lese `research/wissen/keywords-lina-voss.md` (Keyword-Strategie)
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

### Figuren & Serie
- [x] Serien-Bibel erstellt
- [x] Alle 6 Cousins + Werner + Matthias + Henrik (komplett)
- [x] Alle 6 Love Interests (komplett)
- [x] Cover-Portraits alle 8 Figuren (komplett)

### Band 1 — Tageslicht
- [x] Briefing (`band01/briefing.json`)
- [x] Cover-Ästhetik & Portraits (Phase 0.5)
- [x] Ending: Variante C + Mail-PS aus B (`band01/01_ending.md`)
- [x] Outline + Kapitelplan: 20 Kapitel (`band01/02_outline.md`)
- [ ] Schreiben: Session A (Kap 1–5) ← **NÄCHSTER SCHRITT**
- [ ] Schreiben: Session B (Kap 6–10)
- [ ] Schreiben: Session C (Kap 11–15)
- [ ] Schreiben: Session D (Kap 16–20)
- [ ] Lektorat
- [ ] KDP Listing + Cover
