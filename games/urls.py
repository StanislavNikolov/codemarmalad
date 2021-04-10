from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import games.views as views

urlpatterns = [
    path('', views.index, name='home'),
    path('upload/', views.upload, name='upload'),
    path('game/<int:pk>', views.game, name='game'),
    path('game/<int:pk>/<slug:slug>', views.game, name='game'), # slug is ignored, it just makes the urls more descriptive for humans
    path('vote/<int:pk>/<str:vtype>', views.vote, name='vote'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
