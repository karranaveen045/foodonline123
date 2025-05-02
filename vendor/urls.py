from django.urls import path,include
from . import views

from accounts import views as AccountViews

#from foodonline.foodonline_main.urls import urlpatterns

urlpatterns = [
    path('',AccountViews.vendorDashboard,name='vendor'),
    path('profile/',views.vprofile,name='vprofile'),

]
