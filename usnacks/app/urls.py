from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.busqueda, name='busqueda'),

    url(r'^logged/', views.busquedalogeado, name='busquedalogeado'),

    url(r'^$', views.index, name='index'),

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^login/$', views.login, name='login'),
    # ex: /polls/5/
    url(r'^(producto)/(?P<producto_id>[a-z]+)/$', views.producto, name='producto'),
    # ex: /polls/5/results/
    url(r'^(vendedor)/(?P<vendedor_id>[a-z]+)/$', views.vendedor, name='vendedor'),
    url(r'^(vendedor)/(?P<vendedor_id>[a-z]+)/(?P<usuario_id>[a-zA-z]+)/$', views.Vistavendedor, name='usuario')



]

STATIC_URL = '/static/'
