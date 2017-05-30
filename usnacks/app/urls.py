from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.busqueda, name='busqueda'),

    url(r'^logged/', views.busquedalogeado, name='busquedalogeado'),

    url(r'^$', views.index, name='index'),

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^create_user/$', views.create_user, name='create_user'),

    url(r'^login/$', views.login, name='login'),
    # ex: /polls/5/
    url(r'^(producto)/(?P<producto_id>[a-z]+)/$', views.producto, name='producto'),
    # ex: /polls/5/results/
    url(r'^(vendedor)/(?P<vendedor_id>[a-z]+)/$', views.vendedor, name='vendedor'),



]

STATIC_URL = '/static/'
