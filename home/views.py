from django.shortcuts import render
from home.models import Category,Service

# Create your views here.

def home(request):
    """ Default view for the root """
    categories=Category.objects.all()
       
    return render(request,'home/home.html',{'categories':categories})


def category_view(request,category):
    
    services=Service.objects.filter(pk=category)

    return render(request,'home/category.html',{'services':services})

