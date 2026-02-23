---
name: novel-website-update
description: Aktualisiert eine bestehende Astro-Autorinnen-Website wenn ein neues Buch fertig ist — fügt die neue Bonus-Szene als Unterseite hinzu und aktualisiert den Shop mit dem neuen Buch. Wird ausgelöst bei "Website updaten für Buch [N]", "Neues Buch zur Website hinzufügen", oder automatisch nach novel-bonus-scene bei Buch 2+.
metadata: { "openclaw": { "requires": { "env": ["ANTHROPIC_API_KEY"], "bins": ["node"] } } }
---

# Novel Website Update — Neues Buch zur bestehenden Site hinzufügen

## Wann dieser Skill aktiv wird
- "Website updaten für [Pseudonym] Buch [N]"
- "Neues Buch zur Website hinzufügen"
- "[book_id] zur Site"
- Automatisch nach `novel-bonus-scene` wenn Buch 2 oder höher

## Voraussetzungen prüfen

1. Prüfe ob `~/openclaw-websites/[pseudonym-slug]/` existiert — wenn nicht, stoppe und weise auf `novel-website-setup` hin
2. Lies `~/openclaw-novels/[book_id]/` für alle Buchdaten
3. Prüfe ob `~/openclaw-novels/[book_id]/bonus_scene.md` existiert
4. Prüfe ob Cover-Dateien vorhanden sind

## Was bei jedem neuen Buch zu tun ist

### Schritt 1: books.ts aktualisieren

Öffne `~/openclaw-websites/[pseudonym-slug]/src/data/books.ts` und füge den neuen Eintrag hinzu:

```typescript
{
  slug: "[buch-slug]",           // z.B. "alpenrose"
  title: "[Buchtitel]",
  series: "[Serienname]",
  number: [Bandnummer],
  description: "[Klappentext-Kurzfassung, 2-3 Sätze]",
  cover: "/covers/[dateiname].jpg",
  amazonLink: null,              // PLATZHALTER bis Buch live ist
  kindleUnlimited: true,
  published: false               // auf true setzen wenn live
}
```

### Schritt 2: Neue Bonus-Szenen-Seite erstellen

Erstelle `~/openclaw-websites/[pseudonym-slug]/src/pages/bonus/[buch-slug].astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import { books } from '../../data/books';

const book = books.find(b => b.slug === '[buch-slug]');
---

<BaseLayout title={`Bonus-Szene: ${book.title}`}>
  <article class="bonus-scene">
    <header>
      <p class="series-label">{book.series} · Band {book.number}</p>
      <h1>[Titel der Bonus-Szene]</h1>
      <p class="intro">
        [Einleitungstext aus bonus_scene.md — die kursive Einleitung]
      </p>
    </header>
    
    <div class="scene-content">
      [Vollständiger Szenentext aus bonus_scene.md]
    </div>
    
    <footer class="scene-footer">
      <p>[Dankes-Zeile aus bonus_scene.md]</p>
      <div class="links">
        <a href="/bonus">← Alle Bonus-Szenen</a>
        {book.amazonLink && (
          <a href={book.amazonLink} class="btn-primary">
            {book.title} auf Amazon lesen →
          </a>
        )}
      </div>
    </footer>
  </article>
</BaseLayout>
```

### Schritt 3: Bonus-Übersichtsseite aktualisieren

Öffne `~/openclaw-websites/[pseudonym-slug]/src/pages/bonus/index.astro` und füge die neue Szenen-Karte ein:

```astro
<div class="bonus-card">
  <span class="book-label">[Serienname] · Band [N]</span>
  <h2><a href="/bonus/[buch-slug]">[Titel der Bonus-Szene]</a></h2>
  <p>[Teaser-Satz, 1 Zeile — macht neugierig ohne zu spoilern]</p>
  <a href="/bonus/[buch-slug]">Szene lesen →</a>
</div>
```

### Schritt 4: Vorherige Bücher-Status prüfen

Wenn das vorherige Buch inzwischen auf Amazon live ist:
- `amazonLink` in books.ts auf echten Link setzen
- `published: true` setzen
- Via Discord nachfragen: "🔗 Hat [Buch N-1] bereits einen Amazon-Link? Falls ja, bitte mitteilen damit ich ihn eintrage."

### Schritt 5: Homepage aktualisieren (optional)

Falls Homepage einen "Neuestes Buch"-Block hat:
- Neues Buch als Featured-Buch setzen
- Altes Buch in die reguläre Bücherliste verschieben

---

## Was NICHT geändert wird

- Impressum und Datenschutz bleiben unverändert
- Navigation bleibt gleich
- Bestehende Bonus-Szenen-Seiten bleiben unverändert
- Tailwind-Konfiguration bleibt gleich

---

## Workflow

1. Alle Buchdaten aus `~/openclaw-novels/[book_id]/` lesen
2. `books.ts` um neuen Eintrag erweitern
3. Neue Bonus-Szene Astro-Seite erstellen (Inhalt aus `bonus_scene.md`)
4. Bonus-Übersicht um neue Karte erweitern
5. Homepage prüfen ob Update sinnvoll
6. Via Discord melden:
   > "🔄 Website für **[Pseudonym]** aktualisiert!
   > ✅ Neue Seite: `/bonus/[buch-slug]` — [Titel der Bonus-Szene]
   > ✅ Shop: [Buchtitel] als 'Erscheint bald' hinzugefügt
   > 
   > Nächste Schritte:
   > 1. Cover-Datei ablegen: `public/covers/[dateiname].jpg`
   > 2. Nach Amazon-Launch: amazonLink in `src/data/books.ts` eintragen
   > 3. Git commit + push → Netlify deployed automatisch"

---

## Erinnerung: Amazon-Link eintragen

Wenn User meldet "Buch [N] ist jetzt auf Amazon live":
1. books.ts öffnen
2. `amazonLink: null` → `amazonLink: "[echter Amazon-Link]"` ersetzen
3. `published: false` → `published: true`
4. Git-Datei ausgeben mit dem Change
5. Melden: "✅ Amazon-Link eingetragen — nach dem nächsten Deploy ist der Button live"
