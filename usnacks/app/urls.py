from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.busqueda, name='busqueda'),
    # ex: /polls/5/
    url(r'^(producto)/(?P<producto_id>[a-z]+)/$', views.producto, name='producto'),
    # ex: /polls/5/results/
    url(r'^(vendedor)/(vendedor)/(?P<vendedor_id>[a-z]+)/$', views.vendedorPorVendedor, name='vendedor'),
    # ex: /polls/5/vote/
    url(r'^vendedor/alumno/(?P<vendedor_id>[a-z]+)/$', views.vendedorPorAlumno, name='alumno'),
]