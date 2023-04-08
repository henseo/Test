from django.urls import path
from posts.views import *

urlpatterns = [
    #path('', hello_world, name = 'hello_world'),
    path('introduction', introduction, name = 'introduction'),
    path('<int:post_id>/', post_detail, name = 'post_detail'),
    #path('post_detail/', get_post_all, name = 'post_all'),
    path('new/', create_post, name = "create_post"),
    path('', get_post_all, name = "get_post_all"),
    path('comment/<int:post_id>/', get_comment, name = 'get_comment')
]