
from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
   path('index.html',views.home,name="home"),
   path('profile.html',views.profile,name="profile"),
   path('add_stock.html',views.add_stock,name="add_stock"),
]




