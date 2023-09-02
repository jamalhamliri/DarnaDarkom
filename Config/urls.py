"""
URL configuration for Config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import app.views
from Config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
path('', app.views.home, name="home"),
path('about_us/', app.views.about_us, name="about_us"),
path('contact/', app.views.contact, name="contact"),
path('security/', app.views.security, name="security"),
    path('', include('users.urls', namespace='users')),
path('', include('annonce.urls', namespace='annonce')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

