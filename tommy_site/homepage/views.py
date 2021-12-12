from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Intro
from django.views.generic import ListView

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        intro = Intro.objects.first()
        #context["intro"] = getattr(intro, "intro")
        return context
