from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, View
from django.urls import reverse, reverse_lazy
from home.models import HomeItem
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, template_name='home/home.html')


class HomeView(ListView):
    template_name = 'home/home.html'
    model = HomeItem

    
class ContactFormSubmitView(View):
    def post(self, request, *args, **kwargs):
       
      return redirect('home')