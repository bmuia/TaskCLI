import click
from task_manager.commands import Command


@click.group()
def cli():
    """Task Manager CLI"""


@cli.command()
@click.option('--title', prompt="Task title")
@click.option('--description', prompt="Task description")
@click.option('--begin_date', prompt="Begin date (YYYY-MM-DD)")
@click.option('--end_date', prompt="End date (YYYY-MM-DD)")
def add_task(title, description, begin_date, end_date):
    """Add a new task."""
    task = Command(title=title, description=description, begin_date=begin_date, end_date=end_date)
    task.add_task()


@cli.command()
def get_tasks():
    """Get all tasks."""
    task = Command()
    task.get_tasks()


if __name__ == "__main__":
    cli()
