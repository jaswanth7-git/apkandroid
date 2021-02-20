from django.db.models import query
from django.shortcuts import render,HttpResponse
from . models import Apk


def index(request):
    a = Apk.objects.all
    
    return render(request,'app/index.html', {'a':a})

def search(request):
    query = request.GET['query']
    
    b = Apk.objects.filter(name__icontains = query)
    return render(request,'app/search.html',{'b':b})
    

