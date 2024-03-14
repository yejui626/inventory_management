"""
URL configuration for inventory_management project.

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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from inventory.views import BookList,BookDetail,AddBook,DeleteBook,UpdateBook



urlpatterns = [
    path('admin/', admin.site.urls),

    # 1) Create the /api/inventory API to list all products. Allow for query parameters to filter and sort by categories of your choice.
    path('api/inventory/', BookList.as_view(), name='inventory-list'),

    # 2) Create the /api/inventory/[product-id] API to return information only for the product chosen.
    path('api/inventory/<int:pk>/', BookDetail.as_view(), name='inventory-detail'),

    # 3) Create the following additional endpoints:
    path('api/add-inventory/', AddBook.as_view(), name='add-inventory'),
    path('api/delete-inventory/<int:pk>/', DeleteBook.as_view(), name='delete-inventory'),
    path('api/update-inventory/<int:pk>/', UpdateBook.as_view(), name='update-inventory'),
]
