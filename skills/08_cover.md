# SKILL: Buchcover generieren (automatisch via API)

## Zweck
Generiert automatisch ein professionelles Buchcover via Bildgenerations-API (Imagen 3 / DALL-E / etc.) das zu Genre, Zielgruppe und Nische passt.

## Input
- `briefing.json` (Pflicht)
- `03_characters.md` (für Charakterbeschreibungen)
- `07_kdp_listing.md` (für Titel/Untertitel)

## Output
- `08_cover_prompts.md` mit 3 Cover-Varianten (Prompts + generierte Bilder)
- Generierte Cover-Bilder im Output-Ordner

## Workflow

### Schritt 1: Prompts erstellen
Erstelle 3 verschiedene Cover-Konzepte:
1. Klassisches Romance-Cover (Figuren im Vordergrund)
2. Setting-fokussiert (Atmosphäre, kein Gesicht)
3. Symbolisch/minimalistisch (für moderneres Erscheinungsbild)

### Schritt 2: Cover generieren (AUTOMATISCH)
**WICHTIG:** API-Key ist konfiguriert — generiere die Cover direkt via API.
- Rufe die Bildgenerations-API auf
- Speichere Bilder als `output/[book_id]/cover_v1.png`, `cover_v2.png`, `cover_v3.png`
- Zeige dem User die generierten Cover

### Schritt 3: User-Auswahl
Frage den User welche Variante bevorzugt wird, oder ob Anpassungen nötig sind.

---

## Prompt-Struktur (für jede Variante)

```
Professional [STYLE] book cover for German romance novel.

[CHARACTER DESCRIPTION from 03_characters.md]
[SETTING DESCRIPTION]
[MOOD & LIGHTING]
[COLOR PALETTE]

Leave space at top for title text.
Book cover, vertical format, 1600x2560px, professional publishing quality.
```

## Cover-Varianten

### Variante 1: Klassisches Romance-Cover
- Figuren im Vordergrund (Protagonist + Love Interest)
- Emotionaler Blickkontakt oder Nähe
- Setting im Hintergrund (soft focus)

### Variante 2: Setting-fokussiert
- Landschaft/Atmosphäre im Fokus
- Keine Gesichter (oder nur Silhouetten)
- Suggestive Elemente (zwei Weingläser, Schuhe, etc.)

### Variante 3: Symbolisch/Minimalistisch
- Ein zentrales Symbol (Schlüssel, Blume, Hand, etc.)
- Moderne, cleane Ästhetik
- Starke Farbkontraste

---

## Technische Specs

| Parameter | Wert |
|-----------|------|
| Format | 1600 x 2560 px (Kindle) |
| Aspect Ratio | 1:1.6 |
| Stil | Photorealistic oder Painterly |
| Zielgruppe | Frauen 40+ |

---

## Hinweise für den Orchestrator

- **NICHT** den User bitten, Prompts manuell in externe Tools einzugeben
- **DIREKT** via verfügbare Bildgenerations-Tools generieren
- Nach Generierung: User fragen welche Variante, dann ggf. Typografie-Overlay besprechen
