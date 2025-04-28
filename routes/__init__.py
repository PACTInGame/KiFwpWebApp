def parse_markdown_sections(markdown_content):
    """
    Parse the markdown content and identify h1 section boundaries,
    ignoring content inside code blocks.
    Returns a list of (start_line, end_line) tuples for each h1 section.
    """
    lines = markdown_content.split('\n')
    section_boundaries = []
    current_section_start = None
    inside_code_block = False

    for i, line in enumerate(lines):
        # Check if we're entering or leaving a code block
        if line.strip().startswith('```'):
            inside_code_block = not inside_code_block
            continue

        # Only detect h1 headers when outside of code blocks
        if not inside_code_block and line.startswith('# '):
            if current_section_start is not None:
                section_boundaries.append((current_section_start, i - 1))
            current_section_start = i

    # Add the last section
    if current_section_start is not None:
        section_boundaries.append((current_section_start, len(lines) - 1))

    return section_boundaries


def register_routes(app):
    from .main import main_blueprint
    from .api import api_blueprint

    # Make parse_markdown_sections available to route modules
    from . import main, api
    main.parse_markdown_sections = parse_markdown_sections
    api.parse_markdown_sections = parse_markdown_sections

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')