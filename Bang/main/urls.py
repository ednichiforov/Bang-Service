from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name="general"),
    path('school', views.school, name="school"),
    path('party', views.party, name="party"),
    path('bar', views.bar, name="bar"),
    path('menu', views.menu, name="menu"),
    path('excel', views.excel, name="excel"),
    path('users', views.users, name="users"),
    path('admin', views.users, name="admin")
]
