---
name: novel-social
description: Generiert Social-Media-Content für BookTok, Bookstagram und Micro-Influencer-Pitches. Wird ausgelöst wenn User schreibt "BookTok", "Bookstagram", "TikTok", "Reel", "Influencer", "Social Media", "Caption", "Post für", "Micro-Influencer anschreiben" oder ähnliches.
metadata: { "openclaw": { "requires": { "env": ["ANTHROPIC_API_KEY"], "bins": ["node"] } } }
---

# Novel Social — BookTok & Bookstagram Content-Generator

## Wann dieser Skill aktiv wird
- "BookTok Skript für [Buch/Pseudonym]"
- "Bookstagram Caption"
- "Reel-Ideen"
- "Influencer anschreiben"
- "Social Media Post"
- "TikTok Video"
- "Content für diese Woche"

## Pseudonym-Profile

### Maja Sternberg
- Ästhetik: Warm, herbstlich-alpin, Lärchen, Kaffee, Bücher auf Holztisch mit Bergblick
- Hashtag-Kern: #CozyRomance #ZillertaHerzen #Liebesroman #BücherdeTok #MajaSternberg #Frauenroman #TirolRomance
- Zielgruppe Social: Frauen 35-55, BookTok Germany, Buchstagram Deutschland
- Ton: Wie eine Buchempfehlung von einer Freundin

### Monika Huber
- Ästhetik: Bayerisch, blau-weiß, Humor, Comic-nah, etwas chaotisch-liebenswürdig
- Hashtag-Kern: #CozyCrime #Kuschelkrimi #Bayernkrimi #HumorKrimi #HanniUndBeate #MonikaHuber #Regionalkrimi
- Zielgruppe Social: Frauen 35-65, Krimi-TikTok, Bayern-affine Community
- Ton: Locker, witzig, als würde Monika selbst posten

## Content-Typen

### Typ 1: BookTok / TikTok Skript

Format: 30-60 Sekunden, Hook in den ersten 3 Sekunden

Struktur:
```
HOOK (0-3 Sek): [Frage oder provokante Aussage — Thumb-Stopper]
SETUP (3-15 Sek): [Kurze Vorstellung der Prämisse]
ESKALATION (15-40 Sek): [Warum ist das besonders / was passiert]
CTA (40-60 Sek): [Klarer Aufruf: "Link in Bio", "Kommentiere X wenn du mehr willst"]
```

Beispiel-Hooks für Lena:
- "Wenn du 44 bist und glaubst die große Liebe ist vorbei — lies das."
- "Sie hat ihren Job gekündigt, ihre Wohnung aufgegeben, und ist in ein Dorf gezogen das sie nicht will. Und dann."
- "Slow Burn bedeutet: 200 Seiten Spannung. Hier ist warum das besser ist als Action."

Beispiel-Hooks für Hanni & Beate:
- "Zwei Frauen 40+ lösen einen Mord. Eine ist Dorfpolizistin. Die andere hat einen Podcast mit 340 Hörern."
- "POV: Du bist neu im Dorf und deine Nachbarin glaubt ernsthaft dass sie besser ermittelt als du."
- "Bayerischer Regionalkrimi aber make it Comedy. Ich erkläre kurz."

Für jedes Skript:
- Spezifisch für das genannte Buch/Kapitel schreiben
- Kein Spoiler der Auflösung
- Neugier als Ende, nicht Antwort
- Emoji-Einsatz sparsam aber passend

### Typ 2: Bookstagram Caption

Drei Längen anbieten:

**Kurz (unter 150 Zeichen):**
Für einfache Buchcover-Posts. Witz oder emotionaler Treffer.

**Mittel (150-300 Zeichen):**
Für Flat-Lay-Fotos. Kurze Beschreibung + Frage an Community.

**Lang (300-500 Zeichen):**
Für Carousel-Posts oder "talking about a book". Kleine Geschichte + warum das Buch + Frage.

Immer enden mit: Frage an die Community (erhöht Kommentare = mehr Reichweite)

Foto-Ideen mitliefern (was soll auf dem Bild zu sehen sein):
- Lena: Tasse Kräutertee + Buch + Herbstblätter / Alpenpanorama-Hintergrund / Apothekenfläschchen als Deko
- Hanni & Beate: Maßkrug als Lesezeichen (Witz) / Polizeiband als Buchdeko / Zwei Kaffeetassen auf einem Holztisch "zwei Ermittlerinnen"

### Typ 3: Content-Kalender (1 Woche)

7 Tage, je 1 Post-Idee:

Format:
```
MO: [Plattform] — [Content-Typ] — [Thema]
DI: [Plattform] — [Content-Typ] — [Thema]
...
```

Typische Wochenstruktur:
- Mo: Bookstagram — Buchcover-Post mit kurzer Caption
- Di: TikTok — 30-Sek BookTok Skript
- Mi: Story/Reel — "hinter den Kulissen" (wie entsteht das Buch)
- Do: Bookstagram — Zitat aus dem Buch
- Fr: TikTok — "Trope erklärt" oder "warum du dieses Genre lieben wirst"
- Sa: Story — Umfrage ("Welche Figur soll als nächste ihre Geschichte kriegen?")
- So: optional — Leserinnen-Shoutout oder Rezensions-Zitat

### Typ 4: Micro-Influencer Pitch-Mail

Zielgruppe: Krimi- oder Buchaccounts 500-10.000 Follower auf Instagram/TikTok

Struktur der Pitch-Mail:
1. Persönliche Eröffnung (zeigen dass du ihren Account kennst — 1 Satz)
2. Kurze Vorstellung Buch + Pseudonym (2-3 Sätze)
3. Konkrete Anfrage (ARC-Exemplar, ehrliche Meinung, kein Posting-Zwang)
4. Was sie bekommen (kostenloses E-Book, namentliche Erwähnung in Danksagung)
5. Klarer nächster Schritt ("Antworte einfach auf diese Mail mit deiner E-Mail-Adresse")

Tonalität: Kollegial, nicht unterwürfig. Wir bieten etwas an, wir betteln nicht.

Länge: max. 150 Wörter — Influencer lesen lange Pitches nicht.

Für Hanni & Beate: Krimi-Accounts + bayerische Lifestyle-Accounts ansprechen
Für Maja Sternberg: Cozy-Romance-Accounts + Frauenroman-Blogs ansprechen

Immer eine Variante auf Deutsch generieren.

### Typ 5: Reels-Konzept (ohne Video)

Da du die Videos nicht selbst dreht, generiere:
- Konzept-Beschreibung (was passiert im Video)
- Text-Overlay Sequenz (was steht auf dem Bildschirm)
- Audio-Empfehlung (welcher Trend-Sound passt, oder Beschreibung des gewünschten Tons)
- Voiceover-Text (falls voiceover statt Sound)

## Workflow

1. Erkenne Pseudonym aus Kontext oder frage einmalig nach
2. Erkenne gewünschten Content-Typ (1-5) oder frage kurz nach
3. Frage nach spezifischem Buch / Band falls relevant
4. Generiere den Content vollständig und sofort
5. Biete am Ende an: "Soll ich dazu noch [anderen Typ] generieren?"

Kein langer Workflow — Social-Media-Content muss schnell kommen.

## Output

Jeder Output wird gespeichert unter:
`~/openclaw-novels/social/[pseudonym]/[typ]_[datum].md`

Format:
```
---
PSEUDONYM: [Name]
PLATTFORM: [TikTok / Instagram / Beide]
TYP: [1-5]
DATUM: [Generiert am]
---

[Content]

---
HASHTAGS:
[Komplette Hashtag-Liste kopierbereit]
```

## Hashtag-Listen (immer anhängen)

**Maja Sternberg Standard:**
#CozyRomance #Liebesroman #Frauenroman #KleinstadtRomance #BücherDeutschland #BücherdeTok #Buchstagram #Leseliebe #SlowBurn #BergwaldApotheke #LenaBergmann #KindleUnlimited #eBook #Selfpublishing #Neuerscheinung

**Monika Huber Standard:**
#CozyCrime #Kuschelkrimi #Bayernkrimi #Humorkrimi #Regionalkrimi #Frauenkrimi #HanniUndBeate #MonikaHuber #BücherDeutschland #KrimiTikTok #BücherdeTok #KindleUnlimited #Ermittlerinnen #BayernKrimi
