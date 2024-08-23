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
    path('', views.list_authors, name='list_authors')
]