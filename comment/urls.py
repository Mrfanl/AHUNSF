from .views import *
from django.urls import path

# start with /comment/
urlpatterns = [
    path('update_comment', update_comment, name='update_comment'),
    path('delete_comment', delete_comment, name='delete_comment'),
]
