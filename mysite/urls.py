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
    url(r'^applications/(?P<username>[\w]+)/$', views.ApplicationList.as_view()),
    url(r'^backupsets/(?P<username>[\w]+)/$', views.BackupsetsList.as_view()),
    url(r'^backup-operations/(?P<username>[\w]+)/$', views.BackupoperationsList.as_view()),
    url(r'^backup-operations/(?P<username>[\w]+)/latest_backup/$', views.LatestBackupOperation.as_view()),
    url(r'^backupfile-exception/', views.BackupfileExceptionsList.as_view()),
    url(r'^backuparchives-raw/(?P<username>[\w]+)/$', views.BackuparchivesRawList.as_view()),
    url(r'^backuparchives/', views.BackuparchivesList.as_view()),
    url(r'^exclusion-list/(?P<username>[\w]+)/$', views.ExclusionList.as_view()),
    url(r'^backup-recovery/(?P<username>[\w]+)/$', views.BackupRecovery.as_view()),
    url(r'^backup-reports/(?P<username>[\w]+)/$', views.BackupReportsNoOfFiles.as_view()),
    url(r'^backup-reports-volume/(?P<username>[\w]+)/$', views.BackupReportsVolume.as_view()),
    url(r'^admin-reports-operations/', views.AdminReportsOperations.as_view()),
    url(r'^admin-reports-volume/', views.AdminReportsVolume.as_view()),
    url(r'^get-username/(?P<appname>[\w]+)/$', views.UsernameFromApplication.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
