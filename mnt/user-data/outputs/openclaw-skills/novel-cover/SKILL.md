---
name: novel-cover
description: Generiert automatisch ein professionelles Buchcover für einen fertigen Roman via Replicate API (FLUX oder Imagen). Wird ausgelöst wenn User schreibt "Cover generieren für [book_id]" oder "Buchcover erstellen". Speichert fertige PNG-Datei direkt im Roman-Ordner.
metadata: { "openclaw": { "requires": { "env": ["REPLICATE_API_TOKEN"], "bins": ["curl", "node"] } } }
---

# Novel Cover — Automatische Buchcover-Generierung

## Wann dieser Skill aktiv wird
- "Cover generieren für [book_id]"
- "Buchcover erstellen"
- "Mach das Cover für [Buchtitel]"

## Voraussetzung
- `REPLICATE_API_TOKEN` muss in der Umgebung gesetzt sein
- Replicate Account: https://replicate.com (kostenlose Credits für neue Accounts)
- Der book_id Ordner mit `08_cover_prompts.md` muss existieren

## API-Kosten
- FLUX 1.1 Pro: ca. $0.04 pro Bild
- 3 Varianten = ca. $0.12 pro Buch

## Workflow

### Schritt 1: Prompts laden
Lese `~/openclaw-novels/[book_id]/08_cover_prompts.md` und extrahiere alle 3 Imagen-3-Prompts.

Melde: "🎨 Generiere 3 Cover-Varianten via Replicate..."

### Schritt 2: Bilder generieren
Für jeden der 3 Prompts, führe folgenden Shell-Befehl aus:

```bash
curl -s -X POST \
  -H "Authorization: Bearer $REPLICATE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "version": "black-forest-labs/flux-1.1-pro",
    "input": {
      "prompt": "[PROMPT_TEXT]",
      "width": 1600,
      "height": 2560,
      "aspect_ratio": "custom",
      "output_format": "png",
      "output_quality": 95,
      "safety_tolerance": 2,
      "prompt_upsampling": true
    }
  }' \
  https://api.replicate.com/v1/predictions
```

Warte auf die Prediction-ID, dann pollen bis Status "succeeded":

```bash
curl -s -H "Authorization: Bearer $REPLICATE_API_TOKEN" \
  https://api.replicate.com/v1/predictions/[PREDICTION_ID]
```

### Schritt 3: Bilder herunterladen
Wenn Status "succeeded", lade die Output-URL herunter:

```bash
curl -L "[OUTPUT_URL]" -o ~/openclaw-novels/[book_id]/cover_variante_[N].png
```

Speichere alle 3 als:
- `cover_variante_1_figuren.png`
- `cover_variante_2_setting.png`
- `cover_variante_3_minimal.png`

### Schritt 4: Titelannotation (optional)
Falls der User Titel auf dem Cover möchte, nutze ImageMagick:

```bash
convert cover_variante_1_figuren.png \
  -gravity North -pointsize 80 -fill white \
  -annotate +0+100 "[BUCHTITEL]" \
  cover_variante_1_mit_titel.png
```

### Schritt 5: Abschluss
Melde via Discord:
> "🖼️ **3 Cover-Varianten fertig!**
> ~/openclaw-novels/[book_id]/
> • cover_variante_1_figuren.png
> • cover_variante_2_setting.png
> • cover_variante_3_minimal.png
>
> Welche gefällt dir? Ich kann Anpassungen machen: Farben, Stil, Text-Position."

## Anpassungen auf Anfrage

Wenn der User eine Variante anpassen möchte:
- "Mach Variante 2 wärmer" → Prompt anpassen, neu generieren
- "Anderer Hintergrund" → Prompt-Abschnitt tauschen, neu generieren
- "Weniger dramatisch" → Ton im Prompt anpassen

Immer nur die gewünschte Variante neu generieren, nicht alle 3.

## Fehlerbehandlung

Falls REPLICATE_API_TOKEN fehlt:
> "⚠️ Kein Replicate API Key gefunden. Bitte setze REPLICATE_API_TOKEN in deiner Umgebung.
> Account erstellen: https://replicate.com
> Dann: export REPLICATE_API_TOKEN=r8_..."

Falls Prediction fehlschlägt:
- Warte 5 Sekunden, versuche es einmal erneut
- Bei erneutem Fehler: Error-Message ausgeben und alternativen Prompt versuchen
