from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pokemon_images/')
    type=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name