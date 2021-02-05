"""Django_ChromoGraph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic import TemplateView

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'ChromoGraph/static/media')
INDEX_ROOT = os.path.join(BASE_DIR, 'index')

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html'), name='home'),
    path('admin/', admin.site.urls),
    path('chromograph/', include('ChromoGraph.urls'), name='chromograph'),
    path('autos/', include('autos.urls'), name='autos'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^media/(?P<path>.*)$', serve,
            {'document_root': SITE_ROOT, 'show_indexes': True},
            name='media_path'
        ),
]