from django.conf.urls import url
from . import views

app_name = 'players'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^players/add/$', views.AddPlayer.as_view(), name='add-player'),
    url(r'^players/(?P<pk>[0-9]+)/delete/$', views.DeletePlayer.as_view(), name='delete-player'),


]
