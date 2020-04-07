from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog import admin
from django.conf.urls import include

app_name = 'post'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:post_id>/', views.single, name='single'),
    path('<int:post_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    # path('clips/', views.clips, name = 'clips')
]
