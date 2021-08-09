from django.shortcuts import render

from .models import Car

# from django.urls import path,include

# def index(request):
#     return render(request, 'index.html')



def cars_list(request):
    cars = Car.objects.all()
    return render(request,'cars_list.html',{'cars':cars})

def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request,'car_detail.html',{'car':car})

def main(request):
    return render(request, 'main.html')