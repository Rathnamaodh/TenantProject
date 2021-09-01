from django.db import models

# Create your models here.
class Library(models.Model):
    library = models.CharField(max_length=60)

    def __str__(self):
        return self.library