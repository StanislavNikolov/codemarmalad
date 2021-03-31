from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import games.views as views

urlpatterns = [
    path('', views.index, name='home'),
    path('upload/', views.upload, name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
