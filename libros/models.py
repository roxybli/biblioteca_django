from django.db import models

# Create your models here.
class Autor(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.EmailField()

	def __str__(self):
		return '%s %s'%(self.nombre, self.apellido)


class Editor(models.Model):
	nombre = models.CharField(max_length=50)
	domicilio = models.CharField(max_length=100)
	ciudad = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	web = models.URLField()

	def __str__(self):
		return self.nombre


class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	fecha_publicacion = models.DateField()
	descripcion = models.TextField()
	autores = models.ManyToManyField(Autor)
	editor = models.ForeignKey(Editor)
	portada = models.FileField()
	precio = models.FloatField()
	
	def __str__(self):
		return self.titulo