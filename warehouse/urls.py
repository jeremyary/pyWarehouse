from django.conf.urls import patterns, url

from warehouse import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<order_id>\d+)/$', views.details, name='details'),
    url(r'^place_order/', views.place_order, name='place_order'),
)
