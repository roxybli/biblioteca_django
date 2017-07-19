from django.shortcuts import render, redirect
from libros.models import *
from libros.forms import LibroForm, AutorForm, EditorForm

# Create your views here.

def index(request):
	libros = Libro.objects.all()
	contexto = {'libros': libros}
	return render(request, 'libros/index.html', contexto)

def libros_existentes(request):
	libros = Libro.objects.all()
	contexto = {'libros': libros}
	return render(request, 'libros/libros_existentes.html', contexto)

def autores(request):
	autores = Autor.objects.all()
	contexto = {'autores': autores}
	return render(request, 'libros/autores.html', contexto)

def editoriales(request):
	editorial = Editor.objects.all()
	contexto = {'editorial': editorial}
	return render(request, 'libros/editoriales.html', contexto)

def buscarL(request):
	return render(request, 'libros/buscar_libro.html')

def buscar_libro(request):
	busqueda = request.POST['libro']
	libros = Libro.objects.filter(titulo__contains=busqueda)
	contexto = {'libros': libros, 'busqueda': busqueda}
	return render(request, 'libros/resultado_libro.html', contexto,)

def insertar_libro(request):
	if request.method =='POST':
		form = LibroForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('biblioteca:insertarLibro')
	else:
		form = LibroForm()
	return render(request, 'libros/insertar_libro.html', {'form': form})

def eliminar_libro(request, id_libro):
	libro = Libro.objects.get(id=id_libro)
	if request.method=="POST":
		libro.delete()
		return redirect('biblioteca:librosExistentes')
	return render(request, 'libros/eliminar_libro.html', {'libro': libro})

def actualizar_libro(request, id_libro):
	libro = Libro.objects.get(id=id_libro)
	if request.method== 'GET':
		form = LibroForm(instance=libro)
	else:
		form = LibroForm(request.POST, request.FILES, instance=libro)
		if form.is_valid():
			form.save()
		return redirect('biblioteca:librosExistentes')
	return render(request, 'libros/insertar_libro.html', {'form': form})

def agregar_autor(request):
	if request.method == 'POST':
		form = AutorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('biblioteca:agregarAutor')
	else:
		form = AutorForm()
	return render(request, 'libros/agregar_autor.html', {'form': form})

def eliminar_autor(request, id_autor):
	autor = Autor.objects.get(id = id_autor)
	if request.method == 'POST':
		autor.delete()
		return redirect('biblioteca:autores')
	return render(request, 'libros/eliminar_autor.html')

def actualizar_autor(request, id_autor):
	autor = Autor.objects.get(id=id_autor)
	if request.method == "GET":
		form = AutorForm(instance=autor)
	else:
		form = AutorForm(request.POST, instance=autor)
		if form.is_valid():
			form.save()
			return redirect('biblioteca:autores')
	return render(request, 'libros/agregar_autor.html', {'form': form})

def agregar_editor(request):
	if request.method == 'POST':
		form = EditorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('biblioteca:editoriales')
	else:
		form = EditorForm()
	return render(request, 'libros/agregar_editorial.html', {'form': form})

def eliminar_editor(request, id_editor):
	editor = Editor.objects.get(id=id_editor)
	if request.method == 'POST':
		editor.delete()
		return redirect('biblioteca:editoriales')
	return render(request, 'libros/eliminar_editor.html', {'editor': editor})

def actualizar_editor(request, id_editor):
	editor = Editor.objects.get(id=id_editor)
	if request.method == 'GET':
		form = EditorForm(instance=editor)
	else:
		form = EditorForm(request.POST, instance=editor)
		if form.is_valid():
			form.save()
			return redirect('biblioteca:editoriales')
	return render(request, 'libros/agregar_editorial.html', {'form': form})

def ver_libro(request, id_libro):
	libro = Libro.objects.get(id=id_libro)
	contexto = {'libro': libro}
	return render(request, 'libros/libro.html', contexto)