# Prompt Engineering: Wie man Prompts richtig entwickelt, analysiert und effizient anwendet

Prompt Engineering ist die Kunst, KI-Modelle wie GPT so zu füttern, dass sie *genau* das liefern, was man braucht - egal ob Text, Code oder Struktur.
In dieser Vorlesung geht es um die Entwicklung, Analyse und Anwendung von Prompts. 

---

## Was ist Prompt Engineering?

Prompt Engineering ist:
- Die Gestaltung von Eingaben (Prompts), um optimale Ergebnisse aus Sprachmodellen zu erzielen.
- Eine Mischung aus **Technik**, **Kreativität** und **Systematik**.
- Die neue Sprache für den Umgang mit KI - präzise, klar und zielgericht.

---

## Grundlagen: Syntax eines guten Prompts

```text
[Rolle] + [Kontext] + [Aufgabe] + [Format]
```

### Beispiel 

```text
Du bist ein Python-Experte. Schreibe eine Funktion in Python, die prüft, ob eine Zahl eine Primzahl ist. Gib kommentierten Code zurück.
```

Hier ist alles drin:
- Rolle: Du bist ein Python-Experte
- Kontext: Primzahlprüfung
- Aufgabe: Schreibe eine Funktion in Python
- Format: Python-Code, Kommentiert

## Typen von Prompts 
- Instruction Prompt: eine klare Anweisung, was sie tun soll
- Zero-Shot-Prompting: gibts der KI eine Aufgabe ohne jeglicher Beispiel
- Few-shot Prompting: gibts der KI ein oder mehrere Besipiele mit
- Chain-of-Thought (Gedankenkette): Schritt für Schritt zu denken 
- Tree-of-Thought (Gedankenbaum): mehrere Denkpfade gelichzeitig zu entwicklen
- Self-Consistency-Prompting: Mehre Denkwede zu gehen 
- Reflexion-Prompting: ihre eigene Antwort zu prüfen
- Reverse Prompting: welcher Prompt zu einer gegebenen Antwort geführt hat
- Plan like a Graph: Aufgaben wie in einem Graphen zu planen
- Negativer Prompt: was soll die KI tun und was soll sie nicht tun 
- Role Prompting: Die KI schlüpft in eine definierte Rolle

## Prompt Design: Best Practices 
- Sei konkret: "Erkläre Quantenphyisk für ein Kind" > "Erkläre Quantenphyisk"
- Vermeide Mehrdeutigkeit: Präzisiere Format, Länge, Zielgruppe
- Nutze Beispiele: "Gib Beispiele für..."
- Teste iterativ: Prompt > Output > Anpassen > Wiederholen
- Nutze Formatierung: Markdown, Codeblöcke, Listen - für mehr Klarheit

## Prompt Engineering in Coding-Kontext

### Prompt:
```text
Schreibe eine Python-Funktion, die prüft, ob ein String ein Palindrom ist. Verwende keine eingebaute Funktionen außer lower().
```

### Output:
```python
def is_palindrome:
    s = s.lower()
    return s == s[::-1]
```

## Analyse von Prompts

### Checkliste:
- Ist die Aufgabe eindeutig formuliert?
- Fehlt Kontext?
- Zu viel auf einmal verlangt?
- Stimmt der Stil?

## Prompt-Optimierung

### Schlechter Prompt

```text
Mach was mit dem Text.
```

### Verbesserter Prompt

```text
Fasse den folgenden Artikel in 3 Sätzen zusammen. Zielgruppe: Schüler der 5. Klasse. Verwende einfache Sprache.
```

## Effizienz: Gute Prompts sparen Ressourcen
- Schneller zum Ziel = weniger Tokens = günstiger
- Mehr Konsistenz = weniger manuelle Nacharbeit
- Bessere Reproduzierbarkeit = skalierbare Automatisierung

## Prompt-Beispiele aus der Praxis

### Codegenerierung 

```text
Du bist ein Java-Experte. Erstelle eine Funktion, die pürft, ob eine Zahl durch 3 oder 5 teilbar ist.
```

### Übersetzung + Stiländerung

```text
Übersetzte folgenden Satz ins Englische und verwende einen formellen Business-Ton.
```

### Datenextraktion 

```text
Extrahiere alle Namen und E-Mail-Adressen aus dem folgenden Text und gib sie als JSON-Datei zurück.
```

## Übung 1: Prompt Debugging
Analysiere diesen Prompt und verbessere ihn:

```text
Erklär mir Mathe.
```

### Lösungsbeispiel
```text
Erklär das Konzept der linearen Funktionen für Schüler der 10. Klasse anhand eines praktischen Beispiels aus dem Alltag. Verwende einfache Sprache und eine Schritt-für-Schritt-Erklärung.
```

## Übung 2: Prompt bauen
Entwickle einen Prompt für GPT, der einen HTML-Code für eine einfache Portfolio-Seite erstellt - inklusive Header, Projketliste und Footer.

// ??

## Fazit 
- Mach's der KI leicht
- Schreibe Prompt wie Anleitungen für Praktikanten
- Bewerte Output immer kritisch: KI != Wahrheit 

---

// Quellen 
- https://www.coursera.org/de-DE/articles/what-is-prompt-engineering
- https://de.wikipedia.org/wiki/Prompt_Engineering
