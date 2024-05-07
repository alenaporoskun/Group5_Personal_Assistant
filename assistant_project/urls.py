"""
URL configuration for assistant_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from weather.views import weather, WeatherView, weather_view
from news_scraping import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacts.urls')),
    path('users/', include('users.urls')),
    path('notes/', include('notes.urls')),
    path('files/', include('files.urls')),
    path('weather/', WeatherView.as_view(), name='weather'),
    path('news/', views.news_list, name='news'),
]