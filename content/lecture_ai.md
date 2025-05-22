# Prompt Engineering: Wie man Prompts richtig entwickelt, analysiert und effizient anwendet

Prompt Engineering ist die Kunst, KI-Modelle wie GPT gezielt zu steuern, sodass sie präzise und effiziente Ergebnisse liefern. In dieser Vorlesung werden wir uns mit der Entwicklung, Analyse und Anwendung von Prompts beschäftigen, um sicherzustellen, dass Sie das Beste aus KI herausholen können.

---

## Was ist Prompt Engineering?

Prompt Engineering umfasst:
- Die gezielte Gestaltung von Eingaben (Prompts), um aus Sprachmodellen wie GPT optimale Ergebnisse zu erzielen.
- Eine Mischung aus **Technik**, **Kreativität** und **Systematik**.
- Eine neue Sprache im Umgang mit KI: präzise, klar und zielgerichtet.

---

## Grundlagen: Bestandteile eines Prompts

Ein erfolgreicher Prompt besteht aus vier wesentlichen Bestandteilen:

```text
EN: [Goal] + [Return Format] + [Warnings] + [Context Dump]

DE: [Zielsetzung] + [Rückgabeformat] + [Warnhinweise] + [Details und Kontext]
```

### 1. Goal - Zielsetzung:
Das Ziel des Prompts muss klar und spezifisch formuliert werden.
- **Warum?** Eine vage Zielsetzung führt oft zu ungenauen oder irrelevanten Antworten.
- Beginnen Sie mit klaren Phrasen wie „Ich benötige...“ oder „Ich möchte...“.
- Halten Sie es kurz und prägnant, aber vollständig.

#### Beispiel:
```text
"Ich benötige eine Liste von versteckten Biergärten im Zentrum Münchens, die Weißwurstfrühstück servieren." 
```
Dies ist klar und gibt der KI genau die Richtung vor.

### 2. Return Format - Rückgabeformat:
Hier geben Sie an, wie die Antwort strukturiert sein soll.
- **Warum?** Ein klares Format sorgt für eine einfachere Weiterverarbeitung und reduziert Nachbearbeitung.
- Beginnen Sie mit: „Bitte gib für jeden Eintrag an...“ und listen Sie alle benötigten Informationen auf.
- Berücksichtigen Sie Formatierungswünsche (z.B. Listen, Tabellen, Codeblöcke).

#### Beispiel:
```text
"Bitte gib für jeden Biergarten den offiziellen Namen, die vollständige Adresse, die Buchungsdetails, den Preis des Frühstücks und den Bierpreis an."
```
  
### 3. Warnings - Warnhinweise und Anforderungen:
Manchmal gibt es spezifische Anforderungen oder Einschränkungen, die beachtet werden müssen.
- **Warum?** Warnhinweise helfen, Missverständnisse und Fehler zu vermeiden.
- Benennen Sie alle entscheidenden Punkte und Fallstricke.

#### Beispiel:
```text
"„Stelle sicher, dass jedes Restaurant aktuell geöffnet ist und Reservierungen akzeptiert.“
```

### 4. Context Dump - Details und Kontext:
Zusätzliche Informationen, die dem Modell helfen, besser zu verstehen, was Sie suchen.
- **Warum?** Kontext hilft, die Antwort noch genauer auf Ihre Bedürfnisse abzustimmen.
- Erwähne Einschränkungen z.B. "barrierefrei" "für Vegetarier geeignet"
- Geben Sie Hintergrundinformationen oder Erfahrungen an.

```text
Beispiel: "Ich habe die meisten großen Biergärten in München besucht und bevorzuge weniger touristische Einrichtungen."
```

## Typen von Prompts 
- **Instruction Prompt**: Ein klarer Auftrag, der dem Modell sagt, was zu tun ist.
- **Zero-Shot-Prompting**:  Die KI erhält eine Aufgabe ohne jegliche Beispiele.
- **Few-Shot-Prompting**: Die KI bekommt Beispiele, um die Aufgabe besser zu verstehen.
- **Chain-of-Thought** (Gedankenkette): Das Modell geht schrittweise vor, um ein tieferes Verständnis zu entwickeln.
- **Tree-of-Thought** (Gedankenbaum): Es werden mehrere Denkpfade gleichzeitig verfolgt, um verschiedene Lösungsmöglichkeiten zu erkunden.
- **Self-Consistency-Prompting**: Verschiedene Varianten eines Prompts werden getestet, um die konsistenteste Antwort zu finden.
- **Reflexion-Prompting**:  Die KI wird aufgefordert, ihre Antwort zu reflektieren.
- **Reverse Prompting**: Untersuchung, welcher Prompt zu einer gegebenen Antwort geführt hat.
- **Plan like a Graph**: Aufgaben werden in Form eines Entscheidungsgraphen strukturiert.
- **Negativer Prompt**: Es wird explizit angegeben, was die KI nicht tun soll.
- **Role Prompting**: Die KI übernimmt eine definierte Rolle, um aus einer bestimmten Perspektive zu antworten.

## Best Practices für das Design von Prompts
- **Sei konkret**: „Erkläre Quantenphysik für ein Kind“ ist viel präziser als „Erkläre Quantenphysik“.
- **Vermeide Mehrdeutigkeit**: Sei klar bei Format, Zielgruppe und Umfang.
- **Nutze Beispiele**: „Gib Beispiele für...“ hilft der KI, die Aufgabe besser zu verstehen.
- **Teste iterativ**: Teste den Prompt, schaue dir das Ergebnis an und passe es an, wenn nötig.
- **Nutze Formatierung**: Verwende Markdown, Codeblöcke und Listen für bessere Klarheit und Struktur.

## Prompt Engineering im Coding-Kontext

### Beispiel: Codegenerierung
#### Prompt:
```text
Schreibe eine Python-Funktion, die prüft, ob ein String ein Palindrom ist. Verwende keine eingebaute Funktionen außer lower().
```

#### Output:
```python
def is_palindrome:
    s = s.lower()
    return s == s[::-1]
```

- Der Prompt ist spezifisch genug, um die Aufgabe klarzustellen, und enthält eine Einschränkung (keine eingebauten Funktionen außer lower()).
- Das Ergebnis ist direkt und entspricht der Anforderung.

## Analyse von Prompts

### Checkliste:
- Ist die Aufgabe eindeutig formuliert?
- Fehlt Kontext oder Hintergrundinformation?
- Wird zu viel auf einmal verlangt?
- Stimmt der Stil mit der Zielgruppe überein?

## Optimierung von Prompts

### Schlechter Prompt

```text
Mach was mit dem Text.
```

### Verbesserter Prompt

```text
Fasse den folgenden Artikel in 3 Sätzen zusammen. Zielgruppe: Schüler der 5. Klasse. Verwende einfache Sprache.
```

### Warum verbessern?
Der verbesserte Prompt ist präziser und gibt klare Anweisungen hinsichtlich Umfang, Zielgruppe und Ton.

## Effizienz: Gute Prompts sparen Ressourcen
- **Schneller zum Ziel**: Weniger Tokens führen zu schnelleren und kostengünstigeren Ergebnissen.
- **Mehr Konsistenz**: Bessere Prompts resultieren in weniger Nacharbeit und einer konsistenteren Qualität.
- **Bessere Reproduzierbarkeit**: Gut formulierte Prompts machen Prozesse skalierbar und wiederholbar.

## Prompt-Beispiele aus der Praxis

### 1. Codegenerierung 

```text
Du bist ein Java-Experte. Erstelle eine Funktion, die pürft, ob eine Zahl durch 3 oder 5 teilbar ist.
```

### 2. Übersetzung + Stiländerung

```text
Übersetzte folgenden Satz ins Englische und verwende einen formellen Business-Ton.
```

### 3. Datenextraktion 

```text
Extrahiere alle Namen und E-Mail-Adressen aus dem folgenden Text und gib sie als JSON-Datei zurück.
```

## Übung 1: Prompt Debugging
**Ziel**: Identifizieren Sie Schwächen in einem Prompt und verbessern Sie diesen, um präzise und qualitativ hochwertige Ergebnisse zu erhalten.

### Original-Prompt:
```text
Erzähl mir was über die Geschichte von Berlin.
```

### Aufgabe:
- Überlegen Sie, warum dieser Prompt zu ungenauen oder weit gefassten Ergebnissen führen könnte.
- Welche zusätzlichen Informationen fehlen?
- Wie können Sie den Prompt präziser machen?

### Lösung

$Lösung: ^Dies ist ein Beispiel

**Verbesserter Prompt**:
```text
Erzähle mir in 3 Absätzen über die Geschichte Berlins. Beginne mit der Gründung der Stadt, gehe dann auf die Zeit des Kalten Krieges und die Wiedervereinigung ein. Halte den Text einfach, sodass er für Schüler der 10. Klasse verständlich ist.
```

### Erklärung:
- Der ursprüngliche Prompt ist zu vage und kann zu einer umfassenden Antwort führen, die nicht fokussiert oder leicht verständlich ist.
- Der verbesserte Prompt gibt klare Anweisungen zur Struktur und Zielgruppe der Antwort und stellt sicher, dass nur relevante Informationen enthalten sind.

## Übung 2: Erstellung eines Code-Prompts
**Ziel**: Formulieren Sie einen präzisen Prompt, der den Code für eine spezifische Aufgabe generiert.

### Aufgabe:
- Schreiben Sie einen Prompt, der eine Python-Funktion erstellt, die prüft, ob eine Zahl eine Primzahl ist, ohne eingebaute Funktionen wie isprime() zu verwenden.

### Lösung

$Lösung: ^Dies ist ein Beispiel

**Prompt**:
```text
Schreibe eine Python-Funktion, die prüft, ob eine Zahl eine Primzahl ist. Die Funktion soll eine Zahl als Eingabe nehmen und `True` zurückgeben, wenn die Zahl eine Primzahl ist, und `False`, wenn sie es nicht ist. Verwende keine eingebauten Funktionen wie `isprime()` und achte darauf, die Leistung bei größeren Zahlen zu optimieren.
```

### Erklärung:
- Der Prompt stellt sicher, dass die Lösung ohne eingebaute Funktionen auskommt und auf Leistung optimiert ist, was die Anforderungen präzise definiert.

## Übung 3: Datenextraktion aus Text
**Ziel**: Schreiben Sie einen Prompt, der die KI anweist, spezifische Daten aus einem Text zu extrahieren.

### Aufgabe:
- Extrahieren Sie Namen und E-Mail-Adressen aus einem Text und geben Sie die Daten als JSON-Format zurück.

### Text
```text
Johanna Schmidt, johanna.schmidt@email.com, ist die Projektleiterin bei ABC Corp. 
Thomas Müller, thomas.mueller@email.com, arbeitet als Entwickler bei XYZ GmbH.
```

### Lösung
**Prompt**
```text
Extrahiere aus dem folgenden Text alle Namen und E-Mail-Adressen und gib sie im JSON-Format zurück. Achte darauf, dass der Name und die E-Mail-Adresse korrekt zugeordnet sind.

Text: "Johanna Schmidt, johanna.schmidt@email.com, ist die Projektleiterin bei ABC Corp. Thomas Müller, thomas.mueller@email.com, arbeitet als Entwickler bei XYZ GmbH."
```

### Erklärung:
- Der Prompt fordert die KI auf, den Text zu analysieren und die Daten in einem strukturierten Format (JSON) auszugeben. Die klare Anweisung zur Ausgabe im JSON-Format und die präzise Angabe der Daten (Namen und E-Mail-Adressen) vermeiden Unklarheiten.


## Fazit 
- **Mach es der KI leicht**: Je klarer und strukturierter der Prompt, desto besser das Ergebnis.
- **Denke an die Zielgruppe**: Schreibe den Prompt so, als ob du einer Person Anweisungen gibst.
- **Bewerte den Output kritisch**: KI-Modelle liefern Ergebnisse basierend auf den Trainingsdaten – sie sind nicht immer korrekt oder vollständig.

---

// Quellen 
- https://www.coursera.org/de-DE/articles/what-is-prompt-engineering
- https://de.wikipedia.org/wiki/Prompt_Engineering
- https://medium.com/@niall.mcnulty/writing-an-o1-prompt-that-works-16ee921b5859
