from django.db import models
from mysite.settings import DATE_INPUT_FORMATS

# TODO add meta class to change the table's name
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


# TODO add meta class to change the table's name
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

    class Meta:
        db_table = 'backupsets'

    def __str__(self):
        return self.appid


class backupoperations(models.Model):
    appid = models.IntegerField(null=True)
    boid = models.IntegerField(null=True)
    backup_type = models.CharField(max_length=9)
    last_backup_timestamp = models.DateField(null=True)
    num_archives = models.IntegerField(null=True)
    start_time = models.DateField(null=True)
    completion_time = models.DateField(null=True)
    elapsed_seconds = models.IntegerField(null=True)
    status = models.CharField(max_length=24)

    class Meta:
        db_table = 'backupoperations'

    def __str__(self):
        return self.appid


class backupfile_exceptions(models.Model):
    appid = models.IntegerField()
    boid = models.IntegerField()
    bsid = models.IntegerField()
    file_name = models.CharField(max_length=1000)
    file_size = models.IntegerField()
    resent = models.CharField(max_length=12)
    r_boid = models.IntegerField()
    r_bsid = models.IntegerField()
    exception_reason = models.CharField(max_length=64)
    resent_reason = models.CharField(max_length=64)

    class Meta:
        db_table = 'backupfile_exceptions'

    def __str__(self):
        return self.appid


# TODO check for the handle_raw datatype again
class backuparchives_raw(models.Model):
    appid = models.IntegerField()
    boid = models.IntegerField()
    bsid = models.IntegerField()
    file_name = models.CharField(max_length=1000)
    file_size = models.IntegerField(null=True)
    status = models.CharField(max_length=24)
    handle_raw = models.TextField(null=True)
    last_seen = models.DateField(null=True)

    class Meta:
        db_table = 'backuparchives_raw'

    def __str__(self):
        return self.appid

class backuparchives(models.Model):
    appid = models.IntegerField()
    boid = models.IntegerField()
    bsid = models.IntegerField()
    backup_type = models.CharField(max_length=9)
    file_name = models.CharField(max_length=1000)
    filename_offset = models.IntegerField()
    length = models.IntegerField()
    handle = models.CharField(max_length=256)
    backupfile_offset = models.IntegerField()
    status = models.CharField(max_length=24)

    class Meta:
        db_table = 'backuparchives'

    def __str__(self):
        return self.appid


class exclusion_list(models.Model):
    appid = models.IntegerField()
    excl_list = models.CharField(max_length=512)

    class Meta:
        db_table = 'exclusion_list'

    def __str__(self):
        return self.appid