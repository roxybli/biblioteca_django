from django import forms
from libros.models import *

class LibroForm(forms.ModelForm):
	class Meta:
		model = Libro

		fields= [
			'titulo',
			'fecha_publicacion',
			'descripcion',
			'autores',
			'editor',
			'portada',
			'precio',
		]

		labels ={
			'titulo': 'Titulo',
			'fecha_publicacion': 'Fecha de Publicacion',
			'descripcion': 'Descripcion',
			'autores': 'Autores',
			'editor': 'Editorial',
			'portada': 'Portada',
		}

		widgets = {
			'titulo': forms.TextInput(attrs={'class': 'form-control'}),
			'fecha_publicacion': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
			'autores' : forms.CheckboxSelectMultiple(),
			'editor': forms.Select(attrs={'class': 'form-control'}),
			'precio': forms.TextInput(attrs={'class': 'form-control'}),
		}

class AutorForm(forms.ModelForm):
	class Meta:
		model = Autor

		fields=[
			'nombre',
			'apellido',
			'correo',
		]

		widgets={
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control'}),
			'correo': forms.TextInput(attrs={'class': 'form-control'}),
		}

class EditorForm(forms.ModelForm):
	class Meta:
		model = Editor

		fields = [
			'nombre',
			'domicilio',
			'ciudad',
			'pais',
			'web',
		]

		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
			'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
			'pais': forms.TextInput(attrs={'class': 'form-control'}),
			'web': forms.TextInput(attrs={'class': 'form-control'}),
		}