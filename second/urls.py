from django.urls import path
from .views import first, second, pages

urlpatterns = [
    path('', first, name='first'),
    path('second/', second, name='second'),
    path('pages/<str:page>', pages, name='pages'),
]
