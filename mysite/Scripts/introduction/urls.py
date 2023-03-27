from django.urls import path
from Scripts.introduction.views import *

urlpatterns = [
    path('', persons_inform),
]