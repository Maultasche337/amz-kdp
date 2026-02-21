---
name: novel-bonus-scene
description: Generiert eine exklusive Bonus-Szene pro Buch für die Autorinnen-Website — entweder eine "gelöschte Szene" oder eine bekannte Szene aus einem anderen POV. Wird automatisch nach jedem fertiggestellten Roman aufgerufen, oder manuell mit "Bonus-Szene für [Buch]".
metadata: { "openclaw": { "requires": { "env": ["ANTHROPIC_API_KEY"], "bins": ["node"] } } }
---

# Novel Bonus Scene — Exklusiver Website-Content

## Wann dieser Skill aktiv wird
- Automatisch: Am Ende jedes `novel-producer` Durchlaufs (nach Lektorat, vor KDP Listing)
- Manuell: "Bonus-Szene für [Buch/book_id]"
- Manuell: "Gelöschte Szene schreiben", "Alternativer POV für Buch 1"

## Was eine gute Bonus-Szene ausmacht

Die Szene muss einen echten Mehrwert bieten — Leserinnen die das Buch bereits kennen sollen etwas Neues erleben. Optionen:

### Option A: Alternativer POV (empfohlen)
Eine Schlüsselszene aus dem Buch aus der Perspektive einer anderen Figur.
- Perfekt: Die erste Begegnung der beiden Hauptfiguren, aber aus der Perspektive des Liebesinteresses
- Perfekt: Eine emotionale Wendung aus der Perspektive der besten Freundin
- Zeigt innere Gedanken die im Buch nicht sichtbar waren

### Option B: Gelöschte Szene
Eine Szene die logisch ins Buch gepasst hätte, aber aus Erzähltempo-Gründen nicht drin war.
- Perfekt: Ein Gespräch zwischen Nebenfiguren über die Hauptfigur
- Perfekt: Ein "Davor" (was passierte direkt bevor Kapitel 1 beginnt)
- Perfekt: Ein "Danach" (wie geht es den Figuren nach dem Ende weiter)

### Option C: Aus der Vergangenheit
Eine Szene die vor der Haupthandlung spielt und Kontext gibt.
- Perfekt: Der Moment als eine Figur ihre wichtigste Entscheidung traf
- Perfekt: Wie zwei Figuren sich vor langer Zeit zum ersten Mal begegnet sind

## Pseudonym-Anpassungen

### Maja Sternberg
- Szene in derselben präzisen, lakonisch-warmen Stimme
- Bevorzuge alternativen POV (Markus' Gedanken sind Gold für Leserinnen)
- Länge: 1.000-1.500 Wörter
- Endet emotional warm, nicht mit Cliffhanger (Leserinnen sollen sich wohlfühlen)
- Tiroler Details wie im Hauptbuch (Lärchen, Almbetrieb, Rosinas Stübl)

### Monika Huber  
- Behalte den Humor — gelöschte Szenen dürfen noch komischer sein als das Buch
- Bevorzuge Hanni-POV wenn Hauptbuch aus Beates Sicht war, und umgekehrt
- Länge: 800-1.200 Wörter
- Darf mit einem kleinen Witz enden
- Darf Anspielungen auf den Cold Case enthalten die im Buch noch nicht auftauchen

## Output-Format

```
---
PSEUDONYM: [Name]
BUCH: [Titel + Band-Nummer]
BOOK_ID: [book_id]
TYP: [Alternativer POV / Gelöschte Szene / Aus der Vergangenheit]
FIGUR-POV: [Wessen Perspektive]
ORIGINALSZENE: [Auf welche Buchszene bezieht sie sich]
---

# [Titel der Bonus-Szene]
*[Kurze Einleitung: "Diese Szene wurde aus [Buch] herausgeschnitten..." oder "Wir wollten immer wissen was [Figur] in diesem Moment dachte..."]*

[Szenentext — 800-1.500 Wörter]

---
*Danke dass ihr Teil der [Bergwald-Familie / des Ermittlerinnen-Clubs] seid. ❤️*
*[Optional: Hinweis auf Band 2 oder Newsletter]*
```

## Workflow

1. Lies `~/openclaw-novels/[book_id]/05_charaktere.md` und `06_kapitelstruktur.md` um Figuren und Schlüsselszenen zu kennen
2. Entscheide welche Szene sich am besten für Bonus-Content eignet (emotionalster Moment / meiste Neugier)
3. Wähle Typ (A/B/C) basierend auf Pseudonym-Empfehlung
4. Schreibe die Szene vollständig in der Pseudonym-Stimme
5. Speichere unter `~/openclaw-novels/[book_id]/bonus_scene.md`
6. Speichere zusätzlich als Website-Datei: `~/openclaw-websites/[pseudonym]/src/pages/bonus/[book_slug].astro` (Inhalt als Markdown-Block, fertig für Astro)
7. Melde via Discord: "✨ Bonus-Szene fertig: *[Titel der Szene]* ([POV-Figur]-Perspektive) — bereit für Website"
