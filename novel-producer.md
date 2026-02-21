---
name: novel-producer
description: Produziert vollautomatisch einen deutschsprachigen Nischen-Roman für Amazon KDP. Unterstützt Pseudonyme und Serien. Ausgelöst durch "Neues Buch:", "Roman starten", oder "Buch [N] der [Serienname]-Serie schreiben". Führt alle Schritte automatisch durch.
metadata: { "openclaw": { "requires": { "env": ["ANTHROPIC_API_KEY"], "bins": ["node"] } } }
---

# Novel Producer — Automatische Romanproduktion mit Pseudonym & Serien-Support

## Wann dieser Skill aktiv wird
- "Neues Buch: [Details]"
- "Schreib Buch 2 der Bergwald-Serie"
- "Nächstes Hanni & Beate Buch"
- "Roman starten für [Pseudonym]"

---

## Schritt 0: Pseudonym & Serien-Kontext laden

Bevor irgendetwas anderes passiert:

1. Erkenne welches Pseudonym gemeint ist:
   - Erwähnung von "Zillertal", "Maja", "Cozy Romance" → Maja Sternberg
   - Erwähnung von "Hanni", "Beate", "Krimi", "Unterbach" → Monika Huber
   - Unklar → frage einmal kurz nach

2. Lade die entsprechende Pseudonym-Datei:
   - `~/pseudonyme/maja-sternberg/PSEUDONYM.md`
   - `~/pseudonyme/monika-huber/PSEUDONYM.md`

3. Erkenne ob es ein Serien-Folgebuch ist:
   - Prüfe ob bereits Bücher dieser Serie existieren in `~/openclaw-novels/`
   - Falls ja: Lade das letzte Manuskript (nur die letzten 2.000 Wörter für Kontext)
   - Beachte den Cliffhanger aus dem Vorgänger-Buch

4. Setze book_id: `[pseudonym-kürzel]_serie[N]_buch[N]_YYYYMMDD`
   Beispiel: `lb_bergwald_buch2_20260301`

Melde via Discord:
> "📚 **[Pseudonym]: [Serienname] — Buch [N]**
> Lade Kontext... ✅ Pseudonym-Profil geladen | ✅ Vorgänger-Cliffhanger erkannt"

---

## Schritt 1: Briefing vervollständigen

Falls kein vollständiges Briefing: Ergänze fehlende Felder automatisch aus dem Pseudonym-Dokument.

Aus `PSEUDONYM.md` automatisch übernehmen:
- Stimmprofil → wird bei jedem Kapitel als Referenz mitgegeben
- Cover-Ästhetik → geht an novel-cover Skill
- Tonalität, Sprache, Dialekt-Regeln
- Zielgruppe und KDP-Keywords-Basis

Falls Serien-Folgebuch: Übernehme aus dem Serienplan im Pseudonym-Dokument:
- Protagonistin + Liebesinteresse für dieses Buch
- Kerntropes
- Innere Wunden beider Figuren
- Den zu lösenden Cliffhanger aus dem Vorgänger
- Den neuen Cliffhanger für das Folgebuch

---

## Schritt 2: Nischenanalyse (angepasst für Serien)

Bei Buch 1 einer Serie: Vollständige Nischenanalyse wie gehabt.

Bei Folgebüchern (Buch 2, 3): Kürzere Analyse — fokussiert auf:
- Sind neue konkurrierende Titel seit Buch 1 erschienen?
- Welche Keywords aus Buch 1 haben gut funktioniert? (falls bekannt)
- Wie soll das Listing auf die Serie hinweisen?

Speichere als `01_niche_analysis.md`.

---

## Schritt 3: Ending generieren

Nutze den Serienplan aus PSEUDONYM.md als Basis.
Das Ending ist nicht frei erfunden — es muss:
- Den Cliffhanger aus dem Vorgänger auflösen
- HEA für das aktuelle Paar liefern
- Den neuen Cliffhanger für Buch [N+1] einbauen (außer beim letzten Buch der Serie)

Speichere als `02_ending.md`.

---

## Schritt 4: Charakterprofile

Übernimm das Duo / die Hauptfiguren aus PSEUDONYM.md.
Ergänze neue Nebenfiguren die für dieses Buch relevant sind.
Stelle sicher dass bestehende Dorf-Charaktere konsistent sind.

**Besonders für Monika Huber:** Hanni und Beate haben festgelegte Stimmen aus PSEUDONYM.md — halte dich exakt daran. Der Humor entsteht aus dem Kontrast ihrer POVs, nicht aus Situationskomik allein.

**Besonders für Maja Sternberg:** Die Dorf-Charaktere (Rosina, Luise, die Bäckerin) tauchen als Randfiguren auf — konsistent mit vorherigen Büchern halten.

Speichere als `03_characters.md`.

---

## Schritt 5: Kapitelstruktur

Save-the-Cat für [20] Kapitel.

**Für Monika Huber zusätzlich:**
- Abwechselnde POVs: Kapitel 1 (Hanni), Kapitel 2 (Beate), etc.
- Jedes Kapitel endet mit einer kleinen Pointe oder einem Missverständnis
- Der "All is Lost"-Moment ist immer komisch UND emotional gleichzeitig

**Für Maja Sternberg zusätzlich:**
- Slow Burn: Physische Nähe erst ab Kapitel 12+
- Mindestens 3 "Beinahe-Momente" die sich auflösen bevor der echte Moment kommt
- Tiroler Natur-Setting aktiv als Stimmungsträger einsetzen (Lärchen, Jahreszeiten, Almbetrieb)

Zeige fertige Struktur und warte auf Bestätigung.

---

## Schritt 6: Kapitel schreiben

**Basis-Prompt für jedes Kapitel — IMMER diese Elemente mitgeben:**

```
Pseudonym-Stimmprofil:
[STIMMPROFIL aus PSEUDONYM.md]

Charakterreferenz:
[03_characters.md]

Kapitelplan:
[Dieser Kapitel-Eintrag aus 04_outline.md]

Letzter Absatz des vorherigen Kapitels:
[Letzten 300 Wörter aus 05_manuscript.md]

Schreibe jetzt Kapitel [N]: "[Titel]"
- Länge: 2.500-3.500 Wörter
- POV: [Figur]
- Ton: [Pseudonym-spezifisch]
- Halte dich an das Stimmprofil — kein generisches KI-Schreiben
```

**Qualitätsprüfung nach jedem Kapitel (intern):**
- Über 2.000 Wörter? Falls nicht: Regeneriere
- Klingt es nach dem Pseudonym oder generisch? Falls generisch: Regeneriere mit stärkerem Ton-Prompt
- Cliffhanger am Kapitelende vorhanden? Falls nicht: Kurzen Schluss-Absatz hinzufügen

---

## Schritt 7: Lektorat

Zusätzlich zu Standardlektorat prüfe:

**Für Monika Huber:**
- Ist der Ton konsistent zwischen Hanni-Kapiteln (kurz, trocken) und Beate-Kapiteln (lang, verschachtelt)?
- Funktionieren die komödiantischen Missverständnisse?
- Ist der Humor organisch oder aufgesetzt?

**Für Maja Sternberg:**
- Ist der Slow Burn überzeugend oder zu abrupt?
- Sind die Bayern-Elemente authentisch oder klischeehaft?
- Stimmt der emotionale Ton — warm aber nie kitschig?

---

## Schritt 8: KDP Listing

Nutze die Keywords aus PSEUDONYM.md als Basis.

**Serien-Hinweis im Listing einbauen:**
> "Band [N] der [Serienname]-Reihe — auch als Einzelband lesbar"

**Für Folgebücher:** Erwähne kurz was Leserinnen von Buch 1 erwartet (Dorf-Charaktere, Duo etc.) ohne zu spoilern.

---

## Schritt 9: Cover-Prompts

Verwende den Basis-Prompt aus PSEUDONYM.md und passe an:
- Setting dieses Buches
- Jahreszeit (aus der Story)
- Das Erkennungsmerkmal der Serie (Lärchen-Motiv für Maja / bayerisches Detail für Monika)
- Buchtitel und Untertitel

---

## Abschluss-Meldung

> "🎉 **[Pseudonym]: [Titel] — Buch [N]/3 fertig**
> 📁 ~/openclaw-novels/[book_id]/
> 🔗 Nächstes Buch der Serie: '[Cliffhanger-Stichwort]'
> 🎨 Cover: 'Cover generieren für [book_id]'"
