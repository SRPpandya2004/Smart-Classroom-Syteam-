
from django.urls import path
# from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path("", views.index, name='home'),
    path("registration", views.registration, name='registration'),
    path("signin", views.signin, name='signin'),
]