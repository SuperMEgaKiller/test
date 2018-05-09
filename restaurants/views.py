from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView



class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context = {'var': 124}
        return context


# class ContactView(TemplateView):
#     template_name = 'contacts.html'


# class AboutView(TemplateView):
#     template_name = 'about.html'


# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "contacts.html")


# def home(request):
#     return render(request, "home.html")

# def about(request):
#     return render(request, "about.html")

# def contacts(request):
#     return render(request, "contacts.html")