from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.hello_world, name='hello'),
    url(r'^granja/$', views.ListarGranja.as_view(), name='listar'),
    url(r'^granja/nuevo/', views.CrearGranja.as_view(), name='crear'),
    url(r'^granja/consultar/', views.ConsultarGranja.as_view(), name='consultar'),
    url(r'^granja/eliminar/', views.EliminarGranja.as_view(), name='eliminar'),
    #url(r'^granja/(?P<pk>[0-9]+)/$', views.granja_detail),
    #url(r'^granja/detalle/(?P<pk>[0-9]+)/$', views.DetalleGranja.as_view(), name='detail'),

    #url(r'^granja//', views.new_granja, name='new'),
]
