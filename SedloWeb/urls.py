"""
URL configuration for SedloWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from SedloWebApp import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
    path('', views.main_page, name='main_page'),
    path('zapisy/', views.zapisy_z_testovani, name='zapisy_z_testovani'),
    path('programy/', views.programy, name='programy'),
    path('telegramy/', views.telegramy, name='telegramy'),
    path('ostatni/', views.ostatni, name='ostatni'),
    path('3d-models/', views.models_3d, name='models_3d'),  # URL for the "3D models" page
    path('programy/', views.programy, name='programy'),
    path('programy/<int:file_id>/', views.file_detail, name='file_detail'),
    path('3d-models/<int:model_id>/', views.model_detail, name='model_detail'),  # Detail page URL
    path('telegramy/<int:telegram_id>/', views.telegram_detail, name='telegram_detail')
]
# Add this at the bottom of your urls.py file
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)