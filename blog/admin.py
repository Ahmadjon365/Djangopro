from django.contrib import admin
from .models import Author, Ganre, Post #, Book

# Register your models here.
admin.site.register(Author)
admin.site.register(Ganre)
# admin.site.register(Book)
admin.site.register(Post)
