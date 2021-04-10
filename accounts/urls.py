from django.contrib.auth import views as auth_views
from django.urls import path, include
import accounts.views as views

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('register/', views.register_view, name='register'),
    path('user/<str:username>', views.user_view, name='user'),
]