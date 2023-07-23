from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('add-task', add_task, name='add_task'),
    path('task/<int:pk>/', show_task, name='show_task'),
    path('edit-task/<int:pk>/', edit_task, name='edit_task'),
    path('delete-task/<int:pk>/', delete_task, name='delete_task'),
    path('finish-task/<int:pk>/', finish_task, name='finish_task'),
]
