from django.db import models

class FGroup(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    groupname = models.CharField(max_length=15, default='')
    noofphotos = models.IntegerField(default=0)

class FUser(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    ownername = models.CharField(max_length=20, unique=True)


class FPhoto(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    owner = models.CharField(max_length=15)
    secret = models.CharField(max_length=15)
    server = models.CharField(max_length=4)
    farm = models.IntegerField()
    title = models.CharField(max_length=50)
    ispublic = models.IntegerField()
    isfriend = models.IntegerField()
    isfamily = models.IntegerField()
    ownername = models.CharField(max_length=20)
    dateadded = models.CharField(max_length=15)
    groupid = models.CharField(max_length=15)
