from django.contrib import admin
# Register your models here.
from libros.models import *
# Register your models here.
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Editor)
