from flask import Blueprint, render_template, session
import uuid
import os

main_blueprint = Blueprint('main', __name__)


# This will be overridden by the function in __init__.py
def parse_markdown_sections(markdown_content):
    pass


@main_blueprint.route('/')
def index():
    # Initialize a unique session ID for the user if not exists
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())

    # Read the markdown file
    with open('content/lecturev2.md', 'r', encoding='utf-8') as file:
        content = file.read()

    # Identify section boundaries
    section_boundaries = parse_markdown_sections(content)

    return render_template('index.html', content=content, section_boundaries=section_boundaries)