from django.shortcuts import render,redirect


# Create your views here.
def home(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')

def add_stock(request):
    return render(request,'add_stock.html')

def Businessman_dashboad(request):
    fish_list = [
        {'name': 'Salmon', 'location': 'Norway', 'quantity': '10 kg', 'price': '1000 rs', 'address': 'Oslo, Norway', 'phone': '+47 123 456 78'},
        {'name': 'Tuna', 'location': 'Japan', 'quantity': '5 kg', 'price': '1500 rs', 'address': 'Tokyo, Japan', 'phone': '+81 123 456 78'},
        {'name': 'Cod', 'location': 'Iceland', 'quantity': '8 kg', 'price': '800 rs', 'address': 'Reykjavik, Iceland', 'phone': '+354 123 456'},
    ]
    return render(request, 'Businessman_dashboad.html', {'fish_list': fish_list})
    

def driver_dashboard(request):
   


    # Sample data for demonstration purposes
    order_list = [
        {
            'pickup_address': '123 Fisherman Street, Harbor Town',
            'drop_address': '789 Fertilizer Ave, Green Valley',
            'about': 'Dead fish and waste for fertilization',
            'phone': '555-1234'
        },
        {
            'pickup_address': '456 Sea Lane, Oceanview',
            'drop_address': '321 Compost Blvd, AgriCity',
            'about': 'Fish waste for composting',
            'phone': '555-5678'
        },
        {
            'pickup_address': '789 Dockside Rd, Seaport',
            'drop_address': '654 Plant Food Dr, Growtown',
            'about': 'Dead fish for plant food production',
            'phone': '555-9876'
        }
    ]

    # Render the template with the order list
    return render(request, 'driver_dashboard.html', {'order_list': order_list})
    

def driver_profile(request):
    return render(request,'driver_profile.html')

def complents(request):
    return render(request,'complents.html') 

def pickup_drop(request):
    return render(request, 'pickup_drop.html')


