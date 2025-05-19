
# Python List Comprehensions

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

### Traditioneller Ansatz

```python
squares = []
for x in range(10):
    squares.append(x**2)
```

### List Comprehension Ansatz

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

### 💡Beispiel mit Filterung

```python
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

## ✏️Kurze Übung

> **Aufgabe:** Erstelle eine Liste der ersten 10 Vielfachen von 3.

$Lösung:  r'^\[\s*3\s*\*\s*i\s+for\s+i\s+in\s+range\s*\(\s*1\s*,\s*11\s*\)\s*\]$'
## 🧩Verschachtelte List Comprehensions

Du kannst mehrdimensionale Strukturen wie Matrizen erstellen:

### Erstellen einer 3×3 Matrix

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

### Bedingte Ausdrücke (if-else)

#### Verwendung von if-else zur Transformation von Werten

```python
values = [x if x % 2 == 0 else 'odd' for x in range(10)]
# Ergebnis: [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']
```

### Arbeiten mit Strings

```python
words = ['apple', 'banana', 'cherry', 'date']
uppercase = [word.upper() for word in words if len(word) > 5]
# Ergebnis: ['BANANA', 'CHERRY']
```

## ⚡ Leistung und Effizienz

List Comprehensions sind in der Regel schneller als for-Schleifen und speichereffizienter bei der Arbeit mit großen Datensätzen.

### Speicheroptimierung mit Generator-Ausdrücken

Bei der Verarbeitung sehr großer Sequenzen solltest du Generator-Ausdrücke in Betracht ziehen:

#### List Comprehension (speichert alles im Arbeitsspeicher)

```python
sum_squares = sum([x**2 for x in range(1000000)])
```

#### Generator-Ausdruck (verarbeitet jeweils einen Wert)

```python
sum_squares = sum(x**2 for x in range(1000000))
# Beachte die ( ) anstelle von [ ]
```

> 💡 **Profi-Tipp:** Generator-Ausdrücke verbrauchen weniger Speicher, da sie Werte bei Bedarf erzeugen, anstatt die gesamte Liste auf einmal zu speichern.

## 📋 Best Practices

### ✅ Verwende List Comprehensions, wenn:

- Du eine neue Liste basierend auf einer vorhandenen Sequenz erstellst  
- Du einfache Transformationen oder Filterungen durchführst  
- Die Operation klar in einer Zeile ausgedrückt werden kann  

### ❌ Vermeide List Comprehensions, wenn:

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

## 🔄 Andere Comprehensions

### Dictionary Comprehension

```python
{x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Set Comprehension

```python
{x**2 for x in [1, 2, 2, 3, 3, 3]}  # {1, 4, 9}
```

## 📝 Zusammenfassung

- List Comprehensions bieten eine prägnante Möglichkeit, Listen zu erstellen  
- Grundlegende Syntax: `[expression for item in iterable if condition]`  
- Sie sind besser lesbar und oft schneller als traditionelle Schleifen  
- Verwende sie für einfache Operationen; zerlege komplexe Aufgaben  
- Denke daran, dass **Klarheit wichtiger ist als Kompaktheit**

>  🌟 Merke: Obwohl List Comprehensions leistungsstark sind, besteht das Ziel darin, Code zu schreiben, der leicht zu verstehen ist – für dich selbst und andere. Eine gute List Comprehension macht deinen Code **lesbarer und schneller**!
