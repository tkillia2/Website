from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ProjectsView(TemplateView):
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
