from django.urls import path

from pets import views

urlpatterns = [
    path('', views.list_pets, name='pets'),
    path('details/<int:pk>/', views.show_pet_details, name='details'),
    path('like/<int:pk>/', views.like_pet, name='like pet'),
]
