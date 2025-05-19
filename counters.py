page_views = 0
active_connections = set()  # Set für eindeutige Nutzer-IDs
correct_solutions = 0
failed_attempts = 0

def increment_page_views():
    global page_views
    page_views += 1
    return page_views

def add_active_connection(user_id):
    global active_connections
    active_connections.add(user_id)
    return len(active_connections)

def increment_correct_solutions():
    global correct_solutions, failed_attempts
    correct_solutions += 1
    print(f"Korrekte Lösungen: {correct_solutions}, Fehlversuche: {failed_attempts}")
    return correct_solutions, failed_attempts

def increment_failed_attempts():
    global correct_solutions, failed_attempts
    failed_attempts += 1
    print(f"Korrekte Lösungen: {correct_solutions}, Fehlversuche: {failed_attempts}")
    return correct_solutions, failed_attempts