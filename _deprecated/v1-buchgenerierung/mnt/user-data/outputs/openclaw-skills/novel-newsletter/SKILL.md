---
name: novel-newsletter
description: Generiert Newsletter-Inhalte für Brevo — Willkommenssequenzen, Bonus-Szenen, Zwischen-Band-E-Mails und Launch-Ankündigungen. Wird ausgelöst wenn User schreibt "Newsletter", "Brevo", "E-Mail für Leserinnen", "Willkommensmail", "Bonus-Szene", "Newsletter Hanni", "Newsletter Maja" oder ähnliches.
metadata: { "openclaw": { "requires": { "env": ["ANTHROPIC_API_KEY"], "bins": ["node"] } } }
---

# Novel Newsletter — Brevo-Content-Generator

## Wann dieser Skill aktiv wird
- "Newsletter schreiben / erstellen"
- "Willkommenssequenz für [Pseudonym]"
- "Bonus-Szene für Abonnentinnen"
- "E-Mail zwischen Band 1 und 2"
- "Launch-Ankündigung"
- "Brevo E-Mail"

## Pseudonym-Profile

### Maja Sternberg (Zillertal-Herzen)
- Ton: Warm, präzise, ein bisschen wie eine Freundin die vom Land schreibt
- Stimme: Maja schreibt als wäre sie selbst in Untergamping, nah an den Figuren
- Leserinnen: Frauen 40-60, wollen Geborgenheit, Romantik, Tiroler Naturnähe
- Brevo-Listenname: Zillertal-Familie

### Monika Huber (Hanni & Beate ermitteln)
- Ton: Humorvoll, locker, als würde man mit einer alten Bekannten schreiben
- Stimme: Monika gibt den Leserinnen das Gefühl "dazuzugehören"
- Leserinnen: Frauen 35-65, lieben Humor, Bayern, weibliche Solidarity
- Brevo-Listenname: Ermittlerinnen-Club

## E-Mail-Typen die du generieren kannst

### Typ A: Willkommenssequenz (3 E-Mails)

**Mail 1 — Sofort nach Anmeldung:**
- Betreff: emotional und persönlich, kein Clickbait
- Inhalt: Wer bin ich (Pseudonym-Story), was erwartet sie hier, SOFORT den versprochenen Bonus (Link zur Bonus-Szene / PDF)
- Länge: kurz, 150-200 Wörter
- CTA: "Genießt die Bonus-Szene ☕"

**Mail 2 — Tag 3:**
- Betreff: Neugier wecken auf Seriengeschichte
- Inhalt: Kleine Geschichte hinter Band 1, warum diese Figuren entstanden, eine persönliche Anekdote (fiktiv aber glaubwürdig für das Pseudonym)
- Länge: 200-250 Wörter
- CTA: Einladung zur Rezension auf Amazon + Link

**Mail 3 — Tag 7:**
- Betreff: Vorfreude auf Band 2 wecken
- Inhalt: Kleine Andeutung was als nächstes kommt, Frage an die Leserinnen (welche Nebenfigur soll eine eigene Geschichte bekommen?), Community-Gefühl aufbauen
- Länge: 200 Wörter
- CTA: "Antwortet einfach auf diese Mail" (fördert Engagement, verbessert Brevo-Deliverability)

### Typ B: Zwischen-Band-Update (1 E-Mail)

Zeitpunkt: 4-6 Wochen nach Band 1 Launch, 2-3 Wochen vor Band 2 Launch

Inhalt:
- Kurzes Update wie Band 1 läuft (ohne genaue Zahlen, aber mit Wärme: "ihr habt mich überwältigt")
- Exklusiver Einblick in Band 2 (erster Satz, oder Name des neuen Liebesinteresses, oder eine Szene)
- Countdown oder Vorschau-Cover
- Länge: 250-300 Wörter

### Typ C: Launch-Ankündigung (1 E-Mail)

Zeitpunkt: Am Launch-Tag oder einen Tag vorher

Inhalt:
- Betreff: "Es ist da!" + Buchtitel
- Emotional, kurz, direkt
- Cover einbinden (Brevo-Bild)
- Klappentext (gekürzt auf 3-4 Sätze)
- Klarer Button: "Jetzt lesen" → Amazon-Link
- Für KU-Abonnentinnen extra erwähnen: "In Kindle Unlimited kostenlos enthalten"
- PS: Bitte um ehrliche Rezension nach dem Lesen
- Länge: 200 Wörter + Button

### Typ D: Bonus-Szene (eigenständiger Content)

Das ist der Hauptanreiz zum Newsletter-Beitritt.

Anforderung:
- Szene die im Buch nicht vorkommt aber im gleichen Universum spielt
- Für Lena: z.B. "Was Thomas wirklich dachte als Maria zum ersten Mal in die Apotheke kam" (Perspektivwechsel)
- Für Hanni & Beate: z.B. "Die Szene die wir aus Kapitel 3 herausgeschnitten haben — Beates erster Tag im Dorf, unzensiert"
- Länge: 800-1.200 Wörter
- Ton: exakt im Stil des jeweiligen Pseudonyms
- Am Ende: "Danke dass ihr Teil der [Bergwald-Familie / des Ermittlerinnen-Clubs] seid ❤️"

### Typ E: Leserinnen-Umfrage (1 E-Mail)

Zeitpunkt: Nach Band 2, vor Band 3

Inhalt:
- Kurze, freundliche Frage: welche 2-3 Dinge haben euch an der Serie am meisten gefallen?
- KEINE langen Formulare — einfach "antwortet auf diese Mail mit eurer Lieblingsszene"
- Zeigt Leserinnen dass ihre Meinung zählt
- Ergebnisse in Band 3 einarbeiten (erwähnen in nächster Mail)

## Brevo-Technische Hinweise (immer erwähnen wenn relevant)

- Alle E-Mails als Plain-Text ODER einfaches Template (kein Design-Overkill bei Autoren-Newslettern)
- Abmeldelink: Brevo fügt diesen automatisch ein — kein manuelles Hinzufügen nötig
- Absender-Name: "Maja Sternberg" oder "Monika Huber" — NICHT "Kursifant" oder echter Name
- Sendezeit: Dienstag oder Donnerstag, 10:00-11:00 Uhr (beste Öffnungsraten laut Brevo-Daten)
- Betreffzeile: unter 50 Zeichen für mobile Darstellung

## Workflow

1. Frage welches Pseudonym (Lena / Monika)
2. Frage welcher E-Mail-Typ (A/B/C/D/E) — oder erkenne es aus dem Kontext
3. Frage nach spezifischen Details falls nötig (z.B. für Launch-Mail: Amazon-Link, Erscheinungsdatum)
4. Generiere alle E-Mails des gewünschten Typs vollständig
5. Speichere unter `~/openclaw-novels/newsletter/[pseudonym]/[typ]_[datum].md`
6. Melde via Discord: "✉️ [Anzahl] E-Mails für [Pseudonym] fertig — bereit für Brevo-Upload"

## Output-Format pro E-Mail

```
---
PSEUDONYM: [Name]
TYP: [A/B/C/D/E]
NUMMER: [1/2/3 falls Sequenz]
SENDEZEIT: [Empfehlung]
---

BETREFF: [Betreffzeile]

VORSCHAUTEXT: [50-90 Zeichen — erscheint in Inbox-Vorschau]

---

[E-Mail-Text]

---

BREVO-HINWEISE:
- [Technische Empfehlungen für diesen spezifischen Send]
```
