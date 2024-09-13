from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    titulo=models.CharField(max_length=100)
    contenido= models.TextField()
    fecha_posteo= models.DateTimeField(default=timezone.now)
    autor= models.ForeignKey(User, on_delete=models.CASCADE) #clave foranea
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# Create your models here.
