from django.db import connection

def ejecutaSql(txsql):
    with connection.cursor() as cursor:
        cursor.execute(txsql)
        row = cursor.fetchall()
    return row