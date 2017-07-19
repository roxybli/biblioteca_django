from django.conf.urls import url
from libros.views import *


urlpatterns = [
    url(r'^$', index, name='inicio'),
    url(r'^librosExistentes$', libros_existentes, name='librosExistentes'),
    url(r'^autores$', autores, name='autores'),
    url(r'^editoriales$', editoriales, name='editoriales'),
    url(r'^insertarLibro$', insertar_libro, name='insertarLibro'),
    url(r'^eliminarLibro/(?P<id_libro>\d+)/$', eliminar_libro, name='eliminarLibro'),
    url(r'^actualizarLibro/(?P<id_libro>\d+)/$', actualizar_libro, name='actualizarLibro'),
    url(r'^buscarLibro$', buscarL, name='buscarLibro'),
    url(r'^verLibro/(?P<id_libro>\d+)$', ver_libro, name='verLibro'),
    url(r'^buscarLibro/resultadoLibro$', buscar_libro, name='resultadoLibro'),
    url(r'^autores/agregarAutor$', agregar_autor, name='agregarAutor'),
    url(r'^autores/aliminarAutor/(?P<id_autor>\d+)/$', eliminar_autor, name='eliminarAutor'),
    url(r'^autores/actualizarAutor/(?P<id_autor>\d+)/$', actualizar_autor, name='actualizarAutor'),
    url(r'^editoriales/agregarEditor$', agregar_editor, name='agregarEditorial'),
    url(r'^editoriales/actualizarEditor/(?P<id_editor>\d+)/$', actualizar_editor, name='actualizarEditor'),
    url(r'^editoriales/eliminarEditor/(?P<id_editor>\d+)/$', eliminar_editor, name='eliminarEditor'),
]
