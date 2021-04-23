from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name="general"),
    path('school', views.school, name="school"),
    path('party', views.party, name="party"),
    path('bar', views.bar, name="bar"),
    path('users/<str:user_id>', views.users, name="users"),
]
