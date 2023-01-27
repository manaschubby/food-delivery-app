from django.urls import path, include
from outlet import views
urlpatterns = [
    path('outlets/', views.OutletsList.as_view()),
] 