from flask import Flask, session
from routes import register_routes
import os
import counters  # Neue Import-Anweisung


def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)  # Für Session-Management

    # Register routes
    register_routes(app)

    @app.before_request
    def before_request():
        # Seitenaufrufe inkrementieren
        counters.increment_page_views()

        # Aktive Verbindungen verfolgen
        if 'user_id' in session:
            n_connections = counters.add_active_connection(session['user_id'])

        # In Konsole ausgeben
        print(f"Aktive Verbindungen: {len(counters.active_connections)}, Gesamtaufrufe: {counters.page_views}")

    return app


def setup():
    """Ensure all necessary directories and files exist."""
    # Create content directory if it doesn't exist
    os.makedirs('content', exist_ok=True)

    # Create sample markdown file if it doesn't exist
    if not os.path.exists('content/lecturev2.md'):
        with open('content/lecturev2.md', 'w') as f:
            f.write("""# Introduction to Python

Python is a high-level, interpreted programming language known for its readability and versatility.

## Basic Syntax

Python's syntax allows you to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.

```python
# This is a simple Python program
print("Hello, World!")
Try running this code in your local environment!


Data Types in Python

Python has several built-in data types, including:



Numeric Types: int, float, complex

Sequence Types: list, tuple, range

Mapping Type: dict

Set Types: set, frozenset

Boolean Type: bool

Binary Types: bytes, bytearray, memoryview


Numeric Types

Integers

Integers are whole numbers without a fractional component.


x = 5
y = -10
z = 0

Floating-Point Numbers

Floating-point numbers, or floats, are numbers with a decimal point.


a = 3.14
b = -2.5
c = 0.0

Control Flow in Python

Python provides several ways to control the flow of a program:



Conditional statements (if, elif, else)

Loops (for, while)

Control statements (break, continue, pass)


Conditional Statements

Conditional statements are used to perform different actions based on different conditions.


x = 10

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

Try implementing a more complex conditional statement as an exercise!
""")
if __name__ == '__main__':
    setup()
    app = create_app()
    app.run(host="0.0.0.0", debug=True, port=5001)
