
from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
   path('index.html',views.home,name="home"),
   path('profile.html',views.profile,name="profile"),
   path('add_stock.html',views.add_stock,name="add_stock"),
   path('fertilizer_company_dashboard',views.fertilizer_company_dashboard,name="fertilizer_company_dashboard"),
   path('update_company',views.update_company,name="update_company"),
   path('add_requirement',views.add_requirement,name="add_requirement"),
   path('view_my_order',views.view_my_order,name="view_my_order"),
   path('company_contact',views.company_contact,name="company_contact"),
]






