from django.urls import path
from . import views

urlpatterns = [
    path("", views.AboutView.as_view()),
]
