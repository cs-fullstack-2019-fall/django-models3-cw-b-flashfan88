from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=60)
    pageNumber = models.IntegerField()
    genre = models.CharField(max_length=60)
    publishDate = models.DateTimeField(default=0)

    def __str__(self):
        return Book.name.all()




