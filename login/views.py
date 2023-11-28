from django.shortcuts import render, HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'
    login_url = 'login'

def login(request):
    return render (
        request,
        'login.html'
    )