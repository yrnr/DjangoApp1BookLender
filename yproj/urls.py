"""yproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import home, about
from rapp import views as rapp_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', rapp_views.register, name='register'),
    path('profile/', rapp_views.profile, name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='rapp/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='rapp/logout.html'), name='logout'),
    path('home/', home, name='project-home'),
    path('home/about/', about, name='project-about'),
    path('', include('yapp.urls')),
]

if settings.DEBUG : # for production environemnt: https://docs.djangoproject.com/en/4.0/howto/static-files/
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)