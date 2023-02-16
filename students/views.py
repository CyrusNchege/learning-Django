from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'header.html', {'name': 'Cyrus'})


def contact(request):
    return render(request, 'contact.html')
