---
name: novel-website-setup
description: Erstellt eine vollständige Astro-Autorinnen-Website für ein Pseudonym — inklusive Homepage, Shop (Buchübersicht), Bonus-Szenen-Seite, Impressum und Datenschutzerklärung. Wird ausgelöst bei "Website erstellen für [Pseudonym]", "Astro Site aufsetzen", "Autorinnen-Website Lena/Monika" oder automatisch nach Fertigstellung von Buch 1 eines neuen Pseudonyms.
metadata: { "openclaw": { "requires": { "env": ["ANTHROPIC_API_KEY"], "bins": ["node", "npm"] } } }
---

# Novel Website Setup — Vollständige Astro-Autorinnen-Site

## Wann dieser Skill aktiv wird
- "Website erstellen für [Pseudonym]"
- "Astro Site aufsetzen"
- "Autorinnen-Website Maja / Monika"
- Automatisch nach Buch 1 eines neuen Pseudonyms

## Voraussetzungen prüfen

Bevor du anfängst:
1. Lies `~/pseudonyme/[pseudonym]/PSEUDONYM.md` für Farben, Stil, Serien-Info
2. Prüfe ob `~/openclaw-novels/[book_id]/bonus_scene.md` existiert (von novel-bonus-scene)
3. Prüfe ob Cover-Bilder unter `~/openclaw-novels/[book_id]/covers/` vorhanden sind
4. Frage User nach Domain-Name falls nicht in PSEUDONYM.md hinterlegt

## Technische Basis

```bash
npm create astro@latest ~/openclaw-websites/[pseudonym-slug] -- --template minimal --typescript strict --no-install
cd ~/openclaw-websites/[pseudonym-slug]
npm install
npm install @astrojs/tailwind tailwindcss
```

Tailwind konfigurieren mit Pseudonym-Farben aus PSEUDONYM.md.

## Site-Struktur

```
src/
  pages/
    index.astro          → Homepage
    shop.astro           → Alle Bücher + Amazon-Links
    bonus/
      index.astro        → Übersicht aller Bonus-Szenen
      [buch-slug].astro  → Erste Bonus-Szene (aus novel-bonus-scene)
    impressum.astro      → Impressum (DE-Pflicht)
    datenschutz.astro    → Datenschutzerklärung (DSGVO)
  layouts/
    BaseLayout.astro     → Navigation + Footer
  components/
    BookCard.astro       → Wiederverwendbare Buch-Karte für Shop
    Nav.astro            → Navigation
```

## Navigation (immer sichtbar)

```
[Pseudonym-Name] | Bücher | Bonus-Szenen | [optional: Über mich]
```

Kein Newsletter-Link direkt in der Nav — Newsletter-Hinweis erscheint nur auf der Bonus-Szenen-Seite.

---

## Seiten im Detail

### 1. Homepage (index.astro)

Aufbau:
- **Hero-Bereich:** Pseudonym-Name, kurzer Tagline-Satz (aus PSEUDONYM.md), Cover von Buch 1 prominent
- **Über die Serie:** 2-3 Sätze Serien-Beschreibung
- **Bücher-Preview:** Die ersten 1-3 Bücher als Karten mit Titel, Cover-Bild, Kurzbeschreibung, Button "Auf Amazon lesen →"
- **Bonus-Szenen-Teaser:** Kleiner Abschnitt "Exklusive Szenen die nicht ins Buch passten" → Link zur Bonus-Seite
- **Footer:** Impressum | Datenschutz | © [Jahr] [Pseudonym]

Tonalität der Texte: Warm, persönlich, als würde das Pseudonym selbst schreiben.

### 2. Shop (shop.astro)

Eine Übersicht ALLER Bücher des Pseudonyms. Jedes Buch als `<BookCard>` Komponente:

```astro
<!-- BookCard.astro -->
<div class="book-card">
  <img src={cover} alt={title} />
  <h2>{title}</h2>
  <p class="series">{series} · Band {number}</p>
  <p class="description">{description}</p>
  <div class="badges">
    {kindleUnlimited && <span>📖 In Kindle Unlimited</span>}
    <span>📱 E-Book</span>
  </div>
  <a href={amazonLink || "#"} class="btn-primary">
    {amazonLink ? "Jetzt auf Amazon lesen →" : "Erscheint bald"}
  </a>
</div>
```

Für Bücher die noch nicht veröffentlicht sind: `amazonLink = null` → Button zeigt "Erscheint bald" (kein toter Link).

Wichtig: `amazonLink` als Variable in einer zentralen Datei `src/data/books.ts` — so muss man bei jedem neuen Buch nur diese eine Datei updaten.

**books.ts Struktur:**
```typescript
export const books = [
  {
    slug: "vergissmeinnicht",
    title: "Vergissmeinnicht",
    series: "Die Bergwald-Apotheke",
    number: 1,
    description: "Maria erbt eine Kräuterapotheke...",
    cover: "/covers/vergissmeinnicht.jpg",
    amazonLink: null, // PLATZHALTER — hier später den echten Link eintragen
    kindleUnlimited: true,
    published: false
  }
]
```

### 3. Bonus-Szenen-Übersicht (bonus/index.astro)

- Kurze Erklärung was Bonus-Szenen sind ("Szenen die es nicht ins Buch geschafft haben, exklusiv für euch hier")
- Liste aller verfügbaren Bonus-Szenen als Karten (Titel, zugehöriges Buch, kurze Teaser-Zeile)
- **Newsletter-Block am Ende der Seite** (NICHT im Header):
  ```
  Ihr wollt benachrichtigt werden wenn neue Szenen erscheinen?
  → Tragt euch in meinen Newsletter ein: [Brevo-Link]
  ```
  So ist der Mehrwert (die Szene selbst) OHNE E-Mail zugänglich — Amazon-konform.

### 4. Bonus-Szene Einzelseite ([buch-slug].astro)

- Titel der Szene
- Kurze Einleitung ("Diese Szene stammt aus [Buch]...")
- Vollständiger Szenentext (aus `bonus_scene.md`)
- Am Ende: Link zurück zur Übersicht + Link zum Buch auf Amazon
- **Kein** Pflicht-Login, kein E-Mail-Gate — Szene ist frei lesbar

### 5. Impressum (impressum.astro)

Deutsches Impressum nach § 5 TMG. Generiere ein Template mit Platzhaltern:

```
Impressum

Angaben gemäß § 5 TMG:

[VORNAME NACHNAME] ← PLATZHALTER: echter Name der Autorin
[STRAßE HAUSNUMMER]
[PLZ ORT]

Kontakt:
E-Mail: [EMAIL] ← z.B. kontakt@lena-bergmann.de

Hinweis: Dies ist eine fiktive Autorinnen-Website unter einem Pseudonym.
Die verantwortliche Person ist unter obiger Adresse erreichbar.

Haftungsausschluss: [Standard-Haftungstext]
```

Wichtiger Hinweis im Discord: "⚠️ Impressum enthält Platzhalter — bitte echte Kontaktdaten vor dem Launch eintragen!"

### 6. Datenschutzerklärung (datenschutz.astro)

DSGVO-konforme Datenschutzerklärung. Inhalte:

- Verantwortliche Person (Platzhalter)
- Hosting: "Die Website wird auf einem privaten Server betrieben. Es werden keine Daten an Cloud-Drittanbieter übermittelt." (kein Netlify/Vercel nötig)
- Keine Cookies außer technisch notwendige
- Keine Tracking-Tools
- Brevo-Newsletter: Eigener Abschnitt wenn Newsletter-Anmeldung auf der Site ist
  - Datenverarbeitung durch Brevo SAS, Frankreich
  - Opt-in Verfahren
  - Abmeldemöglichkeit in jeder Mail
- Kontaktformular: Nur wenn vorhanden
- Rechte der Nutzer (Auskunft, Löschung etc.)
- Datum der letzten Aktualisierung

Auch hier: Platzhalter-Hinweis via Discord.

---

## Astro Config (astro.config.mjs)

```javascript
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  site: 'https://[domain].de', // Platzhalter
});
```

## Tailwind — Pseudonym-Farben

### Maja Sternberg
```javascript
colors: {
  primary: '#6B7280',    // Schiefergrau
  secondary: '#4A7856',  // Waldgrün
  accent: '#B8860B',     // Bernstein-Gold (Lärchen)
  background: '#FAF7F2', // Cremeweiß
  text: '#2C2C2C'
}
```

### Monika Huber
```javascript
colors: {
  primary: '#1B4F9B',   // Bayerisches Blau
  secondary: '#C41E3A', // Bayerisches Rot
  accent: '#F5C842',    // Bayerisches Gelb
  background: '#FAFAFA',
  text: '#1A1A1A'
}
```

---

## Deploy-Hinweise (DEPLOY.md generieren)

Erstelle eine `DEPLOY.md` mit:

```markdown
# Deployment — Homeserver

Astro baut zu reinen statischen Dateien. Kein Node.js auf dem Server nötig —
nur ein Webserver der statische Dateien ausliefert (Nginx oder Apache).

## Build lokal ausführen

```bash
cd ~/openclaw-websites/[pseudonym-slug]
npm install
npm run build
# Ergebnis liegt in: dist/
```

## Deploy-Script (einmalig einrichten)

Erstelle `deploy.sh` im Projektordner:

```bash
#!/bin/bash
# Anpassen: Pfad auf dem Homeserver wo die Site liegen soll
REMOTE_USER="[dein-user]"
REMOTE_HOST="[homeserver-ip-oder-domain]"
REMOTE_PATH="/var/www/[pseudonym-slug]"

npm run build
rsync -avz --delete dist/ $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH
echo "✅ Deploy fertig"
```

Ausführbar machen: `chmod +x deploy.sh`
Danach jedes Mal nur noch: `./deploy.sh`

## Nginx-Konfiguration (auf dem Homeserver)

```nginx
server {
    listen 80;
    server_name [deine-domain].de www.[deine-domain].de;
    root /var/www/[pseudonym-slug];
    index index.html;

    location / {
        try_files $uri $uri/ $uri.html =404;
    }
}
```

Für HTTPS (empfohlen): Let's Encrypt mit Certbot
```bash
sudo certbot --nginx -d [deine-domain].de
```

## Vor dem Launch Checkliste:
- [ ] Impressum: echte Kontaktdaten eintragen
- [ ] Datenschutz: "Hosting: Eigener Server" eintragen (kein Cloud-Anbieter)
- [ ] Amazon-Links in src/data/books.ts eintragen sobald Buch live
- [ ] Cover-Bilder unter public/covers/ ablegen
- [ ] Domain auf Homeserver-IP zeigen (DNS A-Record)
- [ ] HTTPS einrichten (Certbot)
- [ ] deploy.sh mit korrekten Serverdaten befüllen
```

---

## Workflow

1. PSEUDONYM.md lesen
2. Astro-Projekt aufsetzen
3. Alle Seiten generieren (Homepage, Shop mit books.ts, Bonus-Index, erste Bonus-Szene, Impressum, Datenschutz)
4. BaseLayout mit Navigation erstellen
5. DEPLOY.md erstellen
6. Alles speichern unter `~/openclaw-websites/[pseudonym-slug]/`
7. Via Discord melden:
   > "🌐 Website für **[Pseudonym]** fertig!
   > 📁 Dateien: `~/openclaw-websites/[pseudonym-slug]/`
   > ⚠️ Vor Launch: Impressum + Datenschutz mit echten Daten füllen
   > ⚠️ Amazon-Links in `src/data/books.ts` eintragen sobald verfügbar
   > 📖 Deploy-Anleitung: `DEPLOY.md`"
