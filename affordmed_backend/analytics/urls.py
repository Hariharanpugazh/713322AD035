from django.urls import path
from .views import TopUsersAPIView

urlpatterns = [
    path('top-users', TopUsersAPIView.as_view()),  # First required API
]
