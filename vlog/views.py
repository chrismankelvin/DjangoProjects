from django.shortcuts import render
from .models import Post
# from . import views 



# Create your views here.
def home(request):
    return render(request, 'vlog/base.html')

def index(request):
    return render(request, 'vlog/index.html')

def about(request):
    return render(request, 'vlog/about.html')

def appointment(request):
    return render(request, 'vlog/appointment.html')

def chat(request):
    context={'posts': Post.objects.all()}
    return render(request, 'vlog/chat.html', context)

def service(request):
    return render(request, 'vlog/service.html')

def signup(request):
    return render(request, 'vlog/signup.html')