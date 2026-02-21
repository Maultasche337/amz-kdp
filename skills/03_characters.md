# SKILL: Charakterprofile erstellen

## Zweck
Erstellt vollständige Charakterprofile für alle Hauptfiguren und wichtigen Nebenfiguren, konsistent mit Briefing und Ending.

## Input
- `briefing.json` (Pflicht)
- `02_ending.md` (Pflicht)

## Output
- `03_characters.md` im Buchordner

---

## Referenz: Charakterprofil-Struktur (4 Ebenen)

Jedes Profil durchläuft 4 Tiefenebenen:

**Ebene 1 — Rolle**
Protagonist, Antagonist, Guide, Sidekick, Love Interest, Mentor, Foil

**Ebene 2 — Äußere Ebene (Superficial)**
- Grunddaten: Name, Alter, Beruf, Einkommenssituation
- Physisch: Größe, Figur, Haarfarbe/-länge, Augenfarbe, auffällige Merkmale (Narben, Tattoos)
- Kleidung & Stil: Was trägt sie typischerweise? Was verrät das über sie?

**Ebene 3 — Persönlichkeitsebene**
- Kommunikation: Körperhaltung, Gestik, Augenkontakt, typische Ausdrücke, Floskeln
- Psychologisches Profil: Intro/Extroversion, Definition von Glück, Werte, Liebessprache, Führungsstil
- Motivationen & Ängste: Was will sie (oberflächlich)? Was braucht sie (tief)? Größte Angst? Worauf ist sie stolz?

**Ebene 4 — Backstory-Ebene**
- Familie: Beziehung zu Eltern, Geschwistern, prägenden Bezugspersonen
- Lebensstil: Job-Geschichte, Hobbys, Fähigkeiten, Verhältnis zu Geld
- Geschichte: Kindheitserlebnis, ein Schlüsselereignis, Trauma, größtes Bedauern

**Widerspruchs-Matrix (für Konflikt):**
Wo kollidieren Wunsch vs. Bedarf? Werte vs. Verhalten? Das ist die Quelle des inneren Konflikts.

---

## Quick-Check: 25 kritische Charakterfragen

Für Protagonistin und Love Interest zwingend beantworten:

1. Was will sie am Anfang des Buches — und was braucht sie wirklich?
2. Was hält sie davon ab, zu bekommen was sie braucht?
3. Welches Kindheitserlebnis hat diesen Glaubenssatz geprägt?
4. Wie geht sie mit Konflikten um — kämpft sie, flieht sie, friert sie ein?
5. Was sagen andere Leute hinter ihrem Rücken über sie?
6. Was würde sie niemals tun — und tut sie dann genau das?
7. Welche 3 Gegenstände hat sie immer dabei und warum?
8. Wie klingt ihre innere Stimme wenn sie zweifelt?
9. Was bringt sie zum Lachen — unkontrolliert, ehrlich?
10. Was wäre ihre letzte SMS, bevor sie stirbt?
11. Welches Wort benutzt sie zu oft?
12. Wie sitzt sie? Wie geht sie? Wie betritt sie einen Raum?
13. Was lügt sie sich selbst an?
14. Wen liebt sie bedingungslos — und warum ausgerechnet den?
15. Was würde sie opfern für das, was sie wirklich will?
16. Welchen Geruch verbindet sie mit Sicherheit?
17. Wie reagiert sie wenn jemand zu ihr nett ist — misstraut sie?
18. Was hätte ihr Leben anders gemacht, wenn eine Entscheidung anders gefallen wäre?
19. Welche Schwäche hält sie für eine Stärke?
20. Was sieht sie im Spiegel — und was ist wirklich da?
21. Wie klingt ihre Stimme wenn sie aufgeregt ist? Wenn sie lügt?
22. Was ist ihr Schuldgefühl, das sie nie loswird?
23. Wie definiert sie Liebe — und hat sie je so geliebt oder geliebt wurde?
24. Was würde sie wütend machen, obwohl sie es eigentlich nicht sollte?
25. Wie endet ihr Entwicklungsbogen — was hat sie am Ende verstanden, was sie vorher nicht sehen konnte?

---

## Prompt-Template

```
Du bist eine erfahrene Romanautorin im deutschsprachigen Raum.

Hier ist das Buchbriefing:
[BRIEFING_JSON]

Hier ist das ausgearbeitete Story-Ending:
[ENDING]

Erstelle vollständige Charakterprofile für diesen Roman. Berücksichtige welche Figuren notwendig sind damit das Ending funktioniert.

Für JEDE Figur (Protagonistin, Liebesinteresse, 3-4 Nebenfiguren) — arbeite alle 4 Ebenen durch:

---

**[Name]**

EBENE 1 — ROLLE & FUNKTION:
- Rolle in der Story:
- Funktion für den Plot (was wäre anders ohne diese Figur?):

EBENE 2 — ÄUSSERES:
- Alter:
- Beruf / Lebenssituation:
- Physisch: Haar, Augen, Körperbau, auffällige Merkmale
- Typische Kleidung (was verrät das über sie?):

EBENE 3 — PERSÖNLICHKEIT:
- 3-5 Kernzüge:
- Kommunikation & Manierismen (typische Ausdrücke, Gestik, Körperhaltung):
- Liebessprache / Wie zeigt sie Zuneigung?:
- Innere Wunde / Glaubenssatz (was hält sie zurück?):
- Wunsch (oberflächlich) vs. Bedarf (tief):
- Größte Angst:
- Widerspruch (wo kollidieren Werte und Verhalten?):

EBENE 4 — BACKSTORY:
- Prägendes Kindheitserlebnis:
- Ein Schlüsselereignis (das sie zu wer sie heute ist gemacht hat):
- Beziehung zur Familie:
- Verhältnis zu Geld / Sicherheit:

ENTWICKLUNG:
- Wo startet diese Figur emotional?:
- Wo endet sie? Was hat sie verstanden?:
- Beziehung zur Protagonistin (wie verändert sie sich durch diese Beziehung?):

DIALOGSTIMME:
- Wie klingt diese Person? (Satzbau, Tempo, typische Formulierungen)
- Ein Beispielsatz, den nur diese Person sagen würde:

---

Spezielle Anforderung: Die Protagonistin hat folgende Eigenschaften aus dem Briefing: [PROTAGONIST_CHARACTERISTICS].
Stelle sicher dass diese authentisch und positiv dargestellt werden, nicht als Makel.

Antworte komplett auf Deutsch. Formatiere als übersichtliches Referenzdokument das beim Schreiben aller 20 Kapitel als Konsistenz-Anker dient.
```
