from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Notebook(models.Model):
    model_name = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    price = models.FloatField(max_length=50)
    notebook_url = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    site = models.CharField(max_length=500)
    marka = models.CharField(max_length=500)
    cpu_type = models.CharField(max_length=500)
    cpu_model = models.CharField(max_length=500)
    memory_capacity = models.CharField(max_length=500)
    screen_size = models.CharField(max_length=500)
    dos = models.CharField(max_length=500)
    disc_capacity = models.CharField(max_length=500)
    disc_type = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title

