# Database schema goes hear

def database_schema():
    return """
    CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NULL,
    begin_date DATE NOT NULL, 
    end_date DATE NOT NULL
    )
    """