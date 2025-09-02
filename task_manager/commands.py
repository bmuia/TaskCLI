import sqlite3
from rich.console import Console
from rich.table import Table


class Command:
    def __init__(self, id=None, title=None, description=None, begin_date=None, end_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.begin_date = begin_date
        self.end_date = end_date
        self.db_name = 'tests.db'
        self.console = Console()

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
            task_id = cursor.lastrowid

            # Pretty output
            table = Table(title="✅ Task Successfully Created")
            table.add_column("ID", style="cyan", no_wrap=True)
            table.add_column("Title", style="green")
            table.add_column("Description", style="magenta")
            table.add_column("Begin Date", style="yellow")
            table.add_column("End Date", style="yellow")

            table.add_row(str(task_id), self.title, self.description, self.begin_date, self.end_date)
            self.console.print(table)

            return task_id

    # 2. Get all tasks
    def get_tasks(self):
        command = "SELECT * FROM tasks;"
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(command)
                rows = cursor.fetchall()

              
                table = Table(title="📋 All Tasks")
                table.add_column("ID", style="cyan")
                table.add_column("Title", style="green")
                table.add_column("Description", style="magenta")
                table.add_column("Begin Date", style="yellow")
                table.add_column("End Date", style="yellow")

                for row in rows:
                    table.add_row(str(row[0]), row[1], row[2] or "", row[3], row[4])

                self.console.print(table)
                return rows

        except sqlite3.Error as e:
            self.console.print(f"[red]Error:[/red] {e}")
            return []



