
from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
   path('index.html',views.home,name="home"),
   path('profile.html',views.profile,name="profile"),
   path('add_stock.html',views.add_stock,name="add_stock"),
   path('Businessman_dashboad.html',views.Businessman_dashboad,name="Businessman_dashboad"),
   path('driver_dashboard.html',views.driver_dashboard,name="driver_dashboard"),
   path('driver_profile.html',views.driver_profile,name="driver_profile"),
   path('complents.html',views.complents,name="complents"),
   path('pickup_drop.html',views.pickup_drop,name="pickup_drop"),

]








