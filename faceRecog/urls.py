"""faceRecog re_path Configuration

The `re_pathpatterns` list routes re_paths to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/re_paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a re_path to re_pathpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a re_path to re_pathpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another re_pathconf
    1. Import the include() function: from django.conf.re_paths import re_path, include
    2. Add a re_path to re_pathpatterns:  re_path(r'^blog/', include('blog.re_paths'))
"""
from django.urls import re_path, include
from django.contrib import admin
from faceRecog import views as app_views

urlpatterns = [
    re_path(r'^$', app_views.index),
    re_path(r'^error_image$', app_views.errorImg),
    re_path(r'^create_dataset$', app_views.create_dataset),
    re_path(r'^trainer$', app_views.trainer),
    re_path(r'^eigen_train$', app_views.eigenTrain),
    re_path(r'^detect$', app_views.detect),
    re_path(r'^detect_image$', app_views.detectImage),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^records/', include('records.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
]
