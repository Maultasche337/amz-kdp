---
name: novel-producer
description: Produziert vollautomatisch einen deutschsprachigen Nischen-Roman für Amazon KDP. Wird ausgelöst wenn der User schreibt "Neues Buch:" gefolgt von einem Briefing, oder "Roman starten", oder ähnliche Formulierungen. Führt alle Schritte automatisch durch: Nischenanalyse, Ending, Charaktere, Kapitelstruktur, alle Kapitel schreiben, Lektorat, KDP Listing, Cover-Prompts.
metadata: { "openclaw": { "requires": { "env": ["ANTHROPIC_API_KEY"], "bins": ["node"] } } }
---

# Novel Producer — Automatische Romanproduktion

## Wann dieser Skill aktiv wird
- User schreibt "Neues Buch:" gefolgt von Angaben
- User schreibt "Roman starten", "Buch schreiben", "Produziere einen Roman"
- User nennt Genre + Zielgruppe + Tropes in einer Nachricht

## Briefing parsen

Wenn der User eine Kurznachricht schickt (z.B. "Neues Buch: Cozy Romance, Age Gap, Protagonistin 50+, Kleines Dorf"), extrahiere daraus:
- genre (Standard: "Romance")
- subgenre_mood (Standard: "Cozy")
- tropes (als Array)
- setting (aus Kontext erschließen)
- protagonist.age_range
- protagonist.special_characteristics (falls erwähnt)
- target_length_chapters (Standard: 20)
- author_pen_name (frag nach falls nicht angegeben, oder erfinde einen deutschen Namen)
- book_id (generiere automatisch: buch_YYYYMMDD_001)

Fehlende Pflichtfelder beim User erfragen, aber maximal 2 Rückfragen — dann sinnvolle Defaults setzen.

## Arbeitsverzeichnis

Alle Dateien kommen in: `~/openclaw-novels/[book_id]/`

Erstelle diesen Ordner zu Beginn.

## Workflow — führe alle Schritte automatisch aus

### Schritt 1: Status-Datei anlegen
Erstelle `00_status.md` mit allen geplanten Schritten. Melde dem User via Discord:
> "📚 Starte Produktion von **[Buchtitel-Idee]** | book_id: [book_id]"

### Schritt 2: Nischenanalyse
Analysiere die Nischenkombination aus dem Briefing:
- Bewerte Nachfrage vs. Wettbewerb (1-10) im deutschsprachigen Amazon-Markt
- Identifiziere die 3 stärksten Verkaufsargumente
- Generiere 20 deutsche Amazon-Keywords
- Empfehle Haupttitel + Untertitel (SEO-optimiert)
- Vergleiche mit englischem Markt: Welche Lücken bestehen auf Deutsch?

Speichere als `01_niche_analysis.md`. Melde: "✅ Nischenanalyse fertig"

### Schritt 3: Story-Ending
- Erstelle 10 mögliche Endings (je 3-5 Sätze)
- Wähle selbst das stärkste aus und begründe kurz warum
- Arbeite es vollständig aus (500-800 Wörter) mit thematischen Notizen
- Notiere welche Story-Threads aufgebaut werden müssen

Speichere als `02_ending.md`. Melde: "✅ Ending fertig"

### Schritt 4: Charakterprofile
Erstelle für jede Figur (Protagonistin, Liebesinteresse, 3-4 Nebenfiguren):
- Name, Alter, Rolle
- Äußeres Erscheinungsbild (detailliert)
- Persönlichkeit (3-5 Kernzüge)
- Innere Wunde / Glaubenssatz
- Entwicklungsbogen
- Besondere Eigenheiten
- Dialogstimme

WICHTIG: Protagonistin mit den Eigenschaften aus dem Briefing authentisch und positiv darstellen — kein Makel, eine Stärke.

Speichere als `03_characters.md`. Melde: "✅ Charaktere fertig"

### Schritt 5: Save-the-Cat Kapitelstruktur
Erstelle eine vollständige 15-Beat Save-the-Cat Storyline für [target_length_chapters] Kapitel.

Für jedes Kapitel:
- Nummer und Titel
- STC-Beat (falls zutreffend)
- POV, Setting, Stimmung
- Hauptkonflikt + emotionaler Kern
- Wichtige Szenen (2-4 Punkte)
- Cliffhanger/Überleitung
- Ziel-Wortanzahl: 2.500-3.500 Wörter

Speichere als `04_outline.md`.

Melde dem User via Discord:
> "⏸️ **Kapitelstruktur fertig** — [N] Kapitel geplant.
> Kurze Zusammenfassung: [2-3 Sätze zur Story]
> Soll ich mit dem Schreiben beginnen? (ja / änderungen: [was soll anders sein])"

WARTE auf Antwort des Users.

### Schritt 6: Kapitel schreiben (nach Bestätigung)
Schreibe alle Kapitel nacheinander. Für jedes Kapitel:

**Schreib-Prompt:**
- Länge: 2.500-3.500 Wörter
- Sprache: Fließendes, warmes Deutsch — kein Übersetzer-Stil
- Show don't tell
- Dialoganteil ca. 40%
- Enge dritte Person (konsistent durchhalten)
- Ton: [subgenre_mood aus Briefing]
- Kontinuität: Nutze die letzten 500 Wörter des bisherigen Manuskripts als Anker

Nach jedem Kapitel:
- An `05_manuscript.md` anhängen
- Status-Datei updaten
- Kurzes Discord-Update: "✍️ Kapitel [N]/[total] fertig"

Token-Management:
- Falls Kontext-Limit erreicht wird: Speichere sofort, informiere User, fahre im nächsten Message fort
- Übergebe beim Neustart immer die letzten 1.000 Wörter des Manuskripts + alle Referenzdokumente

### Schritt 7: Lektorat
Prüfe das fertige Manuskript auf:
- Kontinuitätsfehler (mit Kapitelangabe)
- Charakterinkonsistenzen
- Plotlöcher
- Sprachprobleme (Wiederholungen, Passiv-Überladung, Übersetzer-Anmutung)
- Stärken

Erstelle priorisierte To-Do-Liste.

Speichere als `06_editing_report.md`.

Melde: "⏸️ **Lektorat fertig** — [X] kritische Fehler, [Y] Empfehlungen.
Soll ich kritische Fehler automatisch korrigieren? (ja / nein / liste zeigen)"

WARTE auf Antwort.

### Schritt 8: KDP Listing
Erstelle vollständiges SEO-optimiertes Amazon KDP Listing:
- Haupttitel (max. 60 Zeichen)
- Untertitel (max. 200 Zeichen)
- Buchbeschreibung (150-400 Wörter, Struktur: Hook → Protagonistin → Liebesinteresse → Stakes → CTA → Keywords)
- 7 Backend-Keywords (je max. 50 Zeichen)
- 2 empfohlene Amazon-Kategorien
- A+ Content Idee

Speichere als `07_kdp_listing.md`. Melde: "✅ KDP Listing fertig"

### Schritt 9: Cover-Prompts
Erstelle 3 Imagen-3-Prompts für Buchcover-Varianten:
1. Klassisches Romance-Cover (Figuren)
2. Setting-fokussiert (Atmosphäre)
3. Symbolisch/minimalistisch

Jeder Prompt: ca. 150 Wörter Englisch, inkl. "book cover, vertical format, 1600x2560px, professional publishing quality, women's fiction 40+"

WICHTIG: Keine Teenager-Ästhetik. Protagonistin ist 40+.

Speichere als `08_cover_prompts.md`.

Melde: "✅ Cover-Prompts fertig — nutze den novel-cover Skill um das Cover automatisch zu generieren: 'Cover generieren für [book_id]'"

### Schritt 10: Abschluss

Erstelle `FINAL_SUMMARY.md` mit:
- Buchdetails + Marktchancen-Score
- Dateienübersicht
- Nächste Schritte: Cover generieren → Kindle Create → KDP Upload

Melde via Discord:
> "🎉 **Buch fertig: [Titel]**
> 📁 Dateien: ~/openclaw-novels/[book_id]/
> 📊 Marktchancen-Score: [X]/10
> 🎨 Cover: 'Cover generieren für [book_id]'
> 📝 KDP Listing: fertig in 07_kdp_listing.md"
