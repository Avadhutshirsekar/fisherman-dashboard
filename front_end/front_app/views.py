from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')

def add_stock(request):
    return render(request,'add_stock.html')

def fertilizer_company_dashboard(request):
    fish_list = [
        {'name': 'Salmon', 'location': 'Norway', 'quantity': '10 kg', 'price': '1000 rs', 'address': 'Oslo, Norway', 'phone': '+47 123 456 78'},
        {'name': 'Tuna', 'location': 'Japan', 'quantity': '5 kg', 'price': '1500 rs', 'address': 'Tokyo, Japan', 'phone': '+81 123 456 78'},
        {'name': 'Cod', 'location': 'Iceland', 'quantity': '8 kg', 'price': '800 rs', 'address': 'Reykjavik, Iceland', 'phone': '+354 123 456'},
    ]
    return render(request, 'fertilizer_company_dashboard.html', {'fish_list': fish_list})

def update_company(request):
    return render(request, 'update_company.html')

def company_contact(request):
    return render(request,'company_contact.html') 

def add_requirement(request):
    return render(request, 'add_requirement.html')

def view_my_order(request):
    return render(request, 'view_my_order.html')

