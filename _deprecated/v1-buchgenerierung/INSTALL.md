# OpenClaw Novel Skills — Installationsanleitung

## Schritt 1: Skills kopieren

Kopiere alle 3 Skill-Ordner in dein OpenClaw Skills-Verzeichnis:

```bash
# Globale Skills (für alle Agenten verfügbar)
cp -r novel-producer ~/.openclaw/skills/
cp -r novel-cover ~/.openclaw/skills/
cp -r novel-briefing ~/.openclaw/skills/

# ODER: Nur für deinen Discord-Agenten
cp -r novel-producer ~/.openclaw/workspace-[dein-agent]/skills/
cp -r novel-cover ~/.openclaw/workspace-[dein-agent]/skills/
cp -r novel-briefing ~/.openclaw/workspace-[dein-agent]/skills/
```

## Schritt 2: Replicate API Key holen (für Cover)

1. Account erstellen: https://replicate.com
2. API Token kopieren unter: https://replicate.com/account/api-tokens
3. In OpenClaw-Umgebung setzen:

```bash
# In ~/.openclaw/openclaw.json hinzufügen:
{
  "skills": {
    "entries": {
      "novel-cover": {
        "enabled": true,
        "env": {
          "REPLICATE_API_TOKEN": "r8_dein_token_hier"
        }
      }
    }
  }
}
```

## Schritt 3: Ausgabe-Ordner erstellen

```bash
mkdir -p ~/openclaw-novels
```

## Schritt 4: OpenClaw Gateway neu starten

```bash
openclaw gateway restart
```

## Schritt 5: Skills prüfen

```bash
openclaw skills list
# novel-producer, novel-cover, novel-briefing sollten als "ready" erscheinen
```

---

## So benutzt du das System

### Buch starten (Variante A — Kurz):
Discord-Nachricht an deinen Bot:
```
Neues Buch: Cozy Romance, Age Gap, Protagonistin 52 mit ADHS, Kleines Dorf in Bayern, Enemies to Lovers
```

### Buch starten (Variante B — Interaktiv):
```
Neues Buch
```
→ Bot führt dich durch das Briefing

### Cover generieren (nachdem Buch fertig):
```
Cover generieren für buch_20260219_001
```

---

## Kosten-Übersicht

| Was | Kosten |
|-----|--------|
| Roman schreiben (Claude API) | ~$0.50-2.00 pro Buch |
| 3 Cover-Varianten (Replicate) | ~$0.12 |
| Gesamt pro Buch | ~$0.62-2.12 |
| Bei 2 Büchern/Woche | ~$5-17/Monat |

Zum Vergleich: Ein Buch verkauft sich für ~$3.36 Gewinn. **Break-even nach 1 Verkauf.**
