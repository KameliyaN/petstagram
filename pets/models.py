from django.db import models


# Create your models here.
class Pet(models.Model):
    KIND_CHOICES = (
        ('C', 'cat'),
        ('D', 'dog'),
        ('P', 'parrot')
    )
    type = models.CharField(max_length=6, choices=KIND_CHOICES)
    name = models.CharField(max_length=6, blank=False)
    age = models.PositiveIntegerField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.URLField(blank=False)

    def __str__(self):
        return f' i am {self.name} {self.age} years old'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
