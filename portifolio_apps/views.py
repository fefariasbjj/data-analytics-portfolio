from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Renderiza o template index.html
    return render(request, 'portifolio_apps/index.html')
# Create your views here.
