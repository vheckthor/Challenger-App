from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.month_int),
    path("<str:month>", views.remaining_month, name="monthchallenge")
]
