import sqlite3
from rich.console import Console
from rich.table import Table


class Command:
    def __init__(self, id=None, title=None, description=None, begin_date=None, end_date=None, column=None):
        self.id = id
        self.title = title
        self.description = description
        self.begin_date = begin_date
        self.end_date = end_date
        self.db_name = 'tests.db'
        self.column = column 
        self.console = Console()

    # Add a task
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

            table = Table(title="✅ Task Successfully Created")
            table.add_column("ID", style="cyan", no_wrap=True)
            table.add_column("Title", style="green")
            table.add_column("Description", style="magenta")
            table.add_column("Begin Date", style="yellow")
            table.add_column("End Date", style="yellow")

            table.add_row(str(task_id), self.title, self.description, self.begin_date, self.end_date)
            self.console.print(table)

    # Get all tasks
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
        except sqlite3.Error as e:
            self.console.print(f"[red]Error:[/red] {e}")

    # Delete a task
    def remove_task(self):
        command = 'DELETE FROM tasks WHERE id = ?'
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(command, (self.id,))
                conn.commit()
                self.console.print(f'[green][bold] Task {self.id} has been deleted[/bold][/green]')
        except sqlite3.Error as e:
            self.console.print(f"[red]Error:[/red] {e}")

    # Get one task
    def get_task(self):
        command = 'SELECT * FROM tasks WHERE id = ?'
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(command, (self.id,))
                row = cursor.fetchone()
                if row:
                    table = Table(title=f"📌 Task {row[0]}")
                    table.add_column("ID", style="cyan")
                    table.add_column("Title", style="green")
                    table.add_column("Description", style="magenta")
                    table.add_column("Begin Date", style="yellow")
                    table.add_column("End Date", style="yellow")
                    table.add_row(str(row[0]), row[1], row[2] or "", row[3], row[4])
                    self.console.print(table)
                else:
                    self.console.print(f"[red]Task {self.id} not found[/red]")
        except sqlite3.Error as e:
            self.console.print(f"[red]Error:[/red] {e}")

    # Update a task
    def update_task(self):
        if not self.column:
            self.console.print("[red]No column specified to update[/red]")
            return

        field, value = self.column
        if field not in ("title", "description", "begin_date", "end_date"):
            self.console.print(f"[red]Invalid field: {field}[/red]")
            return

        command = f'UPDATE tasks SET {field} = ? WHERE id = ?'
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(command, (value, self.id))
                conn.commit()
                self.console.print(f'[green][bold] Task {self.id} updated: {field} = {value}[/bold][/green]')
        except sqlite3.Error as e:
            self.console.print(f"[red]Error:[/red] {e}")
