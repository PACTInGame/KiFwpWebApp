from flask import Blueprint, request, jsonify, session

api_blueprint = Blueprint('api', __name__)


# This will be overridden by the function in __init__.py
def parse_markdown_sections(markdown_content):
    pass


@api_blueprint.route('/ask', methods=['POST'])
def ask_ai():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Invalid session"}), 400

    data = request.json
    section_index = data.get('section_index', 0)
    question = data.get('question', '')

    # Read the markdown file
    with open('content/lecture.md', 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the markdown and extract the section
    section_boundaries = parse_markdown_sections(content)

    if section_index < 0 or section_index >= len(section_boundaries):
        return jsonify({"error": "Invalid section index"}), 400

    start, end = section_boundaries[section_index]
    section_content = '\n'.join(content.split('\n')[start:end + 1])

    response = f"AI Response: {question, section_content}"

    return jsonify({"response": response})