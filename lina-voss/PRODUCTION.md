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
│   ├── stil-briefing.md              ← Prosa-Regelwerk für KI-Agenten
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

#### Szene-für-Szene-Workflow

Jedes Kapitel wird in **2–4 nummerierte Szenen** geschrieben, nicht als Ganzes. Die Outline definiert pro Kapitel die Szenen-Blöcke mit Wortzielen.

**Warum:** Ein ganzes Kapitel (4.000+ Wörter) überschreitet regelmäßig das Output-Limit. Pro Szene (~1.000–1.800 Wörter) bleibt die Qualität hoch und der User kann zwischen Szenen steuern.

**Ablauf pro Kapitel:**
```
1. Szene 1 prompten → Output (~1.000–1.800 W)
2. User checkt / gibt Feedback
3. Szene 2 prompten (mit letztem Absatz aus Szene 1 als Übergang)
4. ... bis alle Szenen des Kapitels fertig
5. Kapitel-Checkliste (stil-briefing.md §12) prüfen
6. Continuity aktualisieren (04_continuity.md)
7. → Nächstes Kapitel
```

#### Context-Loading pro Szene
Jede Szene bekommt:
1. `serie/00_serien_bibel.md` (Kurzversion — nur Bögen + Steaminess)
2. `serie/figuren/[protagonist].md` + `serie/figuren/[love_interest].md`
3. `serie/figuren/[nebenfiguren die in der Szene vorkommen].md` (selektiv!)
4. `bandXX/02_outline.md` — Szenen-Block für diese Szene + Kapitel-Kontext
5. `bandXX/04_continuity.md` (aktueller Stand)
6. Vorherige Szene(n) des Kapitels (oder letzte 500 Wörter des Vorkapitels bei Szene 1)
7. **`bandXX/stil-briefing.md`** (Prosa-Regelwerk — PFLICHTLEKTÜRE)

#### Schreibregeln — Struktur
- **Kapitel-Ziel:** 3.500–4.750 Wörter pro Kapitel, verteilt auf 2–4 Szenen
- **Szenen-Ziel:** 1.000–1.800 Wörter pro Szene (nie über 2.000)
- **Gesamtlänge Band:** 350–400 Seiten (~80.000–95.000 Wörter)
- **POV:** Dual POV (sie + er) im Wechsel, KEIN Head-Hopping innerhalb eines Kapitels
- **Subtilität:** „Er hat es sich gemerkt"-Momente werden NICHT erklärt. Kein Erzählerkommentar. Die Leserin soll es selbst entdecken.
- **Steamy-Szenen:** Emotional verankert. Keine Szene ohne vorherige Tension-Aufbau über mindestens 2 Kapitel.
- **Szenen-Übergänge:** Jede Szene endet an einem natürlichen Punkt (Ortswechsel, Zeitsprung, Stimmungswechsel). Die nächste Szene knüpft nahtlos an.

#### Schreibregeln — Prosa-Stil
→ **Vollständiges Regelwerk: `bandXX/stil-briefing.md`** (PFLICHT — vor dem Schreiben lesen!)

Kurzfassung der wichtigsten Regeln:
- **Deep POV:** Kein Erzählerkommentar, kein „sie dachte". Leser = Figur.
- **Emotion zeigen:** Körperreaktion statt Benennung. Nie „sie fühlte Traurigkeit".
- **Dialog:** 70% Beats, 20% „sagte", 10% ohne Tag. Kein hauchte/zischte/knurrte.
- **Figurenstimmen:** Leon = knapp, keine Adjektive. Nora = wärmer, Humor als Schutzschild. Carla = präzise, kontrolliert. (Details im Stil-Briefing Abschnitt 3.4)
- **Rhythmus:** Fließtext als Standard. Kurze Sätze NUR für Wirkung (max. 3 Ein-Wort-Sätze/Kapitel). Absatzwechsel bei Sprecherwechsel oder Stimmungswechsel — nicht nach jedem Satz.
- **Anti-Patterns:** 20 verbotene Formulierungen + Wort-Wiederholungs-Limits im Stil-Briefing (Abschnitt 10).
- **Checkliste:** Jedes Kapitel nach der letzten Szene gegen die 10-Punkte-Checkliste im Stil-Briefing prüfen (Abschnitt 12).

#### Session-Aufteilung
```
Session A: Kapitel 1–5 (Akt 1: Setup)        → ~12–16 Szenen
Session B: Kapitel 6–10 (Akt 2a: Annäherung)  → ~12–16 Szenen
Session C: Kapitel 11–15 (Akt 2b: Eskalation) → ~12–16 Szenen
Session D: Kapitel 16–20 (Akt 3: Resolution)   → ~12–16 Szenen
```

⚠️ **PAUSE nach jeder Szene:** User kann Feedback geben oder direkt weiter prompten.

⚠️ **PAUSE nach jedem Kapitel:** User liest das fertige Kapitel. Änderungen werden vor dem nächsten Kapitel eingearbeitet.

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
  - Wiederholungen (Wörter, Gesten, Beschreibungen) → Limits in `stil-briefing.md` Abschnitt 10.2
  - Erzählerkommentare die Subtilität zerstören
  - Figurenstimmen-Konsistenz → Muster in `stil-briefing.md` Abschnitt 3.4
  - Anti-Pattern-Scan → Verbotsliste in `stil-briefing.md` Abschnitt 10.1
  - Umlaute/ß
  - Kapitel-Länge (Minimum 2.500 Wörter)
  - **Abgabe-Checkliste** → `stil-briefing.md` Abschnitt 12
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

> **Vollständiges Prosa-Regelwerk:** → `bandXX/stil-briefing.md`
> Enthält: Deep-POV-Regeln, Body-Language-Lexikon, Dialog-Mechanik, Anti-Pattern-Verbotsliste (20 Einträge), Wort-Limits, Frequenz-Tabelle, Abgabe-Checkliste.

### Subtilität
- KEINE Erzählerkommentare die erklären was die Figur fühlt statt es zu zeigen → Details: Stil-Briefing §1 (Deep POV) + §2 (Emotion zeigen)
- KEINE „sie merkte dass er sich verändert hatte"-Sätze → stattdessen: zeigen WAS sich verändert hat
- „Er hat es sich gemerkt"-Momente: Plant & Payoff ohne Spotlight. Niemand kommentiert es.
- Die Leserin soll sich schlauer fühlen als die Protagonistin
- Die „Fast"-Technik für emotionale Risse: → Stil-Briefing §5

### Figurenstimmen
- **Leon:** Kurze Sätze. Wenig Adjektive. Handlung statt Worte. Wenn er redet, zählt jedes Wort.
- **Nora:** Wärmer, bildhafter, Humor. Aber wenn die Maske fällt: kürzer, ehrlicher, verletzlich.
- **Carla:** Präzise, kontrolliert, professionell. Innerer Monolog = Selbstkritik auf Dauerschleife.
- Dialog-Muster pro Figur: → Stil-Briefing §3.4

### Steamy-Szenen
- Jede Szene braucht einen emotionalen Auslöser (nicht: „es passierte einfach")
- Minimum 2 Kapitel Tension-Aufbau vor der ersten Szene
- Sprache: sinnlich aber nicht klinisch. Keine Euphemismen, aber auch kein Porno.
- Referenz-Level: Nalini Singh (Psy-Changeling Serie) — steamy, emotional verankert, nie gratuitous
- Sensorische Spannung aufbauen: → Stil-Briefing §4 (5 Sinneskanäle, Berührungs-Limits, Distanz-Progression)

### Anti-Patterns (VERBOTEN)
- ❌ Mary Sue (keine Figur die alles kann, bei allen beliebt ist und keine echten Schwächen hat)
- ❌ Manic Pixie Dream Girl (Nora existiert nicht um Leon zu retten)
- ❌ Bella-Swan-Syndrom (Eigenschaften als Label statt als Verhalten)
- ❌ Insta-Love (jede Annäherung muss verdient sein)
- ❌ Big Misunderstanding als einziger Akt-3-Konflikt
- ❌ Billionaire/CEO-Klischee (Leon ist Chef, kein Milliardär. Alter Audi, keine Penthouse-Suite.)
- ❌ „Er hat es sich gemerkt" als expliziten Dialog oder Erzählerkommentar
- ❌ Deus Ex Machina / Zufälle die den Plot lösen
- ❌ 20 weitere verbotene Formulierungen (KI-typische Klischees): → Stil-Briefing §10.1

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
