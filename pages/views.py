from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from pages.form import ContactModelForm
class HomePageView(TemplateView):
    template_name = "home.html"

class ContactTemplateView(CreateView):
    template_name= "contact.html"
    form_class = ContactModelForm
    success_url = '/'
"""
    def get(self, reques, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))
        """

