import sqlite3

class Command:
    def __init__(self, id=None, title=None, description=None, begin_date=None, end_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.begin_date = begin_date
        self.end_date = end_date
        self.db_name = 'tests.db'

    # 1. Add a new task
    def add_task(self):
        command = """
        INSERT INTO tasks (title, description, begin_date, end_date) 
        VALUES(?,?,?,?)
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(command, (self.title, self.description, self.begin_date, self.end_date))
            conn.commit()
            print("Successfully created task")
            return cursor.lastrowid
        
    # 2. Get all tasks
    def get_tasks(self):
        command = "SELECT * FROM tasks;"
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(command)
                rows = cursor.fetchall()
                return rows
        except sqlite3.Error as e:
            print("Error:", e)
            return []


if __name__ == "__main__":
    task_handler = Command(title="Test Task 2", description="A sample2", begin_date="2025-09-01", end_date="2025-09-02")
    task_handler.add_task()
    print(task_handler.get_tasks())
