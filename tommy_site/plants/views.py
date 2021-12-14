from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class PlantView(TemplateView):
    template_name = "plant.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
