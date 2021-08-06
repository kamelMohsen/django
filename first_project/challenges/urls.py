from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"), # challenges/
    path("<int:month>", views.months_n),
    path("<str:month>", views.months_s, name="month-challenge"),
]