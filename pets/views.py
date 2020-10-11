from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from pets.models import Pet


def pet_all(request):
    return render(request, 'pets/pet_list.html')


def pet_detail(request):
    pet = Pet.objects.all()
    return HttpResponse('ok')



