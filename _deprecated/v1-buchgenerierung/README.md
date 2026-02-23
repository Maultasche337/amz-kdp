# 📚 Novel Agent — Automatisierte Nischen-Roman-Produktion

## Was dieses System macht
Aus einem kurzen Briefing (5 Minuten ausfüllen) produziert dieser Agent vollautomatisch:
- Nischenanalyse & Keyword-Strategie
- Story-Ending
- Charakterprofile
- 20-Kapitel-Struktur (Save the Cat)
- Vollständiges Manuskript (~60.000 Wörter)
- Lektoratsbericht
- Amazon KDP Listing (SEO-optimiert)
- 3 Buchcover-Prompts für Imagen 3

---

## Schnellstart

### 1. Briefing ausfüllen
```bash
cp templates/briefing.template.json mein_buch.json
# Öffne mein_buch.json in VS Code und fülle es aus
```

### 2. Agent starten (Claude Code CLI)
```bash
cd novel-agent
claude "Starte Roman-Produktion. Lese CLAUDE.md und dann briefing.json: mein_buch.json"
```

### 3. Warte auf den ersten Pause-Punkt
Der Agent stoppt nach der Kapitelstruktur und zeigt dir den Plan.
Bestätige mit "ja" und er schreibt alle Kapitel automatisch.

### 4. Output abholen
Alle Dateien liegen in: `output/[deine_book_id]/`

---

## Briefing-Felder erklärt

| Feld | Beispiel | Pflicht |
|------|---------|---------|
| book_id | "buch_001" | ✅ |
| author_pen_name | "Lisa Berger" | ✅ |
| genre | "Romance" | ✅ |
| subgenre_mood | "Cozy" / "Dark" / "Steamy" | ✅ |
| tropes | ["Age Gap", "Enemies to Lovers"] | ✅ |
| setting.type | "Small Town" / "Mafia" / "Fantasy" | ✅ |
| protagonist.age_range | "48-55" | ✅ |
| protagonist.special_characteristics | ["Neurodivergent (ADHS)"] | optional |
| target_length_chapters | 20 | ✅ |
| additional_notes | Zielgruppe, Ton, Besonderes | optional |

---

## Token-Management
- Freier Claude-Plan: ~2 Bücher/Woche
- Claude Pro (~20$/Monat): ~1-2 Bücher/Tag
- Der Agent informiert dich wenn das Token-Limit näher kommt und speichert automatisch

---

## Nach der Produktion
1. `05_manuscript.md` → Kindle Create (kostenlos, Amazon)
2. `08_cover_prompts.md` → Imagen 3 in Gemini Pro (kostenloser 30-Tage-Trial)
3. `07_kdp_listing.md` → Direkt in KDP einfügen
4. Upload auf kdp.amazon.com

---

## Dateienübersicht
```
novel-agent/
├── CLAUDE.md              ← Orchestrator (Haupt-Agent)
├── README.md              ← Diese Datei
├── templates/
│   └── briefing.template.json
├── skills/
│   ├── 01_niche_analysis.md
│   ├── 02_ending.md
│   ├── 03_characters.md
│   ├── 04_outline.md
│   ├── 05_chapters.md
│   ├── 06_editing.md
│   ├── 07_listing.md
│   └── 08_cover.md
└── output/
    └── [book_id]/
        ├── 00_status.md
        ├── 01_niche_analysis.md
        ├── 02_ending.md
        ├── 03_characters.md
        ├── 04_outline.md
        ├── 05_manuscript.md
        ├── 06_editing_report.md
        ├── 07_kdp_listing.md
        ├── 08_cover_prompts.md
        └── FINAL_SUMMARY.md
```
