"""
URL configuration for cs415 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from cs415 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.Login.as_view()),
    path("users/", views.UserAPIView.as_view()),
    path("users/user/<int:id>", views.GetSingleUserAPIView.as_view()),
    path("addresses/", views.UserAddressAPIView.as_view()),
    path("driver_licenses/", views.DriverLicenseAPIView.as_view()),
    path("vehicles/", views.VehicleAPIView.as_view()),
    path("vehicles/vehicle/<int:id>", views.GetSingleVehicleAPIView.as_view()),
    path("parking/", views.ParkingInfoAPIView.as_view()),
]
