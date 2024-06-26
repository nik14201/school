"""apps URL Configuration

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
from django.urls import path, include
from django.conf.urls import include, url

urlpatterns = [
    path('api/v2/admin/',       admin.site.urls),
    path('api/v1/auth/',        include('apiusers.urls')),
    path('api/v1/weather/',     include('weather.urls')),
    path('api/v1/youtube/',     include('youtube.urls')),
    path('api/v1/city/',        include('city.urls')),


    path('api/v1/country/',     include('country.urls')),
    path('api/v1/city/',        include('city.urls')),
    path('api/v1/school/',      include('school.urls')),
    path('api/v1/diary/',       include('diary.urls')),
    path('api/v1/homework/',    include('homework.urls')),
    path('api/v1/sclass/',      include('sclass.urls')),
    path('api/v1/subject/',     include('subject.urls')),
    path('api/v1/lesson/',      include('lesson.urls')),
]


