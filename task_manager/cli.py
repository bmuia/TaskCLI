import click
from task_manager.commands import Command


@click.group()
def cli():
    """Task Manager CLI"""


@cli.command("add")
@click.option("--title", prompt="Task title")
@click.option("--description", prompt="Task description")
@click.option("--begin_date", prompt="Begin date (YYYY-MM-DD)")
@click.option("--end_date", prompt="End date (YYYY-MM-DD)")
def add_task(title, description, begin_date, end_date):
    """Add a new task."""
    task = Command(title=title, description=description, begin_date=begin_date, end_date=end_date)
    task.add_task()


@cli.command("list")
def list_tasks():
    """List all tasks."""
    task = Command()
    task.get_tasks()


@cli.command("update")
@click.option("--id", prompt="Task ID", type=int)
@click.option("--field", prompt="Field (title, description, begin_date, end_date)")
@click.option("--value", prompt="New value")
def update_task(id, field, value):
    """Update a task by ID."""
    task = Command(id=id, column=(field, value))
    task.update_task()


@cli.command("delete")
@click.option("--id", prompt="Task ID", type=int)
def delete_task(id):
    """Delete a task by ID."""
    task = Command(id=id)
    task.remove_task()


@cli.command("show")
@click.option("--id", prompt="Task ID", type=int)
def show_task(id):
    """Show details for one task."""
    task = Command(id=id)
    task.get_task()
