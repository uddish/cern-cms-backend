from django.db import models


class applications(models.Model):
    appid = models.IntegerField()
    appname = models.CharField(max_length=50)
    hdfs_root_dir = models.CharField(max_length=50)
    hdfs_cluster = models.CharField(max_length=50)
    appowner = models.CharField(max_length=50)
    appowner_email = models.CharField(max_length=50)
    servicecontact = models.CharField(max_length=50)
    servicecontact_email = models.CharField(max_length=50)
    hdfs_stage = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.appname

class metadata(models.Model):
    hdfs_cluster = models.CharField(max_length=50)
    backupqueue = models.CharField(max_length=50)
    backupsetsize = models.BigIntegerField()
    namenode = models.CharField(max_length=50)

    def __str__(self):
        return self.namenode

class backupsets(models.Model):
    appid = models.IntegerField()
    boid = models.IntegerField()
    bsid = models.IntegerField()
    backupset_name = models.CharField(max_length=256)
    status = models.CharField(max_length=24)
    num_files = models.IntegerField()

    def __str__(self):
        return self.appid
