from django.urls import path
from .views import *
urlpatterns=[
    path('login-user/',LoginUser.as_view(),name="login-user"),
]