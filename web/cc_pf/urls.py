from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_apikey$', views.add_apikey, name='add_apikey'),
]
