from django.db import models

# Create your models here.

class Book(models.Model):
    book = models.CharField(max_length=60)
    author = models.CharField(max_length=120)
    isbn = models.IntegerField()

    def __str__(self):
        return self.book