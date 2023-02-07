from django.urls import path
from . import views

urlpatterns = [
    path('outlets/search', views.outletSearch),
    path('items/search', views.itemSearch),
    path('outlets/', views.getOutlets),
    path('items/', views.getItems),
    path('create_order/', views.create_order.as_view()),
    path('get_customer_orders/', views.GetCustomerOrders.as_view()),
]