from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:blog_title>", views.blogs_n),
    path("<str:blog_title>", views.blogs_s, name="blog-slug"),

]