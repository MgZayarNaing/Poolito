from django.shortcuts import render
from .models import *
# Create your views here.

def Home_view(request):
    hero_area = HeroArea.objects.all().order_by('-id')[:1]
    contex = {
        'hero_area': hero_area
    }
    return render(request, 'index.html',contex)