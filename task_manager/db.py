# Database configuration lives here
import sqlite3
from task_manager.models import database_schema
from task_manager.commands import Command, get_tasks

def create_database():
    database_name = 'tests.db'

    try:
        
        
        with sqlite3.connect(database=database_name) as conn:
            cursor = conn.cursor()
            schema = database_schema()
            fetch_data = get_tasks

            cursor.execute(schema)
            conn.commit()
            print("Table was successfully created")
        
    except Exception as e:
        print(e.args[0])
        print("error")

    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
        print("Failed to create tables:", e)

create_database()


    
