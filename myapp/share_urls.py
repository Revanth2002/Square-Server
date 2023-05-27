from django.urls import path
from .views import OpenGroupShareUrl
urlpatterns=[
    path('public-share/<str:url>',OpenGroupShareUrl.as_view(),name="open-group-share-url"),
]