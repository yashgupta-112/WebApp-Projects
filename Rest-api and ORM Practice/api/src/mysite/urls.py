from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("apilist/", views.apioverview, name="apilist"),
    path("api/", views.api, name="api"),
    path("apidetail/<str:pk>/", views.apidetail, name="apilist"),
    path("apicreate/", views.apicreate, name="apicreate"),
    path("apidelete/<str:pk>/", views.apidelete, name="apidelete"),
    path("apiupdate/<str:pk>/", views.apiupdate, name="apiupdate"),
]
