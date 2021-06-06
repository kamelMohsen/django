from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.months_n),
    path("<str:month>", views.months_s, name="month-challenge"),
]