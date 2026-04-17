import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

with connection.cursor() as cursor:
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'organizations_organization';")
    columns = cursor.fetchall()
    print("Columns in 'organizations_organization':")
    for col in columns:
        print(f" - {col[0]}")
