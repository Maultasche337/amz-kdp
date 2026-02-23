# Publisher Rocket Auswertung — Serien-Settings für Maja Sternberg
*Komplett-Analyse: 2026-02-22 | 34 CSV-Exporte (Suki Bluhm ignoriert, 2 Duplikate markiert)*
*~340 einzigartige Keywords ausgewertet, ~450 Datenpunkte*

---

## Datenqualität & Hinweise

### Verfügbare Regionen
| Region | Typ | Anzahl Suchen | Status |
|--------|-----|--------------|--------|
| Eifel | Book + eBook | 5 | ✅ |
| Allgäu | eBook | 6 (1 Duplikat) | ✅ |
| Tirol/Zillertal (Kontrolle) | Book | 4 | ✅ |
| Genre: Heimatroman Romanze | eBook | 1 | ✅ |
| Genre: Small Town Romance | eBook | 2 | ✅ |
| Genre: Second Chance / Zweite Chance | eBook | 2 | ✅ |
| Comp: Frauenroman Neuanfang | Book | 1 | ✅ |
| Comp: Kleinstadtromance | eBook | 1 | ✅ |
| Comp: Katrin Emilia Buck | Book | 1 | ✅ |
| Comp: Später im Leben Romantik | eBook | 1 | ✅ |
| Comp: Later in Life Romance Deutsch | eBook | 1 | ✅ |
| Comp: L.B. Dunbar | eBook | 1 | ✅ |
| Comp: Lana Stone | eBook | 1 | ✅ |
| Comp: Liebesroman ab 40 | eBook | 1 | ✅ |
| Comp: Susie Tate | eBook | 1 | ✅ |
| Suchintent: Liebesroman 40+ | eBook | 1 | ✅ |
| Suchintent: Liebesromane für Frauen ab 40 | eBook | 2 (1 Duplikat) | ✅ |
| Suchintent: Neuanfang Liebesroman | eBook | 1 | ✅ |
| Suchintent: Neuanfang Romance Deutsch | eBook | 2 (fast Duplikat) | ✅ |

### Fehlend
Sächsische Schweiz, Berchtesgaden, Pfälzerwald, Vinschgau, Salzkammergut, Kategorien-Check, Reverse ASIN

### ⚠️ Book vs. eBook — nicht direkt vergleichbar!
Eifel und Tirol wurden als **Book** gesucht, Allgäu als **eBook**. Die Unterschiede:
- Book-Preise: 9–16 € | eBook-Preise: 1–11 €
- Gleiche Keywords zeigen je nach Format **verschiedene Werte** (z.B. „liebesroman österreich": Book = 545 €/Schwierigkeit 1, eBook = 312 €/Schwierigkeit 64)
- Einkommen ist ein **Durchschnitt der Top-Ergebnisse** — wird von Mega-Sellern nach oben verzerrt

### ⚠️ Duplikate erkannt
- Die beiden Dateien „ALLGÄU LIEBESROMAN 19.55.04" und „19.55.48" enthalten **identische Daten**.
- Die beiden Dateien „LIEBESROMANE FÜR FRAUEN AB 40 21.28.09" und „21.28.56" enthalten **identische Daten**.
- Das zweite „NEUANFANG ROMANCE DEUTSCH" (21.26.42) ist fast identisch mit 21.25.58, enthält aber ein zusätzliches Keyword („new beginning romance deutsch" — 825 Suchen).

---

## 1. Perplexity vs. Rocket — Faktencheck

| Keyword | Perplexity behauptet | Rocket zeigt | Abweichung |
|---------|---------------------|--------------|------------|
| „Eifel Heimatroman" | 12.000+ Suchen/Mo | **<50** | ~240× übertrieben |
| „Allgäu Roman" | 15.000 Suchen/Mo | **<50** | ~300× übertrieben |
| „Sächsische Schweiz Roman" | 9.500 Suchen/Mo | nicht getestet | — |
| „Berchtesgaden Roman" | 11.000 Suchen/Mo | nicht getestet | — |
| „Vinschgau Liebesroman" | 10.500 Suchen/Mo | nicht getestet | — |

**Fazit:** Perplexity hat Suchvolumina um Faktor **200–300× übertrieben**. Alle regionalen Keywords auf amazon.de haben <50 Suchen/Monat. Die Perplexity-Scores sind als Ranking unbrauchbar.

Aber: Das heißt **nicht**, dass der Markt tot ist. Leserinnen finden Bücher über:
- Breite Genre-Keywords („frauenromane", „liebesroman österreich")
- Kategorien-Browsing & Also-Boughts
- Small-Town/Heimat-Genre-Tags

---

## 2. Regionen-Vergleich

### Eifel (5 Book + eBook Suchen)

| Keyword | Typ | Konkurrenten | Preis | Ø Einkommen | Suchen | Schwierigkeit |
|---------|-----|-------------|-------|-------------|--------|---------------|
| **liebesroman eifel** | Book | 272 | 14 € | **199 €** | <50 | 1 🟢 |
| **eifel liebesroman** | Book | 320 | 13 € | **170 €** | <50 | 1 🟢 |
| **eifel roman frauen** | Book | 192 | 16 € | **166 €** | <50 | 1 🟢 |
| historische romane eifel | Book | 479 | 15 € | 137 € | 128 | 16 🟢 |
| historischer roman eifel | Book | 491 | 15 € | 119 € | <50 | 13 🟢 |
| romane aus der eifel | Book | 1.000 | 13 € | 117 € | <50 | 20 🟢 |
| eifel heimatroman | eBook | 64 | 8 € | 77 € | <50 | 1 🟢 |
| liebesroman pfalz | Book | 90 | 11 € | 19 € | <50 | 1 🟢 |

**Stärken:** Konstant niedrige Schwierigkeit (1–20), hohe TB-Preise (13–16 €), solide 170–199 €
**Schwächen:** Kein einzelner Ausreißer nach oben, relativ viele Konkurrenten (272–491)

---

### Allgäu (6 eBook Suchen)

| Keyword | Konkurrenten | Preis | Ø Einkommen | Suchen | Schwierigkeit |
|---------|-------------|-------|-------------|--------|---------------|
| **liebesroman allgäu** | **63** | 3 € | **283 €** | <50 | 25 🟢 |
| allgäu roman frauen | 34 | 8 € | 98 € | <50 | 13 🟢 |
| allgäu liebesroman | 60 | 6 € | 65 € | <50 | 13 🟢 |
| historischer roman allgäu | 32 | 9 € | 57 € | <50 | 25 🟢 |
| heimatroman allgäu alm | 10 | 9 € | 49 € | <50 | 1 🟢 |
| allgäu liebesgeschichte | 17 | 11 € | 44 € | <50 | 1 🟢 |
| allgäu roman | 159 | 6 € | 29 € | <50 | 13 🟢 |
| roman allgäu | 187 | 8 € | 15 € | <50 | 2 🟢 |

**Stärken:** Extrem wenig Konkurrenten (10–63!), bestes Einkommen-pro-Konkurrent-Verhältnis aller Regionen
**Schwächen:** eBook-Preise niedrig (3–11 €), TB-Daten fehlen (wahrscheinlich besser)

**Breitere Bayern-Keywords (Dach-Keywords für Allgäu):**

| Keyword | Konkurrenten | Preis | Ø Einkommen | Schwierigkeit |
|---------|-------------|-------|-------------|---------------|
| bayerische romane | 734 | 9 € | 265 € | 5 🟢 |
| romane schwäbische alb | 121 | 14 € | 132 € | 13 🟢 |
| romane oberbayern | 270 | 9 € | 97 € | 11 🟢 |

---

### Tirol/Südtirol (4 Book-Suchen)

| Keyword | Konkurrenten | Preis | Ø Einkommen | Suchen | Schwierigkeit |
|---------|-------------|-------|-------------|--------|---------------|
| **südtirol roman** | 1.000 | 12 € | **632 €** | <50 | 15 🟢 |
| historischer roman tirol | 275 | 12 € | **328 €** | <50 | 1 🟢 |
| romane aus südtirol | 1.000 | 14 € | 306 € | <50 | 33 🟢 |
| **liebesroman tirol** | 273 | 9–10 € | **196–225 €** | <50 | 1 🟢 |
| südtirolromane | 1.000 | 12 € | 212 € | <50 | 40 🟢 |
| familienroman südtirol | 219 | 13 € | 181 € | <50 | 1 🟢 |
| liebesroman aus südtirol | 153 | 11 € | 173 € | <50 | 20 🟢 |
| romane südtirol | 1.000 | 13 € | 159 € | <50 | 15 🟢 |
| südtirol romane | 1.000 | 12 € | 138 € | <50 | 20 🟢 |
| tirol roman frauen | 120 | 15 € | 81 € | <50 | 1 🟢 |
| tirol heimatroman | 361 | 11 € | 74 € | <50 | 1 🟢 |
| liebesromane tirol | 255 | 11 € | 50–75 € | <50 | 1 🟢 |

**Stärken:** Höchstes absolutes Einkommen (632 €!), breites Südtirol-Keyword-Universum, Zugang zu „liebesroman österreich"
**Schwächen:** Mehr Konkurrenten bei breiteren Keywords (1.000), etwas niedrigere Preise als Eifel

### Zillertal separat (Micro-Nische)

| Keyword | Konkurrenten | Preis | Ø Einkommen | Schwierigkeit |
|---------|-------------|-------|-------------|---------------|
| zillertal roman | 81 | 14 € | 31 € | 1 🟢 |
| zillertal liebesroman | 18 | 3 € | 5 € | 1 🟢 |
| roman zillertal | 65 | 8 € | 3 € | 26 🟢 |

**Fazit Zillertal:** Allein **zu klein** (3–31 €). Funktioniert nur als Setting innerhalb einer Tirol/Südtirol-Serie. Nicht als eigenständiges Keyword tauglich.

---

## 3. Ranking der Regionen

| Rang | Region | Bester Kern-Wert | Konkurrenten (Kern) | Breit-Keyword | Schwierigkeit | Score |
|------|--------|-----------------|---------------------|---------------|---------------|-------|
| 🥇 | **Allgäu** | 283 € (63 Konk.) | 10–63 | bayerische romane 265 €/5 | 1–25 🟢 | **Bestes Verhältnis** |
| 🥈 | **Tirol/Südtirol** | 225 € (273 Konk.) | 120–1.000 | südtirol roman 632 €/15 | 1–40 🟢 | **Höchstes Einkommen** |
| 🥉 | **Eifel** | 199 € (272 Konk.) | 192–491 | hist. romane eifel 137 €/16 | 1–20 🟢 | **Höchste TB-Preise** |
| 4 | Zillertal (eng) | 31 € (81 Konk.) | 18–81 | — | 1–26 🟢 | Zu klein allein |

### Warum Allgäu #1?
- **283 € / 63 Konkurrenten = 4,49 € pro Konkurrent** (bester Wert)
- Eifel: 199 € / 272 = 0,73 €
- Tirol: 225 € / 273 = 0,82 €
- Die wenigen Konkurrenten bedeuten: Leichter auf Seite 1 rankbar
- Dazu kommt „bayerische romane" (265 €, Schwierigkeit 5) als Dach-Keyword

### Warum Tirol/Südtirol #2?
- **632 € bei „südtirol roman"** — höchster Einzelwert aller Keywords
- Zugang zum Goldkeyword „liebesroman österreich" (545 €, 397 Suchen)
- Aber: 1.000 Konkurrenten bei den breiteren Keywords

### Warum Eifel #3?
- Konstant solide (170–199 €), durchgehend Schwierigkeit 1
- **Höchste TB-Preise aller Regionen** (13–16 €) — höhere Marge pro Verkauf
- Aber: Weder das beste Einkommen noch die wenigsten Konkurrenten
- Kein „Super-Keyword" als Dach verfügbar

---

## 4. Goldkeywords — Die wichtigsten Entdeckungen

### Tier 1: Muss in jedes KDP-Buch

| Keyword | Suchen/Mo | Ø Einkommen | Konkurrenten | Schwierigkeit | Warum |
|---------|-----------|-------------|-------------|---------------|-------|
| **second chance liebesroman deutsch** | **203** 🟡 | **499 €** | 4.000 | **36 🟢** | 🏆 Bestes Verhältnis Einkommen/Schwierigkeit |
| **second chance romanze deutsch** | **451** 🟢 | **567 €** | 4.000 | **38 🟢** | 🏆 Hohes Volumen + grüne Schwierigkeit |
| **unabhängige frauen roman** | 1.336 (B) / 2.924 (eB) | 649 € (B) / 3.017 € (eB) | 203–566 | 13–49 | Perfekt für 40+/50+ Neuanfang |
| **liebesroman österreich** | 397–407 | 312–545 € | 386–1.000 | 1 (B) / 64 (eB) | Dach-Keyword für Österreich-Settings |
| **small town romance deutsch** | 68 | 311 € | 2.000 | 43 🟡 | Engl. Genre-Tags auf amazon.de |

### Tier 2: Starke Zusatz-Keywords

| Keyword | Suchen/Mo | Ø Einkommen | Konkurrenten | Schwierigkeit | Warum |
|---------|-----------|-------------|-------------|---------------|-------|
| **liebesroman mit zweiter chance** | **1.929** 🟢 | **956 €** | 1.000 | 58 🟡 | Höchstes Suchvolumen aller Keywords! |
| **second chance liebesromane deutsch** | **434** 🟢 | **1.335 €** | 4.000 | 51 🟡 | Sehr hohes Einkommen |
| **second chance romance deutsch** | **245** 🟡 | **1.048 €** | 3.000 | 57 🟡 | Vierstelliges Einkommen |
| **starke frauen romane** | <50 | 3.788 € (eB) | 6.000 | 36 🟢 | Hohes Einkommen, grüne Schwierigkeit |
| **small town romanze** | 366 | 180 € | 50.000 | 35 🟢 | Breitestes Hybrid-Keyword |
| **heimat roman** (Leerzeichen!) | <50 | 465 € | 6.000 | 38 🟢 | Besser als „heimatroman" (70 🔴!) |
| **slow burn romance deutsch** | 81 | 309 € | 2.000 | 60 🟡 | Passt zu unseren Büchern |
| **bayerische romane** | <50 | 265 € | 734 | 5 🟢 | Dach-Keyword für Allgäu |
| **familienroman deutsch** | 219 | 401 € | 20.000 | 29 🟢 | Breit, gute Schwierigkeit |
| **zeitgenössischer liebesroman** | 372 | 1.743 € | 60.000 | 36 🟢 | Sehr viel Einkommen |
| **südtirol roman** | <50 | 632 € | 1.000 | 15 🟢 | Bester regionaler Einzelwert |

### Tier 3: Nischen-Ergänzungen (für spezifische Bücher)

| Keyword | Ø Einkommen | Konkurrenten | Schwierigkeit | Einsatz |
|---------|-------------|-------------|---------------|---------|
| skifahren liebesroman | 128 € | 191 | 13 🟢 | Wintertitel |
| landwirt liebesroman | 97 € | 63 | 40 🟢 | Bauernhof-Setting |
| weihnachtsroman alpen | 93 € | 76 | 25 🟢 | Weihnachts-Special |
| sommerurlaub liebesroman | 219 € | 271 | 12 🟢 | Sommertitel |
| liebesroman deutsch skifahren | 110 € | 52 | 13 🟢 | Wintertitel, wenig Konkurrenz |
| cottagecore liebesroman | 52 € | 222 | 59 🟡 | Trend-Keyword |

### ⚠️ Finger weg (zu schwer oder irreführend)

| Keyword | Problem |
|---------|---------|
| **heimatroman** (zusammen) | Schwierigkeit **70 🔴** — zu hart |
| **liebesroman** (allein) | 80.000 Konkurrenten, Schwierigkeit 61 |
| **frauenroman** (allein) | 20.000 Konkurrenten, Schwierigkeit 50 |
| **zweite chance** (allein) | Schwierigkeit **91 🔴** — viel zu hart! |
| **second chance** (allein) | 60.000 Konkurrenten, Schwierigkeit 84 🔴 |
| spicy romance small town | Spicy ≠ Clean — falsche Zielgruppe |
| wild love | Schwierigkeit 84 🔴, englischsprachige Konkurrenz |
| dark romance deutsch zweite chance | Dark ≠ Clean — falsche Zielgruppe |

---

## 5. Second Chance / Zweite Chance — Deep Dive (eBook)

Das **stärkste Trope** das wir gefunden haben. Massives Suchvolumen, hohe Einkommen, viele grüne Such-Indikatoren (= Amazon bestätigt echtes Volumen).

### Top-Keywords sortiert nach Einkommen × Schwierigkeit

| Keyword | Suchen/Mo | Ø Einkommen | Konk. | Schwierigkeit | Bewertung |
|---------|-----------|-------------|-------|---------------|-----------|
| **second chance romanze deutsch** | **451** 🟢 | **567 €** | 4.000 | **38 🟢** | 🏆 BESTER GESAMTWERT |
| **second chance liebesroman deutsch** | **203** 🟡 | **499 €** | 4.000 | **36 🟢** | 🏆 BESTE SCHWIERIGKEIT |
| **second chance liebesromane deutsch** | **434** 🟢 | **1.335 €** | 4.000 | 51 🟡 | Hohes Einkommen |
| **second chance romance deutsch** | **245** 🟡 | **1.048 €** | 3.000 | 57 🟡 | Vierstellig |
| **liebesroman mit zweiter chance** | **1.929** 🟢 | **956 €** | 1.000 | 58 🟡 | 🏆 MEISTE SUCHEN |
| **romance mit zweiter chance** | **401** 🟢 | **884 €** | 1.000 | 63 🟡 | Wenig Konkurrenten |
| **second chance deutsch** | **1.346** 🟡 | **865 €** | 4.000 | 44 🟡 | Breit, stark |
| zweite chance romance deutsch | 131 | 819 € | 6.000 | 60 🟡 | |
| liebesromane deutsch second chance | 193 | 601 € | 3.000 | 62 🟡 | |
| second chance romanze deutsch | (s.o.) | | | | |
| romantik der zweiten chance | 297 🟡 | 481 € | 1.000 | 55 🟡 | |
| zweite-chance-liebesroman | 354 | 479 € | 6.000 | 53 🟡 | |
| romance deutsch zweite chance | 165 | 385 € | 6.000 | 64 🟡 | |
| zweite chance liebesromane deutsch | 105 | 355 € | 6.000 | 48 🟡 | |
| **slow burn romance deutsch** | 81 | **309 €** | 2.000 | 60 🟡 | Bonus-Trope! |
| zweite chance romance | 166 | 283 € | 6.000 | 64 🟡 | |
| 2. chance deutsch liebesroman | <50 | 247 € | 1.000 | 35 🟢 | Nischig |
| liebesromane deutsch zweite chance | <50 | 180 € | 6.000 | 37 🟢 | |
| second-chance romance | 487 | 143 € | 50.000 | **17 🟢** | Niedrigste Schwierigkeit |
| second chance romance deutsch ehe | <50 | 42 € | 343 | 57 🟡 | Zu spezifisch |

### Erkenntnisse Second Chance

- ✅ **Das ist DAS Trope für unsere Bücher.** Neuanfang 40+/50+ = Second Chance per Definition.
- ✅ **„liebesroman mit zweiter chance"** hat **1.929 bestätigte Suchen** (grün!) — das höchste verifizierte Volumen aller unserer Keywords
- ✅ **Zwei Keywords mit grüner Schwierigkeit UND hohem Einkommen:**
  - „second chance romanze deutsch" (451 Suchen, 567 €, **Diff. 38 🟢**)
  - „second chance liebesroman deutsch" (203 Suchen, 499 €, **Diff. 36 🟢**)
- ✅ Deutsche Varianten performen besser als rein englische
- ✅ **Bonus-Fund:** „slow burn romance deutsch" (309 €, 81 Suchen) — passt auch zu unserem Stil
- ⚠️ Die generischen Varianten ohne „deutsch" haben 50.000+ Konkurrenten — immer „deutsch" dazupacken
- ⚠️ „zweite chance" allein = Schwierigkeit **91 🔴** — nie als alleiniges Keyword nutzen!

### Die Killer-Kombination

**Region (grüne Schwierigkeit) + Trope (hohes Suchvolumen) = unser Rezept**

| Region-Keyword (Schwierigkeit 1–25) | + | Trope-Keyword (451–1.929 Suchen) |
|--------------------------------------|---|-----------------------------------|
| liebesroman allgäu (63 Konk.) | + | second chance romanze deutsch (451 Suchen) |
| liebesroman eifel (272 Konk.) | + | liebesroman mit zweiter chance (1.929 Suchen) |
| liebesroman tirol (273 Konk.) | + | second chance liebesroman deutsch (203 Suchen) |

Die Region sorgt für **wenig Konkurrenz auf Seite 1**, der Trope bringt **Traffic über breitere Suchen**. Beides zusammen in den 7 KDP-Keywords = maximale Sichtbarkeit.

---

## 6. Daten-Auffälligkeiten (ehrliche Warnung)

### Gleiche Keywords, verschiedene Werte
Einige Keywords tauchen in mehreren Suchen auf und zeigen **unterschiedliche Werte**:

| Keyword | Book-Wert | eBook-Wert | Differenz |
|---------|-----------|------------|-----------|
| liebesroman österreich | 545 € / Diff. 1 | 312 € / Diff. 64 | -43% Einkommen, +63 Schwierigkeit |
| unabhängige frauen roman | 649 € / Diff. 13 | 3.017 € / Diff. 49 | +365% Einkommen, +36 Schwierigkeit |
| frauenromane | 702 € / Diff. 24 | 19.111 € / Diff. 54 | +2.623% Einkommen |

**Bedeutung:** Die Rocket-Werte sind **Durchschnitte der aktuellen Top-Ergebnisse**, nicht absolute Wahrheiten. Ein Mega-Seller (z.B. Emma Bishop mit 7.063 €/Mo) verzerrt den Durchschnitt massiv nach oben. Die eBook-Einkommen über 3.000 € sind mit Vorsicht zu genießen.

### Verlässlichere Werte
Regionale Keywords (Eifel, Allgäu, Tirol) sind **weniger verzerrt**, weil keine Mega-Seller in der Nische sitzen. Dort sind die Einkommen realistischer:
- 150–300 € Durchschnittseinkommen = **realistisch erreichbar**
- 500–600 € (z.B. südtirol roman) = **oberes Ende, mit guter Serie machbar**
- 3.000+ € = **Ausreißer, nicht als Ziel setzen**

---

## 6. Competition Analyzer

### Frauenroman Neuanfang (Book)

| Titel | Autor | ⭐ | Reviews | ABSR | Preis | Umsatz/Mo |
|-------|-------|----|---------|------|-------|-----------|
| Das Echo vergessener Bücher | Barbara Davis | 4,4 | 140 | 23.821 | 16,46 € | **874 €** |
| Villa Strandbrise — See der Träume | Mia Peters | 4,2 | 3.383 | 35.155 | 11,99 € | **480 €** |
| Kleine Bäckerei am Strandweg | Jenny Colgan | 4,4 | 988 | 39.183 | 13 € | **461 €** |
| Neuanfang in Notting Hill | Norie Clarke | 4,2 | 214 | 62.605 | 13 € | 119 € |
| Neuanfang auf Sylt | Nadine Feger | 4,1 | 24 | 357.175 | 12,99 € | 104 € |
| Villa Strandbrise — Leuchten d. Horizonts | Mia Peters | 4,3 | 1.077 | 78.133 | 11,99 € | 88 € |
| Sommerhimmel über der Toskana | Sarah Short | 4,1 | 37 | 316.456 | 18 € | 180 € |
| Mondlichtfrauen | Barbara Davis | 4,3 | 97 | 221.198 | 12 € | 168 € |

**Erkenntnisse:**
- 12–16 € TB-Preis ist der Sweet Spot
- **Serien > Einzeltitel:** Mia Peters generiert zusammen ~570 €/Mo mit Villa Strandbrise
- Bewertungen 4,1–4,4 reichen
- ABSR unter 40.000 = funktionierendes Buch (~15–20+ Verkäufe/Mo)

### Kleinstadtromance (eBook)

| Titel | Autor | Reviews | ABSR | Preis | Umsatz/Mo |
|-------|-------|---------|------|-------|-----------|
| Ein schottischer Buchladen | Emma Bishop | 219 | **448** | 8,99 € | **7.063 €** |
| Defending a Promise | Annie Carlisle | 0 | 132.224 | 6,99 € | 133 € |
| Under Our Stars | Ronja Sova | 78 | 163.545 | 5,87 € | 100 € |
| Schneegestöber im Katzencafé | Rachel Rowlands | 19 | 350.972 | 10,99 € | 88 € |
| Zweite Chancen… | Lissy König | 3 | 117.375 | 3,99 € | 80 € |
| Verwöhnter Erbe… | Lissy König | 3 | 117.881 | 3,99 € | 80 € |

**Erkenntnisse:**
- **Winner-takes-all:** Ein Buch (Emma Bishop) dominiert mit 7.063 €/Mo
- Alle anderen unter 135 €/Mo — extrem steile Verteilung
- **Unser Vorteil:** TB-First statt eBook-Preiskampf bei 3,99 €
- Elsie Silver (nicht im Comp, aber in Keyword-Daten) macht 1.035 €/Mo — Referenz-Autorin

### Katrin Emilia Buck — Case Study: Serien-Explosion (Book, eBook)

Aktuell eine der heißesten deutschen Romance-Autorinnen. Zwei Serien, komplett unterschiedliche Performance:

**Hearts of Starlight Springs (eBook, 3,99–4,99 €) — Small Town Romance:**

| Titel | Band | Alter | ABSR | €/Tag | €/Mo | Reviews | Tropes im Untertitel |
|-------|------|-------|------|-------|------|---------|---------------------|
| **Falling Twice** | 7 | **5 Tage** | **50** | **289 €** | **6.650 €** | 89 | **Zweite Chance**, Highschoolliebe |
| Silent Dreams | 6 | 68 Tage | 1.065 | 39 € | 894 € | 548 | Single Dad, Cowboy |
| Suits & Surprises | 5 | 117 Tage | 1.823 | 33 € | 770 € | 556 | Baby, Anwalt |
| Rink & Romance | — | 348 Tage | 1.604 | 30 € | 696 € | 1.650 | Spicy Hockey |
| Fakes & Fireworks | 8 | -64 (Preorder!) | 1.864 | 26–31 € | 601–707 € | — | Fake Boyfriend |
| Fake Feelings | 4 | 166 Tage | 2.750 | 26 € | 603 € | 658 | Fake Dating, Anwalt |
| **Serien-Total** | | | | **~443 €/Tag** | **~10.200 €/Mo** | | |

**San Antonio Billionaires (TB, 12,99 €) — Billionaire Romance:**

| Titel | Band | Alter | ABSR | €/Tag | €/Mo | Reviews |
|-------|------|-------|------|-------|------|---------|
| Security-CEO | 11 | 768 Tage | 247.590 | 1–2 € | 169–199 € | 1.816 |
| Security-Specialist | 15 | 530 Tage | 302.836 | 1 € | 130 € | 1.290 |
| Fake-verliebt Anwalt | 9 | 950 Tage | 353.200 | 1 € | 104 € | 2.049 |
| Nanny Single-Dad | 12 | 712 Tage | 406.417 | 1 € | 65 € | 1.579 |
| **Serien-Total** | | | | **~4 €/Tag** | **~480 €/Mo** | | |

**Was hier abgeht:**

1. **Falling Twice: ABSR 50 nach 5 Tagen.** Das ist Top 50 von GANZ Kindle Deutschland. 89 Reviews in 5 Tagen = ~18 Reviews/Tag = massive ARC-Armee + organische Käufer.

2. **Das Serien-Flywheel:** Jedes neue Buch pusht die alten über Also-Boughts hoch. Die ganze Starlight-Springs-Serie macht zusammen **~10.200 €/Mo** — und das nächste Buch (Fakes & Fireworks) ist schon im Preorder und generiert bereits 600+ €/Mo.

3. **eBook-Serie bei 3,99 € schlägt TB-Serie bei 12,99 € um Faktor 20x:**
   - Starlight Springs (eBook): ~10.200 €/Mo über 6 Titel
   - San Antonio (TB): ~480 €/Mo über 4 Titel
   - Dabei hat San Antonio **viel mehr Reviews** (1.290–2.049 pro Buch!) — aber die alte Billionaire-Nische ist tot.

4. **„Zweite Chance" direkt im Untertitel** von Falling Twice — und es ist ihr erfolgreichstes Buch ever. Das validiert unsere Second-Chance-Keyword-Strategie.

5. **Taktrate:** Band 4–7 in ~160 Tagen = **ein Buch alle 40 Tage**. Schnelle Veröffentlichung hält den Algorithmus warm.

**Was wir lernen:**

| Lektion | Bedeutung für uns |
|---------|-------------------|
| Serien-Flywheel ist real | Schnelle Folgebücher sind wichtiger als perfekte Einzeltitel |
| „Zweite Chance" im Untertitel = Klick-Magnet | Sollten wir bei unseren Büchern auch testen |
| 3,99 € eBook > 12,99 € TB (bei Romance) | Für ein spicy/NA-Pseudonym wäre eBook-First die richtige Strategie |
| ARC-Team = Launch-Rakete | 18 Reviews/Tag ab Tag 1 ist kein Zufall — das ist organisiert |
| Billionaire-Nische stirbt, Small Town lebt | Bestätigt unsere Small-Town-Strategie |
| ~10.000 €/Mo mit 6 eBooks bei 3,99 € | Das ist das Potenzial einer gut laufenden Romanze-Serie |

**⚠️ Aber:** Buck schreibt spicy New Adult / Contemporary Romance für 20–35-jährige. Das ist eine **komplett andere Zielgruppe** als unsere Clean Romance 40+. Ihre Also-Boughts würden unsere Bücher nicht anzeigen. Für ein **drittes Pseudonym** in Richtung spicy/NA wäre das allerdings ein extrem attraktives Modell.

### Later-in-Life Romance — Marktanalyse (2 Competition Analyzer)

Die zentrale Frage für Maja Sternberg: Gibt es deutsche Later-in-Life Romance? **Nein.**

Zwei Suchen ("Später im Leben Romantik" + "Later in Life Romance Deutsch") ergeben zusammen:

**Echte Later-in-Life Bücher auf amazon.de (dedupliziert):**

| Titel | Autor | Alter | ABSR | €/Mo | Preis | Reviews | Typ |
|-------|-------|-------|------|------|-------|---------|-----|
| Die Liebe, später | Gisa Klönne | 26 Tage | 7.507 | **1.174–1.385 €** | 19,99–23,57 € | 111 | Literarische Fiktion |
| Zwischen uns ein ganzes Leben | Melanie Levensohn | 2.797 Tage | 4.112 | **510 €** | 3,99 € | 1.621 | Literarische Fiktion (Evergreen!) |
| Zweite Chance in der Liebe | L.B. Dunbar | 724 Tage | 156.586 | 90–106 € | 4,99 € | 73 | Steamy Silberfuchs-Kollektion |
| Liebe nebenan | L.B. Dunbar | 654 Tage | 107.640 | 100 € | 4,99 € | 63 | Steamy Silberfuchs-Kollektion |
| Midlife Crisis | L.B. Dunbar | 906 Tage | 133.515 | 95–112 € | 4,99 € | 145 | Steamy Silberfuchs-Kollektion |
| A Christmas for Chrissie | D.E. Haggerty | 197 Tage | 135.391 | 95 € | 4,99 € | 10 | Übersetzung, Love Will Out 5 |
| Endlich Mein | Elena Aitken | 446 Tage | 275.089 | 60 € | 4,99 € | 16 | Übersetzung |
| Ein Leben später | Annette Hohberg | 296 Tage | 95.048 | 18 € | 14,99 € | 54 | Neuanfang-Thema |
| Späte Liebe | Nina Potter | 612 Tage | 140.304 | 18 € | 0,99 € | 13 | Second Chance Liebesroman |
| Her New Romance Later in Life | Anna Hart | 62 Tage | — | 0 € | 0,89 € | 2 | Englisch, 35 Seiten, tot |

**Erkenntnisse:**
- Die Nische existiert auf Deutsch **quasi nicht**. Amazon zeigt bei beiden Suchen hauptsächlich irrelevante allgemeine Romance.
- Nur **2 Bücher** machen echtes Geld — und beide sind literarische Fiktion (Klönne 1.385 €, Levensohn 510 €), keine Serien-Romance.
- **L.B. Dunbar** ist die einzige Later-in-Life-Serie auf Deutsch — aber steamy/spicy ("Sexy Silberfuchs"), nicht clean/slow burn. Macht zusammen nur ~300 €/Mo mit 3 übersetzten Büchern.
- **D.E. Haggerty** und **Elena Aitken** sind Übersetzungen mit 8–16 Reviews — nicht optimiert für den deutschen Markt.
- Es gibt **null** deutsche Clean Later-in-Life Serien-Romance. Maja Sternberg wäre die Erste.

**L.B. Dunbar im Detail — warum sie keine Konkurrenz ist:**

| Metrik | L.B. Dunbar (Silberfuchs) | Maja Sternberg (geplant) |
|--------|--------------------------|--------------------------|
| Ton | Steamy/Spicy | Clean/Slow Burn |
| Sprache | Übersetzung aus Englisch | Deutsch-Original |
| Setting | USA (generisch) | Regionale Heimat (Tirol, Allgäu, Eifel) |
| Titel-Stil | "Midlife Crisis", "Sexy Silberfuchs" | Emotionaler Ort + Gefühl |
| €/Mo (3 Bücher) | ~300 € | Ziel: 400–600 € pro Buch |
| Zielgruppe | Steamy-Leserinnen 40+ | Clean-Leserinnen 40+ |
| Reviews (deutsch) | 63–145 | — |

### Lana Stone — Case Study: Boss/Billionaire Romance (Competition Analyzer)

Zum Vergleich mit Buck (Small Town) und Dunbar (Later-in-Life): Lana Stone bedient die **Boss/Billionaire-Nische** mit ihrer „New York Billionaires"-Serie.

**Profil:**
- ~16+ Bücher, Preisrange 0,99–3,53 € (eBook)
- Geschätzter Gesamtumsatz: **~5.000 €/Mo**
- Ton: Spicy, Urban, Billionaire/Boss-Trope
- Setting: New York (Großstadt), nicht Small Town

**Top-Titel:**

| Titel | Alter (Tage) | ABSR | €/Mo (ca.) | Anmerkung |
|-------|-------------|------|------------|-----------|
| Breathless for my Boss | 32 | 201 | **~1.500 €** | Frischer Launch, starker Einstieg |
| DU BIST MEIN (NYB 1) | 3.092 | 615 | **~1.500 €** | Evergreen seit 8+ Jahren! |
| Grumpy Boss (NYB 14) | 489 | — | ~420 € | Solider Backlist-Titel |
| Bound by the Boss (NYB 16) | 305 | — | ~400 € | Neuester Serien-Eintrag |

**Relevanz für uns:**
- Bestätigt das Serien-Flywheel: 16+ Bücher = stabiler Umsatz, auch alte Titel verdienen
- „DU BIST MEIN" (3.092 Tage alt, ~1.500 €/Mo) zeigt: **Evergreens existieren** auch bei Billig-eBooks
- **Andere Sub-Nische als Buck:** Urban Billionaire vs. Small Town — Lana Stone fischt in einem völlig anderen Teich
- Relevant als Vergleich für ein mögliches **Pseudonym 3** (spicy Romance), aber **nicht** für Maja Sternberg (clean/Heimat)
- Preise (0,99–3,53 €) bestätigen den eBook-Preiskampf in der spicy Nische — TB-First bleibt für Maja die bessere Strategie

### Competition Analyzer: Liebesroman ab 40 — Was man falsch machen kann

Die CSV enthielt 10 deduplizierte Bücher. **Kein einziges funktioniert richtig.** Das ist gleichzeitig erschreckend und eine Riesenchance.

| Titel | Autor | Alter | ABSR | Seiten | Preis | €/Mo | Problem |
|-------|-------|-------|------|--------|-------|------|---------|
| Das ungekürzte Leben der Missy Kinkaid | Kirsten Pursell | 131 T | 54 | 329 | 0 € | 0 € | Free/KU only, kein Einkommen |
| Anfang 40 - Ende offen | Franka Bloom | 3.292 T | 12.153 | 408 | 9,99 € | 95 € | Zu teuer, kein Untertitel, 9 Jahre alt |
| Stethoskop und Schreibfeder | Maria Weinbauer | 147 T | 615.867 | 69 | 1,19 € | 1 € | 69 Seiten (!), 1,19 € = 35 % Royalty |
| Ab 40 wird's einfach nicht schwer | Sylvia Kling | 2.032 T | 174.397 | 290 | 6,99 € | 119 € | Alte Backlist, zu teuer |
| Liebe trotz allem | Annabelle Benn | 3.226 T | 1.027.070 | 326 | 4,99 € | 5 € | ABSR >1 Mio = tot |
| Endlich glücklich ab 40 | Ralf Weisbecker | 182 T | 304.638 | 106 | 9,99 € | 100 € | SACHBUCH, kein Roman! |
| Dating After 40... Weeks! | A.B. Taylor | 47 T | — | — | 2,69 € | 0 € | Englisch, Fehlplatzierung |
| Eine bessere Version von Liebe | Alea Kolling | 625 T | 247.272 | 281 | 3,99 € | 52 € | Unsichtbar |
| Die Kirschbauminsel | Daisy Landish | 32 T | — | 197 | 4,99 € | 0 € | WICHTIG: Macht genau unser Ding (Subtitle „zweite chance liebesroman ab 40", KWT=Yes) und scheitert trotzdem |
| Gefangen im Duft der Rosen | Anna Rusher | 202 T | 158.337 | 170 | 2,69 € | 48 € | Falsche Nische (Milliardär-Suspense) |

**Die 8 Todsünden dieser Nische:**

1. ❌ **Zu kurz schreiben** — Weinbauer mit 69 Seiten. Leserinnen erwarten 250–400 Seiten bei einem Liebesroman.
2. ❌ **Unter 2,99 € preisen** — 35 % statt 70 % Royalty. Weinbauer und Rusher verschenken die Hälfte ihrer Marge.
3. ❌ **Keinen Untertitel** — Franka Bloom hat 1.068 Reviews, aber keine Keywords im Untertitel. Damit ist sie für Amazon-Suchen unsichtbar.
4. ❌ **Keywords ohne Produkt** — Kirschbauminsel hat perfekte Keywords, aber 0 €. Kein Launch, kein ARC-Team, keine Serie = kein Umsatz.
5. ❌ **Falsche Kategorie** — Sachbücher (Weisbecker) und Milliardär-Suspense (Rusher) in der „ab 40"-Suche. Leserinnen klicken weg.
6. ❌ **Keine Serie aufbauen** — Fast alle hier sind Standalone. Kein Flywheel, keine Also-Boughts, kein Backlist-Effekt.
7. ❌ **Zu teuer** — 9,99 € und 6,99 € sind Verlagspreise. Self-Publisher-Sweet-Spot liegt bei 3,99–4,99 € (eBook) bzw. 12,99 € (TB).
8. ❌ **Keine Sichtbarkeits-Strategie** — Ohne Launch-Plan, ARC-Team und Preisaktionen versickert auch das beste Buch im Katalog.

**Schlussfolgerung:** Die Nische „Liebesroman ab 40" hat Nachfrage (~1.600 Suchen/Mo über alle Varianten) und **KEINE funktionierende Konkurrenz**. Kein einziges Top-10-Buch kombiniert die Grundlagen richtig: Richtiger Preis + Untertitel mit Keywords + Serie + Launch-Strategie. Das ist ein Markt, wo noch niemand das Produkt richtig gebaut hat. Für Maja Sternberg = Riesenchance.

### Case Study: Susie Tate — Mega-Launch durch Übersetzung

Susie Tate ist eine etablierte englischsprachige Romance-Autorin, deren Bücher jetzt ins Deutsche übersetzt werden — mit spektakulären Ergebnissen.

**Deutsche Übersetzungen (amazon.de):**

| Titel | Bewertungen | Alter | ABSR | Seiten | Preis | €/Mo |
|-------|------------|-------|------|--------|-------|------|
| **Unperfect – Liebe wider Willen** | 576 | 19 Tage | **14** | 424 | 4,99 € | **66.567 €** |
| Unworthy – Sehnsucht nach dir | — | Preorder (-43 T) | 2.443 | 350 | 4,99 € | 961 € |
| Unwanted – Verbotenes Verlangen | — | Preorder (-99 T) | 7.297 | 340 | 4,99 € | 298 € |

**Englische Backlist auf amazon.de:**

| Titel | Bewertungen | ABSR | €/Mo |
|-------|------------|------|------|
| Unperfect (EN) | 22.574 | 2.566 | 814 € |
| Unworthy (EN) | 11.673 | 3.404 | 576 € |
| Unwanted (EN) | 7.468 | 3.659 | 620 € |
| Outlier (EN) | 12.694 | 7.943 | 241 € |
| Daydreamer (EN) | 21.434 | 12.440 | 40 € |

**Was hier passiert:**

- **66.567 €/Mo = 2.200 € am Tag.** ABSR 14 nach 19 Tagen. Das ist 10× Katrin Emilia Bucks bester Launch.
- **ABER:** Tate ist eine etablierte englischsprachige Bestseller-Autorin mit 22.574+ Reviews, die ihre Hits ins Deutsche übersetzen lässt. Die englische Fanbase kauft sofort, BookTok/BookStagram promoten international, und die deutsche Übersetzung profitiert von jahrelangem englischem Momentum.
- **Das ist KEIN erreichbares Vorbild** für einen Self-Publisher-Neustart. Es zeigt aber, welches Umsatzpotenzial der deutsche Romance-Markt grundsätzlich hat.
- **Trotzdem relevant für uns:** Deutsche Leserinnen sind hungrig nach „Workplace Romance" + „Enemies to Lovers" + „Grumpy meets Sunshine" (ihre Untertitel!). Diese Tropes überlappen mit Bucks erfolgreichsten Titeln.
- **Tates Tropes vs. unsere:** Workplace, Grumpy×Sunshine, Enemies to Lovers — das sind Mainstream-Romance-Tropes für 20–35-Jährige. Für Maja Sternberg (Clean, 40+, Heimat) nicht direkt übertragbar, aber als Markt-Signal relevant: Die Nachfrage nach deutschsprachiger Romance wächst massiv.

---

## 6b. Suchintent-Analyse: Was Leserinnen wirklich eingeben

Fünf neue Keyword-Suchen (21.22–21.28) zeigen, wie die Zielgruppe **tatsächlich auf Amazon sucht** — und das weicht deutlich von Genre-Labels ab.

### Kernbefund: Leserinnen suchen NICHT „Later in Life Romance"

Sie suchen stattdessen:
- **„liebesroman ab 40"** / **„liebesromane für frauen ab 40"** / **„bücher für frauen ab 40"**
- **„neuanfang"** / **„second chance"** / **„new beginning"**
- **„frauenroman ab 40"** / **„roman für frauen ab 40"**

Der englische Genre-Term „Later in Life Romance" hat auf amazon.de quasi **null Suchvolumen**. Die Leserinnen denken in Altersgruppen und Lebensthemen, nicht in Genre-Fachbegriffen.

### „Ab 40"-Keywords — Gesamtübersicht

| Keyword | Suchen/Mo | Ø Einkommen | Difficulty | Bewertung |
|---------|-----------|-------------|------------|-----------|
| **liebesromane für frauen ab 40** | **389** 🟢 | **1.034 €** | 53 🟡 | 🏆 Höchstes Volumen |
| **romane für frauen ab 40** | 233 🟡 | 6.857 € ⚠️ | 54 🟡 | Einkommen = Ausreißer |
| **bücher für frauen ab 40** | 221 🟡 | 1.396 € | **33 🟢** | 🏆 Niedrige Schwierigkeit + hohes Einkommen |
| **liebesromane ab 40** | 209 🟡 | 604 € | **33 🟢** | 🏆 Bestes Gesamtpaket |
| **liebesroman ü40** | 168 | 179 € | 60 🟡 | Abkürzung funktioniert |
| **liebesroman ab 40** | 152 | 18.431 € ⚠️ | 44 🟡 | Einkommen = extremer Ausreißer |
| **liebesroman für alle über 40** | 150 | 117 € | **6 🟢** | 🏆 Niedrigste Schwierigkeit |
| **liebesroman über 40** | 144 | 69 € | **36 🟢** | Solide |
| roman für frauen ab 40 | 103 | 855 € | 53 🟡 | |
| liebesroman für frauen 40+ | 87 | 3.341 € ⚠️ | **36 🟢** | Einkommen = Ausreißer |
| frauenromane ab 40 | 84 | 1.305 € | 57 🟡 | |
| romance für frauen ab 40 | <50 | 514 € | 44 🟡 | |
| liebesroman ab 40 sammelband | <50 | 2.448 € | **23 🟢** | Sammelband = hohe Marge! |
| frauenroman ab 40 | <50 | 147 € | **22 🟢** | |
| liebesroman frau ab 40 | <50 | 617 € | 53 🟡 | |
| **liebesroman ab 50** | **<50** | **16 €** | 63 🟡 | ☠️ Ab 50 = quasi tot |

**Gesamtvolumen aller „ab 40"-Varianten: ~1.600 Suchen/Mo**

### „Neuanfang"-Keywords — Gesamtübersicht

| Keyword | Suchen/Mo | Ø Einkommen | Difficulty | Bewertung |
|---------|-----------|-------------|------------|-----------|
| **second-chance liebesroman** | **986** | 1.122 € | 65 🟡 | Höchstes Volumen (ohne „deutsch") |
| **new beginning romance deutsch** | **825** 🟢 | 2.058 € | 61 🟡 | Englischer Term auf amazon.de! |
| **neuanfang romance deutsch** | 634 🟡 | 387 € | 65 🟡 | |
| **neuanfang liebesromane deutsch** | 351 🟡 | 734 € | 46 🟡 | |
| **liebesroman neue start** | 249 🟡 | 7.202 € ⚠️ | 48 🟡 | Einkommen = Ausreißer |
| **second chance liebesroman deutsch** | 203 🟡 | 499 € | **36 🟢** | 🏆 Bereits in Tier 1! |
| katrina verde (Autorin) | 122 | 180 € | 43 🟡 | Autorinnen-Suche |
| neuanfang liebesroman | 87 | 129 € | **22 🟢** | 🏆 Niedrige Schwierigkeit |
| romance mit neuanfang | 54 | 359 € | **22 🟢** | 🏆 Niedrige Schwierigkeit |
| frauenroman neuanfang liebe | <50 | 106 € | **20 🟢** | 🏆 Niedrigste Schwierigkeit |

**Gesamtvolumen aller „Neuanfang"-Varianten: ~1.400 Suchen/Mo**

**Bonus-Keyword:** „romance auf deutsch" hat **3.165 Suchen** 🟢, aber mit 5.837 € Einkommen bei Difficulty 56 — zu generisch für unsere 7 Keyword-Boxen.

### Strategische Erkenntnisse aus der Suchintent-Analyse

1. **Long-Tail schlägt Broad:** Die spezifischen Varianten (z.B. „liebesroman für alle über 40", Difficulty 6) sind viel leichter zu ranken als die generischen (z.B. „romane für frauen ab 40", Difficulty 54).

2. **Englische Terms funktionieren auf amazon.de:** „New beginning romance deutsch" hat 825 bestätigte Suchen — Leserinnen mischen Deutsch und Englisch in ihren Suchen.

3. **„Ab 50" ist quasi tot:** Nur <50 Suchen und 16 € Einkommen. Die Zielgruppe definiert sich als „ab 40", nicht „ab 50". Unser Branding sollte „40+" verwenden, nicht „50+".

4. **Einkommens-Ausreißer kritisch prüfen:** Die Werte 18.431 €, 6.857 €, 7.202 € und 3.341 € sind höchstwahrscheinlich durch einzelne Bestseller verzerrt (ein Mega-Seller unter den Top-Ergebnissen hebt den Durchschnitt). Die realistischen Werte liegen bei 100–1.400 €.

5. **Sammelband-Keywords = verstecktes Gold:** „Liebesroman ab 40 sammelband" hat nur Difficulty 23 🟢, aber 2.448 € Einkommen. Sobald 3+ Bücher existieren → Sammelband publizieren und dieses Keyword nutzen.

6. **Neuanfang + Ab 40 = doppeltes Suchvolumen:** Zusammen ~3.000 Suchen/Mo — mehr als „second chance" allein. Unsere Bücher bedienen beide Suchintents gleichzeitig.

---

## 7. Strategische Empfehlungen

### KDP-Keywords (7 Boxen) — Vorschlag pro Region

**Für Allgäu-Serie (Maja Sternberg):**
1. liebesroman allgäu
2. **liebesromane für frauen ab 40** ← NEU (389 Suchen 🟢, 1.034 €)
3. **second chance romanze deutsch** (451 Suchen, 567 €, Diff. 38 🟢)
4. **bücher für frauen ab 40** ← NEU (221 Suchen, 1.396 €, Diff. 33 🟢)
5. bayerische romane
6. heimat roman *(mit Leerzeichen!)*
7. unabhängige frauen roman

**Für Tirol/Südtirol-Serie (Maja Sternberg, inkl. Hanni & Beate):**
1. liebesroman tirol *(oder: südtirol roman)*
2. liebesroman österreich
3. **liebesromane ab 40** ← NEU (209 Suchen, 604 €, Diff. 33 🟢)
4. **second chance liebesroman deutsch** (203 Suchen, 499 €, Diff. 36 🟢)
5. **bücher für frauen ab 40** ← NEU (221 Suchen, 1.396 €, Diff. 33 🟢)
6. heimat roman
7. familienroman deutsch

**Für Eifel-Serie (Maja Sternberg):**
1. liebesroman eifel
2. **liebesromane für frauen ab 40** ← NEU (389 Suchen 🟢, 1.034 €)
3. **second chance romanze deutsch** (451 Suchen, 567 €, Diff. 38 🟢)
4. **liebesromane ab 40** ← NEU (209 Suchen, 604 €, Diff. 33 🟢)
5. heimat roman
6. eifel roman frauen
7. unabhängige frauen roman

> **Warum die Umstellung?** Die neuen „ab 40"-Keywords haben zusammen **~1.600 Suchen/Mo** bei durchgehend grüner bis gelber Schwierigkeit. Sie ersetzen „small town romance deutsch" (68 Suchen, Diff. 43) und „starke frauen romane" (<50 Suchen), weil sie deutlich mehr Traffic bringen und den tatsächlichen Suchintent unserer Zielgruppe treffen.

### Serienplanung — Empfohlene Reihenfolge

| Priorität | Region | Begründung |
|-----------|--------|------------|
| **Serie 2** | **Allgäu** | Wenigste Konkurrenz, bestes Verhältnis, Bayern-Dach-Keywords |
| **Serie 3** | **Eifel** | Höchste TB-Preise, konstant niedrige Schwierigkeit |
| Serie 1 | Tirol (läuft) | Hanni & Beate bereits in Produktion |

### Was noch in Rocket getestet werden sollte

| Priorität | Was | Warum |
|-----------|-----|-------|
| **Hoch** | Sächsische Schweiz | Ostdeutsche Lücke — evtl. wenig Konkurrenz wie Allgäu |
| **Hoch** | Berchtesgaden | Bayern wie Allgäu — könnte ähnlich performen |
| Mittel | Salzkammergut | Profitiert von „liebesroman österreich" |
| Niedrig | Pfälzerwald | Pfalz-Keywords zeigen nur 9–19 € — schwach |
| Niedrig | Vinschgau | Südtirol-Keywords bereits durch Tirol abgedeckt |
| **Hoch** | Kategorien-Check | Ghost-Categories & Bestseller-Schwelle |
| **Hoch** | Reverse ASIN Top-3 Eifel + Allgäu | Welche Keywords nutzen die Bestseller? |

---

## 8. Wichtigste Lektionen

| # | Erkenntnis | Konsequenz |
|---|-----------|------------|
| 1 | Alle regionalen Keywords haben <50 Suchen | Bücher werden über Kategorien + Also-Boughts entdeckt, nicht über Keyword-Suche |
| 2 | Schwierigkeit bei Regionen durchgehend grün | Einstieg ist leicht — es gibt keine Platzhirsche |
| 3 | Perplexity-Suchvolumina 200–300× übertrieben | Nie Perplexity für Amazon-Suchvolumina nutzen |
| 4 | eBook-Einkommen werden von Mega-Sellern verzerrt | Regionaldaten (150–300 €) sind realistischer als Genre-Daten (3.000+ €) |
| 5 | Leserinnen nutzen englische Genre-Tags | „small town romance deutsch" als KDP-Keyword einsetzen |
| 6 | „heimatroman" (zusammen) = Schwierigkeit 70 🔴 | „heimat roman" (getrennt) = 465 €, Schwierigkeit 38 🟢 |
| 7 | TB-Preise 12–16 € sind Standard | Unsere Preisstrategie (12,99 €) passt |
| 8 | Serien schlagen Einzeltitel | Mia Peters: 2 Bücher = 570 €/Mo zusammen |
| 9 | Zillertal allein zu eng (3–31 €) | Hanni-Beate als Tirol/Südtirol positionieren |
| 10 | Allgäu hat das beste Einkommen/Konkurrenz-Verhältnis | Nächste Serie sollte im Allgäu spielen |
| 11 | **Second Chance = stärkstes Trope** (1.929 Suchen, 956 €) | Muss in KDP-Keywords + Klappentext jedes Buches |
| 12 | Region + Trope = Killer-Kombination | Region für Ranking (wenig Konkurrenz), Trope für Traffic (viel Suchvolumen) |
| 13 | „zweite chance" allein = Schwierigkeit 91 🔴 | Immer mit Zusatz: „romanze deutsch", „liebesroman deutsch" |
| 14 | Slow Burn passt auch (309 €, 81 Suchen) | Als Sekundär-Trope im Klappentext erwähnen |
| 15 | Later-in-Life Romance auf Deutsch = quasi unbesetzt | Maja Sternberg hat keine echte Konkurrenz — First Mover Advantage |
| 16 | Dunbar (Silberfuchs) ist steamy, nicht clean | Unsere Nische (clean/slow burn/Heimat 40+) ist komplett frei |
| 17 | **„Ab 40" ist der echte Suchintent** für Later-in-Life | Leserinnen suchen „liebesroman ab 40", nicht englische Genre-Labels — Keywords entsprechend anpassen |
| 18 | **Sammelband-Keywords = verstecktes Gold** | „Liebesroman ab 40 sammelband" hat Diff. 23 🟢 bei 2.448 € Einkommen — ab 3 Büchern Sammelband publizieren |
| 19 | **Einkommens-Ausreißer immer kritisch prüfen** | Einzelne Bestseller verzerren den Rocket-Durchschnitt massiv (18.431 €, 7.202 €) — realistische Werte liegen bei 100–1.400 € |
| 20 | **Wenn kein Top-10-Buch in einer Nische funktioniert, ist das die beste Gelegenheit** | Die Nachfrage ist da (~1.600 Suchen/Mo für „ab 40"), aber das Angebot ist schlecht — falsche Preise, keine Serien, keine Keywords, keine Launch-Strategie |
| 21 | **Keywords + Launch + Serie + richtiger Preis müssen ZUSAMMEN stimmen** | Kirschbauminsel-Lektion: Perfekte Keywords allein bringen 0 € — ohne ARC-Team, Serienbindung und Preisoptimierung versickert auch das richtige Produkt |
