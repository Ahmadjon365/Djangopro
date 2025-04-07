from django.utils import timezone, text
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Ganre(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
#     ganre = models.ForeignKey(Ganre, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.title

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    publish_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.title)
        super().save(*args, **kwargs)
