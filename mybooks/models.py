from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100, default="noaniq")
    description = models.TextField(default="Izoh mavjud emas.")


    def __str__(self):
        return self.title
