# KDP-Produktions-Projekt

Du unterstützt bei der Produktion deutschsprachiger Nischen-Romane für Amazon KDP.
Arbeitsweise: **interaktiv, Schritt für Schritt, mit Freigabe** — keine automatisierte Pipeline.

---

## Sprache — PFLICHT

Alle Outputs MÜSSEN korrekte deutsche Rechtschreibung verwenden:
- **Immer echte Umlaute:** Ä Ö Ü ä ö ü — NIEMALS ae, oe, ue als Ersatz
- **Immer ß:** Straße, großer, heißt — NIEMALS ss als Ersatz (außer nach kurzem Vokal: dass, muss, Schluss)
- Gilt für ALLE .md-Dateien — Manuskript, Outline, Listing, Cover-Prompts, Wissensbasis

---

## Projektstruktur

```
amz-kdp/
├── CLAUDE.md                        ← diese Datei
├── PSEUDONYM.md                     ← Übersicht aller 3 Pseudonyme
│
├── lina-voss/                       ← AKTIV — Spicy Contemporary Romance
│   ├── PRODUCTION.md                ← Produktions-Workflow (HIER lesen vor jedem Schritt!)
│   ├── serie/
│   │   ├── 00_serien_bibel.md       ← Serienüberblick, Bögen, Struktur
│   │   ├── agentur_rollen.md        ← Agentur-Referenz
│   │   └── figuren/                 ← Alle Figurenprofile (Cousins + Love Interests)
│   └── band01/                      ← Produktion Band 1 (Leon × Nora)
│
├── research/                        ← Wissensbasis & Recherche
│   ├── WISSENSBASIS.md              ← Master-Index aller Wissens-Themen
│   ├── WISSENS-SCANNER.md           ← Skill: Neues Material verarbeiten
│   ├── ROCKET-SCANNER.md            ← Skill: Publisher Rocket CSV-Exporte verarbeiten
│   ├── wissen/                      ← Konsolidiertes Wissen (HIER lesen)
│   ├── quellen/                     ← Rohdaten & Originalanalysen
│   └── incoming/                    ← Neues Material ablegen, dann scannen
│       └── rocket/                  ← Publisher Rocket CSV-Exporte ablegen
│
├── _parked/                         ← Geparkte Pseudonyme
│   ├── monika-huber/                ← Cozy Crime (hanni_beate_001 fertig)
│   └── maja-sternberg/              ← Clean Heimat-Romance 40+
│
└── _deprecated/                     ← Altes v1-System (nur Referenz)
    └── v1-buchgenerierung/          ← Automatisierte Pipeline (nicht mehr nutzen)
```

---

## Drei Pseudonyme

| Pseudonym | Genre | Status |
|-----------|-------|--------|
| **Lina Elise Voss** | Spicy Contemporary Romance (Workplace, Hamburg) | ✅ AKTIV — Band 1 als nächstes |
| Monika Huber | Cozy Crime (Hanni & Beate, Eifel) | ⏸️ Geparkt (Band 1 fertig) |
| Maja Sternberg | Clean Heimat-Romance 40+ (Allgäu/Tirol) | ⏸️ Geparkt |

Details zu allen Pseudonymen: `PSEUDONYM.md`

---

## Workflows

### Roman schreiben (Lina Voss)
→ Lese **`lina-voss/PRODUCTION.md`** — enthält den kompletten Workflow mit Phasen, Qualitätsregeln, Session-Aufteilung und Continuity-Tracking.

### Neues Recherche-Material verarbeiten
→ User sagt: **„Scanne den incoming-Ordner"**
→ Folge `research/WISSENS-SCANNER.md`

### Publisher Rocket CSVs auswerten
→ User sagt: **„Scanne die Rocket-Exporte"**
→ Folge `research/ROCKET-SCANNER.md`

### Wissensbasis nachschlagen
→ Starte bei `research/WISSENSBASIS.md` — dort steht welche Datei welches Thema abdeckt.

---

## Wissens-Dateien (Kurzreferenz)

| Thema | Datei |
|-------|-------|
| Markt & Trends 2026 | `research/wissen/markt-trends-2026.md` |
| Goldkeywords (alle) | `research/wissen/keywords-goldkeywords.md` |
| Keywords Lina Voss | `research/wissen/keywords-lina-voss.md` |
| Keywords Maja Sternberg | `research/wissen/keywords-maja-sternberg.md` |
| Konkurrenz-Autorinnen | `research/wissen/konkurrenz-autorinnen.md` |
| Konkurrenz Lina Voss | `research/wissen/konkurrenz-lina-voss.md` |
| Launch-Operationen | `research/wissen/launch-operationen.md` |
| Regionale Settings | `research/wissen/regionale-settings.md` |
| Trope-Analyse | `research/wissen/trope-analyse.md` |
| KDP Listing-Methodik | `research/wissen/kdp-listing-methodik.md` |

---

## Qualitätsregeln (gelten immer)

- **Subtilität:** Zeigen, nicht erklären. Keine Erzählerkommentare die Gefühle benennen.
- **Figurenstimmen:** Jede Figur spricht anders. Stimme aus Figurenprofil lesen.
- **Anti-Patterns:** Kein Mary Sue, kein MPDG, kein Insta-Love, kein Bella-Swan-Labeling.
- **Prosa-Stil:** Fließtext wie ein Roman. Kein Stakkato. Variation im Satzbau.
- **Steamy-Szenen:** Emotional verankert, mindestens 2 Kapitel Tension-Aufbau vorher.
- Vollständige Regeln stehen in `lina-voss/PRODUCTION.md` (Sektion Qualitätsregeln).

---

## Session-Prinzip

Produktion wird über **mehrere Sessions** verteilt — nie alles auf einmal.
Am Ende jeder Session: Status speichern + Memory aktualisieren.
Am Anfang jeder neuen Session: Status lesen + nahtlos weitermachen.
Details: `lina-voss/PRODUCTION.md` (Sektion Session-Aufteilung).
