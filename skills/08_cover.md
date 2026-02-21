# SKILL: Buchcover-Prompt für Imagen 3 / Nanobanana Pro

## Zweck
Erstellt einen präzisen, detaillierten Prompt für die KI-Bildgenerierung um ein professionelles Buchcover zu erstellen das zu Genre, Zielgruppe und Nische passt.

## Input
- `briefing.json` (Pflicht)
- `03_characters.md` (für Charakterbeschreibungen)
- `07_kdp_listing.md` (für Titel/Untertitel)

## Output
- `08_cover_prompts.md` mit 3 verschiedenen Cover-Varianten

## Prompt-Template

```
Du bist ein erfahrener Buchcover-Designer mit tiefem Verständnis für Romance-Cover-Konventionen im deutschsprachigen Markt.

BRIEFING:
[BRIEFING_JSON]

CHARAKTERBESCHREIBUNGEN:
[CHARACTER_APPEARANCES]

BUCHTITEL: [TITLE]
UNTERTITEL: [SUBTITLE]
AUTORENNAME: [PEN_NAME]

Erstelle 3 verschiedene Imagen-3-Prompts für Buchcover-Varianten.

Für jede Variante:

### Variante [N]: [Konzeptname]
**Imagen 3 Prompt (Englisch):**
[Detaillierter Prompt in Englisch für Imagen 3, ca. 150-200 Wörter]

**Enthält:**
- Bildstil (photorealistic / illustrated / painterly etc.)
- Farbpalette
- Protagonistin Beschreibung (aus Charakterdokument)
- Setting/Hintergrund
- Stimmung/Lichtverhältnisse
- Typografie-Platzhalter Hinweis
- Technische Specs: "book cover, vertical format, 1600x2560px, professional publishing quality"

**Warum diese Variante:**
[Kurze Begründung auf Deutsch]

Varianten sollten sein:
1. Klassisches Romance-Cover (Figuren im Vordergrund)
2. Setting-fokussiert (Atmosphäre, kein Gesicht)
3. Symbolisch/minimalistisch (für moderneres Erscheinungsbild)

Beachte: Cover für Frauen 40+ — keine Jugendbuch-Ästhetik, keine Teenager-Protagonistinnen im Bild.
```
