# from django.urls import path
# from . import views



# app_name = 'book-url'
# urlpattern = [
#     path('authors/',views.list_authors,name='list-author'),
# ]

from django.urls import path
from . import views

app_name = 'book-url'  

urlpatterns = [
    path('author/', views.list_authors, name='list_authors'),
    path('tag/', views.list_tags, name='list_tags'),
     path('list/', views.list_books, name='list-books'),
     path('create/', views.create_books, name='create-books')
]