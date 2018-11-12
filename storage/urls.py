from django.conf.urls import url

from django_project import settings
from . import views

urlpatterns = [
    url(r'^$', views.main_menu, name='main_menu_url'),
    url(r'^upload/$', views.upload_file, name='upload_file_url'),
    url(r'^download/$', views.download_file, name='download_file_url'),
    url(r'^delete/$', views.delete_file, name='delete_file_url'),
]