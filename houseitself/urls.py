from django.conf.urls import url

from . import views

urlpatterns = [
               
               url(r'^(?P<doll_id>[0-9]+)$', views.showdoll, name='show_doll'),
               url(r'^$', views.index, name='index'),
               url(r'^add_doll', views.add_doll, name='add_doll'),
               url(r'^showdolly', views.showdolly, name='showdolly'),
               url(r'^dragdrop', views.dragdrop, name='dragdrop')
               ]
