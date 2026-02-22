# Publisher Rocket Recherche — Serien-Settings für Maja Sternberg

## Ziel
Verifiziere die Perplexity-Daten mit echten amazon.de-Suchvolumen aus Publisher Rocket.
Die Ergebnisse entscheiden, welche Regionen wir als nächste Serien produzieren.

---

## Anleitung

### Schritt 1: Marketplace einstellen
- Publisher Rocket öffnen
- Oben rechts: **Marketplace → amazon.de** auswählen

### Schritt 2: Keyword Search — Regionen testen
Gib folgende Keywords **einzeln** in die Keyword Search ein.
Exportiere jede Suche als CSV (Export-Button rechts oben) und speichere sie in diesen Ordner.

**Dateinamen-Konvention:**
```
01_eifel.csv
02_allgaeu.csv
03_saechsische_schweiz.csv
04_berchtesgaden.csv
05_pfaelzerwald.csv
06_vinschgau.csv
07_salzkammergut.csv
08_kontrolle_zillertal.csv  ← zum Vergleich mit bekannter Serie
```

**Keywords pro Region:**

#### 01 — Eifel
```
Eifel Heimatroman
Eifel Liebesroman
Liebesroman Eifel
Heimatroman Vulkaneifel
Eifel Roman Frauen
```

#### 02 — Allgäu
```
Allgäu Roman
Allgäu Liebesroman
Allgäu Liebesgeschichte
Heimatroman Allgäu Alm
Allgäu Roman Frauen
```

#### 03 — Sächsische Schweiz
```
Sächsische Schweiz Roman
Elbsandstein Liebesroman
Heimatroman Sachsen
Sachsen Liebesgeschichte
Elbe Roman
```

#### 04 — Berchtesgadener Land
```
Berchtesgaden Liebesroman
Berchtesgaden Roman
Heimatroman Berchtesgaden
Watzmann Roman
Bayern Berge Liebesroman
```

#### 05 — Pfälzer Wald
```
Pfalz Liebesroman
Pfälzer Wald Roman
Weinroman Pfalz
Heimatroman Pfalz
Pfalz Roman Frauen
```

#### 06 — Vinschgau / Südtirol
```
Südtirol Liebesroman
Vinschgau Roman
Südtirol Heimatroman
Meran Liebesgeschichte
Südtirol Roman Frauen
```

#### 07 — Salzkammergut
```
Salzkammergut Roman
Salzkammergut Liebesroman
Hallstatt Roman
Heimatroman Österreich See
Salzkammergut Liebesgeschichte
```

#### 08 — Kontrolle: Zillertal (zum Vergleich)
```
Zillertal Liebesroman
Tirol Heimatroman
Liebesroman Tirol
Zillertal Roman
Tirol Roman Frauen
```

### Schritt 3: Category Search
Prüfe diese Kategorien auf Ghost-Status und Bestseller-Schwelle:

```
Belletristik → Liebesromane → Zeitgenössische Liebesromane
Belletristik → Heimat- & Brauchtumsromane
Belletristik → Frauenromane
Belletristik → Familienleben
Liebesromane → Romantische Komödie
Liebesromane → Romantische Weihnachtsromane
```

Notiere pro Kategorie:
- [ ] Ghost Category? (ja/nein)
- [ ] Duplicate? (ja/nein — wenn ja, mit welcher?)
- [ ] Sales needed for #1 Bestseller: ___

Speichere als: `kategorien_check.csv` oder Screenshot.

### Schritt 4: Reverse ASIN (optional, aber wertvoll)
Geh auf amazon.de und suche nach:
```
Heimatroman Liebesroman Eifel
Heimatroman Liebesroman Allgäu
```
Öffne die **Top 3 Bücher** pro Suche, kopiere die ASIN und gib sie in Rocket's Reverse ASIN ein.
Exportiere als CSV: `reverse_asin_eifel.csv`, `reverse_asin_allgaeu.csv` etc.

---

## Auswertung

Wenn alle CSVs in diesem Ordner liegen, sage Claude:

> **„Bitte werte die Publisher Rocket CSVs in research/publisher_rocket/ aus und erstelle ein Ranking der besten Serien-Settings."**

Claude wird dann:
1. Alle CSVs einlesen
2. Perplexity-Daten mit echten Rocket-Daten vergleichen
3. Ein finales Ranking erstellen
4. Briefings für die Top-3-Serien generieren

---

## Erwartete Dateien in diesem Ordner

```
research/publisher_rocket/
├── README.md                    ← diese Datei
├── 01_eifel.csv
├── 02_allgaeu.csv
├── 03_saechsische_schweiz.csv
├── 04_berchtesgaden.csv
├── 05_pfaelzerwald.csv
├── 06_vinschgau.csv
├── 07_salzkammergut.csv
├── 08_kontrolle_zillertal.csv
├── kategorien_check.csv
├── reverse_asin_eifel.csv       (optional)
└── reverse_asin_allgaeu.csv     (optional)
```
