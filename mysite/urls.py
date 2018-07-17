"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from hadoop_backup_catalog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^metadata/', views.MetadataList.as_view()),
    url(r'^applications/(?P<appid>[\d]+)/$', views.ApplicationList.as_view()),
    url(r'^backupsets/(?P<appid>[\d]+)/$', views.BackupsetsList.as_view()),
    url(r'^backup-operations/(?P<appid>[\d]+)/$', views.BackupoperationsList.as_view()),
    url(r'^backupfile-exception/', views.BackupfileExceptionsList.as_view()),
    url(r'^backuparchives-raw/(?P<appid>[\d]+)/$', views.BackuparchivesRawList.as_view()),
    url(r'^backuparchives/', views.BackuparchivesList.as_view()),
    url(r'^exclusion-list/', views.ExclusionList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
