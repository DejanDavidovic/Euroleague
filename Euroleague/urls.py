
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Home/', include('Home.urls')),
    url(r'^standings/', include('standings.urls')),
    url(r'^stats/', include('stats.urls')),
    url(r'^roster/', include('roster.urls')),
    url(r'^players/', include('players.urls')),
    url(r'^videos/', include('videos.urls')),
    url(r'^About/', include('About.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)