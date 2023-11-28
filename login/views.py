from django.shortcuts import render
from django.views import generic

# Create your views here.
class Home( generic.TemplateView):
    template_name = 'index.html'
    login_url = 'login'

def login(request):
    return render (
        request,
        'login.html'
    )