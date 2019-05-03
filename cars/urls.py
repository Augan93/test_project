from django.urls import path
from . import views


app_name = 'cars'

urlpatterns = [
    path('cars/', views.CarListCreateView.as_view(), name='car-create-list'),
    path('cars/<int:pk>/', views.CarRetrieveView.as_view(), name='car-retrieve'),
    path('cars/<int:pk>/edit/', views.CarUpdateView.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car-delete'),
]