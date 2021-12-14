from django.urls import path
from . import views

urlpatterns = [
    path("", views.PlantView.as_view()),
]
