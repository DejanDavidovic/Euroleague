from django.conf.urls import url
from . import views

app_name = 'videos'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^videos/add/$', views.AddVideo.as_view(), name='add-video'),
    url(r'^videos/(?P<pk>[0-9]+)/delete/$', views.DeleteVideo.as_view(), name='delete-video'),

]