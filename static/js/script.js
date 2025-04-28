document.addEventListener('DOMContentLoaded', function() {
    const content = document.getElementById('content');
    const rawMarkdown = content.textContent.trim();

    function formatMessageContent(content) {
        const html = marked.parse(content);

        setTimeout(() => {
            document.querySelectorAll('pre code').forEach((block) => {
                hljs.highlightBlock(block);
            });
        }, 0);

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
                <textarea placeholder="Your notes for this section..." rows="4"></textarea>
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

    // Add AI question inputs after each h1
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

    // Save button functionality
    document.getElementById('save-button').addEventListener('click', function() {
        window.print();
    });

    // Global function to ask the AI
    window.askAI = function(index) {
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
            responseDiv.innerHTML = data.response;
        })
        .catch(error => {
            responseDiv.innerHTML = `<div class="alert alert-danger">Error: ${error.message}</div>`;
        });
    };
});