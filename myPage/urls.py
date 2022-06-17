from django.urls import path
from django.conf.urls.static import static
from config import settings

from . import views

app_name = 'myPage'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/download/<int:post_id>', views.audio_download, name='audio_download'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)