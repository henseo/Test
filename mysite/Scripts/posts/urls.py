from django.urls import path
from Scripts.posts.views import *

urlpatterns = [
    path('', hello_world, name = 'hello_wolrd'),
]