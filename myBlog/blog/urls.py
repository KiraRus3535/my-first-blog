from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog import admin
from django.conf.urls import include
 
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.single, name='single'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += staticfiles_urlpatterns()

    if settings.MEDIA_ROOT:
 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
# Эта строка опциональна и будет добавлять url'ы только при DEBUG = True
 
