"""omnium_lmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from pages.views import home_view, stats, welcome, user_stats, lmt_admin, save_changes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('stats', stats),
    path('welcome', welcome),
    path('userstats', user_stats),
    path('lmt_admin', lmt_admin),
    path('save_changes/', save_changes)
]
