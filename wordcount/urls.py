from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name = "home_page"),
    path("count/", views.count, name = "count"),
    path("about/", views.about_page, name = "about_page"),
]
