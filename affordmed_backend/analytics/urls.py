from django.urls import path
from .views import *

urlpatterns = [
    path('top-users/', top_users),
        path('posts/', get_posts),
]
