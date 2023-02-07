from django.urls import path
from . import views

urlpatterns = [
    path('get_orders/', views.OrdersFetchView.as_view()),
    path('order_ready/', views.OrderReadyView.as_view()),
    path('order_delete/', views.OrderDeleteView.as_view()),
]