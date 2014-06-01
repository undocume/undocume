from django.shortcuts import render
from home.models import Category

# Create your views here.

def home(request):
    """ Default view for the root """
    categories=Category.objects.all()
       
    return render(request,'home/home.html',{'categories':categories})
