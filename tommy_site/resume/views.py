from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ResumeView(TemplateView):
    template_name = "resume.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
