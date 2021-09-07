# from django.http import HttpResponse
# from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def homepageview(request):
#     return HttpResponse('hello world!')
class HomePageView(TemplateView):
    template_name='home.html'
class AboutPageView(TemplateView):
    template_name='about.html'

class Base(TemplateView):
    template_name='base.html'