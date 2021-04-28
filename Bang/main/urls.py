from django.urls import path
from . import views

urlpatterns = [
    path("", views.general, name="general"),
    path("users/<str:user_id>", views.users, name="users"),
]
