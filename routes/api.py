import re
from typing import List, Dict

import anthropic
from flask import Blueprint, request, jsonify, session

import counters

api_blueprint = Blueprint('api', __name__)


# This will be overridden by the function in __init__.py
def parse_markdown_sections(markdown_content):
    pass


def _call_anthropic_api(model: str, system_prompt: str, messages: List[Dict[str, str]],
                        max_tokens: int, anthropic_client) -> str:
    """Call the Anthropic API to generate a response."""
    if not anthropic_client:
        return "Error: Anthropic client not initialized"

    try:
        # Call the API
        response = anthropic_client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=messages
        )
        print(response)  # Keeping the debug print

        # Extract token counts and update session cost
        tokens = {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens
        }
        return response.content[0].text
    except Exception as e:
        response = f"Error calling Anthropic API: {str(e)}."
        return response


def call_api(question, section_content):
    anthropic_client = anthropic.Anthropic(api_key="")
    model = "claude-3-5-haiku-latest"
    system_prompt = ("Du bist ein eingebetteter KI Assistent in einer Web App für Studierende. Du kannst nur innerhalb "
                     "Web App verwendet werden und wirst immer den aktuellen Teil des Uni-Skriptes sowie eine Anfrage "
                     "von einem Student bekommen. Gib dein Bestes, die Frage präzise, ausführlich, simpel und fachlich "
                     "korrekt zu beantworten. Antworte nur auf die Frage des Studenten. Deine Antwort wird in dem Skript "
                     "ohne Veränderung angezeigt. Versuche keine Lösungen vorzugeben, sondern erkläre die Konzepte zum "
                     "Verständnis.")
    prompt = (f"Dies ist die Frage des Nutzers:\n{question}\n Dies ist der aktuelle Abschnitt "
              f"des Skriptes:\n{section_content}")
    prompt = [{"role": "user", "content": prompt}]
    return _call_anthropic_api(model, system_prompt, prompt, 4096, anthropic_client)


@api_blueprint.route('/ask', methods=['POST'])
def ask_ai():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Invalid session"}), 400

    data = request.json
    section_index = data.get('section_index', 0)
    question = data.get('question', '')

    # Read the markdown file
    with open('content/lecturev2.md', 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the markdown and extract the section
    section_boundaries = parse_markdown_sections(content)

    if section_index < 0 or section_index >= len(section_boundaries):
        return jsonify({"error": "Invalid section index"}), 400

    start, end = section_boundaries[section_index]
    section_content = '\n'.join(content.split('\n')[start:end + 1])

    response = f"AI Response: {call_api(question, section_content)}"

    return jsonify({"response": response})


SOLUTION_PATTERNS = {
    "list_comprehension_multiples_3": r"^\[3\s*\*\s*([a-zA-Z])\s+for\s+\1\s+in\s+range\(1,\s*11\)\]$",
    "simple_list": r"^\[\d+(,\s*\d+)*\]$",
    "for_loop_range": r"^for\s+\w+\s+in\s+range\([^)]+\):$",
    "function_definition": r"^def\s+\w+\([^)]*\):$",
}


@api_blueprint.route('/check-solution', methods=['POST'])
def check_solution():
    data = request.json
    user_input = data.get('userInput', '')
    solution_id = data.get('solutionId', '')

    try:
        # Pattern anhand der ID aus Dictionary holen
        if solution_id not in SOLUTION_PATTERNS:
            return jsonify({"error": f"Solution ID '{solution_id}' not found"}), 400

        pattern = SOLUTION_PATTERNS[solution_id]

        print(f"User input: {user_input}")
        print(f"Solution ID: {solution_id}")
        print(f"Using pattern: {pattern}")

        is_correct = bool(re.fullmatch(pattern, user_input))

        if is_correct:
            correct, failed = counters.increment_correct_solutions()
        else:
            correct, failed = counters.increment_failed_attempts()

        return jsonify({
            "isCorrect": is_correct,
            "correctSolutions": correct,
            "failedAttempts": failed,
            "solutionId": solution_id
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400