from django.urls import path, include
from outlet import views
urlpatterns = [
    path('items/search', views.search),
    path('outlets/', views.OutletsList.as_view()),
    path('items/<slug:outlet_slug>/', views.ItemsList.as_view()),
] 