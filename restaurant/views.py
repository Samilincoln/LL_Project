from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import MenuItem


#from django.contrib.auth.models import User







# Create your views here.
def sayHello(request):
    return HttpResponse('Hello World')

def home(request):
    return render(request, 'index.html', {})

#class MenuItemView (generics.ListCreateAPIView):

#class SingleItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):

    