---
name: novel-briefing
description: Hilfsskill der den User durch ein interaktives Briefing führt und am Ende automatisch den novel-producer Skill startet. Wird ausgelöst wenn User "Neues Buch" ohne weitere Details schreibt, oder "Hilf mir ein Buch zu planen".
metadata: { "openclaw": { "requires": {} } }
---

# Novel Briefing — Interaktiver Buchplaner

## Wann dieser Skill aktiv wird
- "Neues Buch" (ohne weitere Details)
- "Ich will ein Buch schreiben"
- "Hilf mir ein Buch planen"

## Zweck
Führt den User in maximal 3 Nachrichten durch das Briefing, dann übergibt es an novel-producer.

## Ablauf

### Nachricht 1: Kernfragen

Stelle diese Fragen in einer einzigen Discord-Nachricht:

> "📚 **Neues Buch — Schnell-Briefing**
>
> Beantworte kurz (alles in einer Nachricht reicht):
>
> **1. Genre & Stimmung** — z.B. "Cozy Romance", "Dark Romance", "Fantasy Romance", "Krimi"
> **2. Tropes** — z.B. "Age Gap, Enemies to Lovers, Second Chance" (2-4 Tropes)
> **3. Protagonistin** — Alter? Besonderheiten? (z.B. "55, ADHS, Wiedereinsteigerin")
> **4. Setting** — z.B. "Kleines Dorf Bayern", "Wien Innenstadt", "Fantasiewelt mit Magie"
> **5. Autorenname** — Pseudonym für Amazon (oder ich erfinde einen)"

### Nachricht 2: Bestätigung + Start

Wenn der User geantwortet hat, fasse das Briefing zusammen:

> "✅ **Briefing verstanden:**
> 📖 Genre: [X]
> 🎭 Tropes: [X, X, X]
> 👩 Protagonistin: [X]
> 🏘️ Setting: [X]
> ✍️ Autorenname: [X]
> 📄 20 Kapitel (ca. 60.000 Wörter)
>
> Starte ich jetzt die Produktion? (ja / änderungen: [was])"

### Nachricht 3: Übergabe

Bei "ja" — übergib alle Daten an den **novel-producer** Skill und starte die Produktion.

## Defaults (falls User wenig angibt)
- Kapitelanzahl: 20
- Sprache: Deutsch
- Explizitheit: Keine (Clean Romance / Fade to Black)
- Zielgruppe: Frauen 40+
- Amazon-Markt: amazon.de
