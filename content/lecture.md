# 0 - Prompt Engineering: Wie man Prompts richtig entwickelt, analysiert und effizient anwendet
**Lernziel:**
Nach diesem Teil der Veranstaltung sollten die Studierenden in der Lage sein, unter Anwendung von Techniken des Prompt Engineering eigene Prompts richtig und effizient zu entwickeln, um ein einfaches Problem zu lösen, bestehende Prompts systematisch zu analysieren und deren Effizienz und Korrektheit für konkrete Anwendungen (z.B. Code-Generierung) zu evaluieren. 

## Was ist Prompt Engineering?
Prompt Engineering ist die Kunst, KI-Modelle wie GPT gezielt zu steuern, sodass sie präzise und effiziente Ergebnisse liefern. In dieser Vorlesung werden wir uns mit der Entwicklung, Analyse und Anwendung von Prompts beschäftigen, um sicherzustellen, dass Sie das Beste aus KI herausholen können.

Prompt Engineering umfasst:
- Die gezielte Gestaltung von Eingaben (Prompts), um aus Sprachmodellen wie GPT optimale Ergebnisse zu erzielen.
- Eine Mischung aus **Technik**, **Kreativität** und **Systematik**.
- Eine neue Sprache im Umgang mit KI: präzise, klar und zielgerichtet.

---

# 1 - Grundlagen: Bestandteile eines Prompts

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
---

# 2 - Typen von Prompts 
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

---

# 3 - Best Practices für das Design von Prompts
- **Sei konkret**: „Erkläre Quantenphysik für ein Kind“ ist viel präziser als „Erkläre Quantenphysik“.
- **Vermeide Mehrdeutigkeit**: Sei klar bei Format, Zielgruppe und Umfang.
- **Nutze Beispiele**: „Gib Beispiele für...“ hilft der KI, die Aufgabe besser zu verstehen.
- **Teste iterativ**: Teste den Prompt, schaue dir das Ergebnis an und passe es an, wenn nötig.
- **Nutze Formatierung**: Verwende Markdown, Codeblöcke und Listen für bessere Klarheit und Struktur.

## 3.1 Prompt Engineering im Coding-Kontext

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

## 3.2 Analyse von Prompts

### Checkliste:
- Ist die Aufgabe eindeutig formuliert?
- Fehlt Kontext oder Hintergrundinformation?
- Wird zu viel auf einmal verlangt?
- Stimmt der Stil mit der Zielgruppe überein?

## 3.3 Optimierung von Prompts

### Schlechter Prompt

```text
Mach was mit dem Text.
```

#### Verbesserter Prompt

```text
Fasse den folgenden Artikel in 3 Sätzen zusammen. Zielgruppe: Schüler der 5. Klasse. Verwende einfache Sprache.
```

## 3.4 Warum verbessern?
Der verbesserte Prompt ist präziser und gibt klare Anweisungen hinsichtlich Umfang, Zielgruppe und Ton.

## Effizienz: Gute Prompts sparen Ressourcen
- **Schneller zum Ziel**: Weniger Tokens führen zu schnelleren und kostengünstigeren Ergebnissen.
- **Mehr Konsistenz**: Bessere Prompts resultieren in weniger Nacharbeit und einer konsistenteren Qualität.
- **Bessere Reproduzierbarkeit**: Gut formulierte Prompts machen Prozesse skalierbar und wiederholbar.

---

# 4 - Prompt-Beispiele aus der Praxis

## 1. Codegenerierung 

```text
Du bist ein Java-Experte. Erstelle eine Funktion, die pürft, ob eine Zahl durch 3 oder 5 teilbar ist.
```

## 2. Übersetzung + Stiländerung

```text
Übersetzte folgenden Satz ins Englische und verwende einen formellen Business-Ton.
```

## 3. Datenextraktion 

```text
Extrahiere alle Namen und E-Mail-Adressen aus dem folgenden Text und gib sie als JSON-Datei zurück.
```

---

# 5 - Übung macht den Meister

## Übung 1: Prompt Debugging
**Ziel**: Identifizieren Sie Schwächen in einem Prompt und verbessern Sie diesen, um präzise und qualitativ hochwertige Ergebnisse zu erhalten.



### Aufgabe:
Original Prompt:
```text
Erzähl mir was über die Geschichte von Berlin.
```
- Überlegen Sie, warum dieser Prompt zu ungenauen oder weit gefassten Ergebnissen führen könnte.
- Welche zusätzlichen Informationen fehlen?
- Wie können Sie den Prompt präziser machen?


$Lösung: ki_task_1

## Übung 2: Erstellung eines Code-Prompts
**Ziel**: Formulieren Sie einen präzisen Prompt, der den Code für eine spezifische Aufgabe generiert.

### Aufgabe:
- Schreiben Sie einen Prompt, der eine Python-Funktion erstellt, die prüft, ob eine Zahl eine Primzahl ist, ohne eingebaute Funktionen wie isprime() zu verwenden.

$Lösung: ki_task_2

## Übung 3: Datenextraktion aus Text
**Ziel**: Schreiben Sie einen Prompt, der die KI anweist, spezifische Daten aus einem Text zu extrahieren.

### Aufgabe:
- Extrahieren Sie Namen und E-Mail-Adressen aus einem Text und geben Sie die Daten als JSON-Format zurück.

Text:
```text
Johanna Schmidt, johanna.schmidt@email.com, ist die Projektleiterin bei ABC Corp. 
Thomas Müller, thomas.mueller@email.com, arbeitet als Entwickler bei XYZ GmbH.
```

$Lösung: ki_task_3

---

# Fazit 
- **Mach es der KI leicht**: Je klarer und strukturierter der Prompt, desto besser das Ergebnis.
- **Denke an die Zielgruppe**: Schreibe den Prompt so, als ob du einer Person Anweisungen gibst.
- **Bewerte den Output kritisch**: KI-Modelle liefern Ergebnisse basierend auf den Trainingsdaten – sie sind nicht immer korrekt oder vollständig.

---

## Quellen 
- https://www.coursera.org/de-DE/articles/what-is-prompt-engineering
- https://de.wikipedia.org/wiki/Prompt_Engineering
- https://medium.com/@niall.mcnulty/writing-an-o1-prompt-that-works-16ee921b5859



# Python List Comprehensions
**Lernziel:**
Nach der Teilnahme an der Lehrveranstaltung sind die Studierenden in der Lage, unter Verwendung von List Comprehension konkrete Anwendungssituationen in Python zu analysieren und in eigenen Worten zu erklären. Dabei können die Studierenden analysieren, welche Funktionalität konkrete Implementierungen einer List Comprehension haben und können selbst eine einfache Listenstruktur mit List Comprehension erstellen.
## Einführung

List Comprehensions (Listenverständnisse) sind eine der leistungsstärksten Funktionen von Python, die es ermöglichen, Listen auf kompakte, lesbare Weise zu erstellen.  
Anstatt mehrere Zeilen mit Schleifen und Bedingungen zu verwenden, kann man dieselbe Operation in einer einzigen Codezeile ausdrücken.

## Warum List Comprehensions?

✅Kompakterer Code (weniger Zeilen)  
✅Oft besser lesbar, sobald man die Syntax versteht  
✅Allgemein schneller als entsprechende `for`-Schleifen  
✅Gilt als "pythonisch" – idiomatischer Python-Stil  

## Grundlegende Syntax

Die grundlegende Syntax ist:

```python
[expression for item in iterable]
```

**Traditioneller Ansatz**

```python
squares = []
for x in range(10):
    squares.append(x**2)
```

**List Comprehension Ansatz**

```python
squares = [x**2 for x in range(10)]
# Ergebnis: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

> 📝Hinweis: Die List Comprehension erreicht in 1 Zeile, wofür eine traditionelle Schleife 3 Zeilen benötigt!

## 🧮Hinzufügen von Bedingungen

Du kannst Elemente mit Bedingungen filtern:

```python
[expression for item in iterable if condition]
```

**💡Beispiel mit Filterung**

```python
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

## ✏️Kurze Übung

> **Aufgabe:** Erstelle eine Liste der ersten 10 Vielfachen von 3.

$Lösung: list_compt_task_1
## 🧩Verschachtelte List Comprehensions

Du kannst mehrdimensionale Strukturen wie Matrizen erstellen:

**Erstellen einer 3×3 Matrix**

```python
matrix = [[i*j for j in range(3)] for i in range(3)]
```

**Ergebnis:**

```python
[[0, 0, 0], 
 [0, 1, 2], 
 [0, 2, 4]]
```

### 💡Beispiel zur Matrix-Transposition

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Zeilen zu Spalten transponieren
transposed = [[row[i] for row in matrix] for i in range(3)]
# Ergebnis: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

> 📝 Hinweis: Die äußere Comprehension erstellt jede neue Spalte, während die innere Werte aus jeder Zeile sammelt.

## 🚀 Fortgeschrittene Techniken

**Bedingte Ausdrücke (if-else)**

Verwendung von if-else zur Transformation von Werten

```python
values = [x if x % 2 == 0 else 'odd' for x in range(10)]
# Ergebnis: [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']
```

**Arbeiten mit Strings**

```python
words = ['apple', 'banana', 'cherry', 'date']
uppercase = [word.upper() for word in words if len(word) > 5]
# Ergebnis: ['BANANA', 'CHERRY']
```

## ⚡ Leistung und Effizienz

List Comprehensions sind in der Regel schneller als for-Schleifen und speichereffizienter bei der Arbeit mit großen Datensätzen.

**Speicheroptimierung mit Generator-Ausdrücken**

Bei der Verarbeitung sehr großer Sequenzen solltest du Generator-Ausdrücke in Betracht ziehen:

**List Comprehension (speichert alles im Arbeitsspeicher)**

```python
sum_squares = sum([x**2 for x in range(1000000)])
```

**Generator-Ausdruck (verarbeitet jeweils einen Wert)**

```python
sum_squares = sum(x**2 for x in range(1000000))
# Beachte die ( ) anstelle von [ ]
```

> 💡 **Profi-Tipp:** Generator-Ausdrücke verbrauchen weniger Speicher, da sie Werte bei Bedarf erzeugen, anstatt die gesamte Liste auf einmal zu speichern.
## 🔄 Andere Comprehensions

**Dictionary Comprehension**

```python
{x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Set Comprehension**

```python
{x**2 for x in [1, 2, 2, 3, 3, 3]}  # {1, 4, 9}
```

## 📋 Best Practices

**✅ Verwende List Comprehensions, wenn:**

- Du eine neue Liste basierend auf einer vorhandenen Sequenz erstellst  
- Du einfache Transformationen oder Filterungen durchführst  
- Die Operation klar in einer Zeile ausgedrückt werden kann  

**❌ Vermeide List Comprehensions, wenn:**

- Die Logik komplex ist oder mehrere Schritte umfasst  
- Die Comprehension schwer zu lesen wird  
- Du Nebeneffekte benötigst (wie Ausgaben)  

### Priorisiere Lesbarkeit:

**Zu komplex für eine Zeile:**

```python
bad = [x for x in [y for y in range(100) if y % 2 == 0] if x % 3 == 0]
```

**Besser als separate Schritte:**

```python
even_numbers = [y for y in range(100) if y % 2 == 0]
result = [x for x in even_numbers if x % 3 == 0]
```

## 📝 Zusammenfassung

- List Comprehensions bieten eine prägnante Möglichkeit, Listen zu erstellen  
- Grundlegende Syntax: `[expression for item in iterable if condition]`  
- Sie sind besser lesbar und oft schneller als traditionelle Schleifen  
- Verwende sie für einfache Operationen; zerlege komplexe Aufgaben  
- Denke daran, dass **Klarheit wichtiger ist als Kompaktheit**

>  🌟 Merke: Obwohl List Comprehensions leistungsstark sind, besteht das Ziel darin, Code zu schreiben, der leicht zu verstehen ist – für dich selbst und andere. Eine gute List Comprehension macht deinen Code **lesbarer und schneller**!

## ✏️Weiterführende Übung

> **Aufgabe:** Gegeben ist eine Liste von Dictionaries, in der Informationen über Studierende und ihre Noten in verschiedenen Fächern gespeichert sind:
```python
students = [
    {"name": "Anna", "grades": {"Mathe": 3, "Deutsch": 2, "Englisch": 1}},
    {"name": "Ben", "grades": {"Mathe": 4, "Deutsch": 3, "Englisch": 2}},
    {"name": "Clara", "grades": {"Mathe": 1, "Deutsch": 1, "Englisch": 1}},
    {"name": "David", "grades": {"Mathe": 5, "Deutsch": 4, "Englisch": 3}},
    {"name": "Eva", "grades": {"Mathe": 2, "Deutsch": 2, "Englisch": 2}},
]
```
> Erstelle eine neue Liste von Tupeln mit dem Namen und dem Durchschnitt der Noten jedes Studierenden. Runde dabei den Durchschnitt auf zwei Nachkommastellen.

$Lösung: list_compt_task_2