from django.shortcuts import render , get_object_or_404
from .forms import ContactForm
from .models import *

def index(request):
    data = {
        'portfolio':Portfolio.objects.all(),
    }
    return render(request,'main/index.html',data)

def about(request):
    return render(request,'main/about.html')

def contact(request):
    if request.method == 'post':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save

    data = {
        'form': ContactForm(),
    }
    return render(request,'main/contact.html',data,)

def portfolio(request):
    return render(request,'main/portfolio.html')

def work(request,portfolio_slug):
    data={
        'post': get_object_or_404(Portfolio,slug=portfolio_slug)
    }
    return render(request,'main/work.html',data)
