"""e_mela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from app import views as app_views
from login import views as login_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', app_views.home, name='home'),
    path('automobiles/', app_views.automobiles, name='automobiles'),
    path('electronics/', app_views.electronics, name='electronics'),
    path('restaurants/', app_views.restaurants, name='restaurants'),
    path('sports/', app_views.sports, name='sports'),
    path('admin/', admin.site.urls),
    path('seller/', include('seller.urls')),
    path('login/', include('login.urls')),
    path('user_logout',login_views.user_logout, name='logout')
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
