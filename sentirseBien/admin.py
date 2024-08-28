from django.contrib import admin #admin.py
from .models import Profile, Post  # Asegúrate de importar desde el archivo models.py correctamente

admin.site.register(Profile)
admin.site.register(Post)
