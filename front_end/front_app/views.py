from django.shortcuts import render,redirect


# Create your views here.
def home(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')

def add_stock(request):
    return render(request,'add_stock.html')


    