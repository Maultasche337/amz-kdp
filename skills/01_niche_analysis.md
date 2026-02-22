# SKILL: Nischen-Validierung & Marktanalyse

## Zweck
Analysiert das Briefing und bewertet die Marktchancen der gewählten Nischenkombination.
Nutzt die **Perplexity API** für echte, aktuelle Marktdaten von Amazon.de.
Generiert eine datengestützte Nischenstrategie und Keyword-Liste für Amazon KDP.

## Input
- `briefing.json` (Pflicht)
- Perplexity API Key in `.env`

## Output
- `01_niche_analysis.md` im Buchordner

## Ablauf

### Phase 1: Live-Marktrecherche via Perplexity API

Führe 3 Perplexity-Recherchen durch (via `scripts/perplexity_research.sh`):

**Recherche 1 — Wettbewerb:**
```
Welche deutschsprachigen [GENRE] Bücher mit [SETTING]-Setting sind aktuell auf Amazon.de erfolgreich?
Liste konkrete Buchtitel, Autoren, Bewertungen, BSR und Preise.
Fokus auf Kindle/KDP. Nenne auch Serien in dieser Nische.
```

**Recherche 2 — Keywords & Suchverhalten:**
```
Welche Keywords und Suchbegriffe nutzen deutsche Leserinnen auf Amazon.de
wenn sie nach [GENRE] mit [TROPES] und [SETTING]-Setting suchen?
Nenne konkrete Amazon-Suchbegriffe mit geschätztem Suchvolumen.
Welche verwandten Kategorien/Subgenres sind relevant?
```

**Recherche 3 — Marktlücken & Trends:**
```
Welche Trends gibt es 2025/2026 im deutschsprachigen [GENRE]-Markt auf Amazon KDP?
Welche Nischen-Kombinationen ([TROPES] + [SETTING]) sind unterversorgt?
Wo gibt es Nachfrage aber wenig Angebot?
```

Ersetze die Platzhalter durch Werte aus dem Briefing:
- `[GENRE]` = `market.genre` + `market.subgenre_mood`
- `[SETTING]` = `setting.type` + `setting.description`
- `[TROPES]` = `tropes[]`

Speichere die Rohdaten als `output/[book_id]/01a_research_raw.md`.

### Phase 2: Analyse & Bewertung

Analysiere die Recherche-Ergebnisse zusammen mit dem Briefing:

```
Du bist ein erfahrener Self-Publishing-Stratege, spezialisiert auf den deutschsprachigen Amazon KDP Markt.

Hier ist das Buchbriefing:
[BRIEFING_JSON]

Hier sind aktuelle Marktdaten aus Live-Recherche:
[PERPLEXITY_RESULTS]

Deine Aufgabe — stütze dich auf die echten Marktdaten:
1. Bewerte die Nischenkombination auf einer Skala von 1-10 (Nachfrage vs. Wettbewerb). Begründe mit konkreten Daten.
2. Identifiziere die 3 stärksten Verkaufsargumente — was unterscheidet dieses Buch von der existierenden Konkurrenz?
3. Schlage 2-3 Variationen der Nischenkombination vor, die laut Recherche unterversorgter sind
4. Erstelle eine Liste von 20 deutschen Amazon-Keywords (basierend auf den recherchierten Suchbegriffen)
5. Wettbewerbsanalyse: Nenne konkrete Konkurrenz-Titel, deren Stärken/Schwächen, und wo unser Buch besser sein kann
6. Empfehle einen Buchtitel (Haupttitel + Untertitel) der SEO-optimiert ist und sich von der Konkurrenz abhebt
7. Preisempfehlung basierend auf dem Markt

Antworte auf Deutsch. Formatiere als strukturiertes Markdown-Dokument.
Kennzeichne klar, welche Aussagen auf Recherche-Daten basieren und welche auf Einschätzung.
```

## Hinweise
- Denkmodus aktivieren für beste Ergebnisse
- Falls der Score unter 5 liegt, alternative Nischen vorschlagen
- Die Perplexity-Ergebnisse können halluzinierte Daten enthalten — bei offensichtlichen Ungereimtheiten darauf hinweisen
- Alle 3 Recherchen parallel ausführen für Geschwindigkeit
