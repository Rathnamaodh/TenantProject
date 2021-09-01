from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

import psycopg2

# Create your views here.
def index(request):
    return HttpResponse('Hello, tenant!')

def library_create(request):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO tenant_library_library (library) VALUES ('Chennai Library')")
        # cursor1.execute("UPDATE APP1_Menu set age = 40 where ID = 26")


        cursor.execute("SELECT * FROM tenant_library_library")
        row = cursor.fetchall()
        print(row)
        cursor.close()
        connection.close()

    return HttpResponse(row)


def library_update(request):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE tenant_library_library set library = 'Rk library' where ID = 7")
        

        cursor.execute("SELECT * FROM tenant_library_library")
        row = cursor.fetchall()
        print(row)
        cursor.close()
        connection.close()

    return HttpResponse(row) 

def library_delete(request):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM tenant_library_library where ID = 7")
        cursor.execute("SELECT * FROM tenant_library_library")
        row = cursor.fetchall()
        print(row)
        cursor.close()
        connection.close()

    return HttpResponse(row) 