document.addEventListener('DOMContentLoaded', function () {
    const content = document.getElementById('content');
    const rawMarkdown = content.textContent.trim();

    function formatMessageContent(content) {
        const html = marked.parse(content);

        setTimeout(() => {
            document.querySelectorAll('pre code').forEach((block) => {
                hljs.highlightBlock(block);
            });
        }, 200);

        return html;
    }

    // Parse the markdown content
    content.innerHTML = formatMessageContent(rawMarkdown);

    // Get all the h1, h2, and h3 headings
    const headings = Array.from(content.querySelectorAll('h1, h2, h3'));

    // Add notes areas before each heading (except the first one)
    headings.forEach((heading, index) => {
        if (index > 0) {  // Skip the first heading
            const notesArea = document.createElement('div');
            notesArea.className = 'notes-area';
            notesArea.innerHTML = `
                <textarea placeholder="Your notes for this section..." rows="4" id="notes-${index}"></textarea>
            `;
            heading.before(notesArea);
        }
    });

    // Add a final notes area at the end
    if (headings.length > 0) {
        const notesArea = document.createElement('div');
        notesArea.className = 'notes-area';
        notesArea.innerHTML = `
            <textarea placeholder="Your final notes..." rows="4"></textarea>
        `;
        content.appendChild(notesArea);
    }

    // Find elements containing "$Lösung: " and add check buttons
    // to the nearest notes area
    Array.from(content.querySelectorAll('p, li')).forEach((element, idx) => {
        if (element.textContent.includes('$Lösung: ')) {
            const text = element.textContent;
            const pattern = text.split('$Lösung: ')[1].trim();

            // Text ohne das Lösungsmuster anzeigen
            element.textContent = text.split('$Lösung: ')[0];

            // Finde das nächstliegende Notizfeld
            let closestNotesArea = null;
            let currentElement = element;

            // Suche nach dem nächsten Notizfeld
            while (currentElement.nextElementSibling) {
                currentElement = currentElement.nextElementSibling;
                if (currentElement.classList.contains('notes-area')) {
                    closestNotesArea = currentElement;
                    break;
                }
            }

            // Falls kein Notizfeld gefunden wurde, suche nach dem vorherigen
            if (!closestNotesArea) {
                currentElement = element;
                while (currentElement.previousElementSibling) {
                    currentElement = currentElement.previousElementSibling;
                    if (currentElement.classList.contains('notes-area')) {
                        closestNotesArea = currentElement;
                        break;
                    }
                }
            }

            // Wenn ein Notizfeld gefunden wurde, füge den Überprüfungsbutton hinzu
            if (closestNotesArea) {
                const textarea = closestNotesArea.querySelector('textarea');

                // Erstelle Überprüfungsbutton
                const checkButton = document.createElement('button');
                checkButton.className = 'btn btn-primary mt-2';
                checkButton.textContent = 'Lösung überprüfen';

                // Erstelle Ergebnisbereich
                const resultDiv = document.createElement('div');
                resultDiv.id = `solution-result-${idx}`;
                resultDiv.className = 'mt-2';

                // Füge Überprüfungsfunktion hinzu
                checkButton.onclick = function () {
                    const userInput = textarea.value.trim();

                    // API-Aufruf zur Lösungsüberprüfung
                    fetch('/api/check-solution', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            userInput: userInput,
                            pattern: pattern
                        }),
                    })
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok');
                            }
                            return response.json();
                        })
                        .then(data => {
                            if (data.isCorrect) {
                                resultDiv.innerHTML = '<div class="alert alert-success">Korrekte Lösung!</div>';
                            } else {
                                resultDiv.innerHTML = '<div class="alert alert-danger">Falsche Lösung. Bitte versuche es erneut!</div>';
                            }
                        })
                        .catch(error => {
                            resultDiv.innerHTML = `<div class="alert alert-warning">Fehler bei der Überprüfung: ${error.message}</div>`;
                            console.error('Fehler:', error);
                        });
                };

                closestNotesArea.appendChild(checkButton);
                closestNotesArea.appendChild(resultDiv);
            }
        }
    });

    // Bestehender Code für AI-Fragen und Save-Button bleibt unverändert
    const h1Elements = Array.from(content.querySelectorAll('h1'));
    h1Elements.forEach((h1, index) => {
        const aiQuestion = document.createElement('div');
        aiQuestion.className = 'ai-question no-print';
        aiQuestion.innerHTML = `
            <div class="input-group">
                <input type="text" class="form-control" placeholder="Ask AI about this topic" id="question-${index}">
                <button class="btn btn-primary" onclick="askAI(${index})">Ask AI</button>
            </div>
            <div class="ai-response" id="response-${index}" style="display: none;"></div>
        `;
        h1.after(aiQuestion);
    });

    document.getElementById('save-button').addEventListener('click', function () {
        window.print();
    });

    // Global function to ask the AI
    window.askAI = function (index) {
        const questionInput = document.getElementById(`question-${index}`);
        const responseDiv = document.getElementById(`response-${index}`);
        const question = questionInput.value.trim();

        if (!question) {
            alert('Please enter a question');
            return;
        }

        // Display a loading indicator
        responseDiv.style.display = 'block';
        responseDiv.innerHTML = '<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>';

        fetch('/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: question,
                section_index: index
            }),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                response_as_md = formatMessageContent(data.response)
                responseDiv.innerHTML = response_as_md;
            })
            .catch(error => {
                responseDiv.innerHTML = `<div class="alert alert-danger">Error: ${error.message}</div>`;
            });
    };
});