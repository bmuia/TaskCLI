import sqlite3
import os
import pytest
from task_manager.models import database_schema

TEST_DB = "test_tasks.db"

@pytest.fixture
def setup_db():
    """Create a fresh test database before each test, and delete after."""
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.executescript(database_schema())
    conn.commit()
    yield conn
    conn.close()
    os.remove(TEST_DB)


def test_table_created(setup_db):
    """Check if 'tasks' table exists"""
    conn = setup_db
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks';")
    result = cursor.fetchone()

    assert result is not None
    assert result[0] == "tasks"


def test_insert_and_retrieve(setup_db):
    """Check inserting and retrieving a task works"""
    conn = setup_db
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, description, begin_date, end_date)
        VALUES (?, ?, ?, ?)
    """, ("Test Task", "Description here", "2025-09-01", "2025-09-02"))
    conn.commit()

    cursor.execute("SELECT title, description FROM tasks WHERE title=?", ("Test Task",))
    row = cursor.fetchone()

    assert row is not None
    assert row[0] == "Test Task"
    assert row[1] == "Description here"
