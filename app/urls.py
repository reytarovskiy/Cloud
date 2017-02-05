from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.default, name='default'),
    url(r'^catalog$', views.catalog, name='catalog'),
    url(r'^upload$', views.upload, name='upload'),
]