from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

import psycopg2

# Create your views here.
def index(request):
    return HttpResponse('Hello, Rathnam!')

def book_create(request):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO shared_books_book (book,author,isbn) VALUES ('pppp','qqqqqq',22222222)")
        # cursor1.execute("UPDATE APP1_Menu set age = 40 where ID = 26")


        cursor.execute("SELECT * FROM shared_books_book")
        row = cursor.fetchall()
        print(row)
        cursor.close()
        connection.close()

    return HttpResponse(row)


def book_update(request):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE shared_books_book set book = 'sssssssssssss',author = 'ooooooooooooo' where ID = 9")
        

        cursor.execute("SELECT * FROM shared_books_book")
        row = cursor.fetchall()
        print(row)
        cursor.close()
        connection.close()

    return HttpResponse(row) 

def book_delete(request):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM shared_books_book where ID = 9")
        cursor.execute("SELECT * FROM shared_books_book")
        row = cursor.fetchall()
        print(row)
        cursor.close()
        connection.close()

    return HttpResponse(row) 