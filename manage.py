#!/usr/bin/env python
import os
import sys
from django.db import connection

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ts_django.settings')
    try:
        from django.core.management import execute_from_command_line
        cursor = connection.cursor()
        query = '''CREATE TABLE if not exists api_item(id serial PRIMARY KEY, title VARCHAR (200) UNIQUE NOT NULL, content VARCHAR (200) NOT NULL);'''
        cursor.execute(query)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()