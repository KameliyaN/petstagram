from django.urls import path

from pets import views

urlpatterns = [
    path('', views.pet_all, name='pets'),
    path('details/<int:pk>', views.pet_detail, name='details'),
]
