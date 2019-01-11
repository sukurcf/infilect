from django.db import models


class FGroup(models.Model):
    id = models.CharField(max_length=10,primary_key=True)

class FUser(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    ownername = models.CharField(max_length=20, unique=True)
    group = models.ManyToManyField(FGroup)


class FPhoto(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    owner = models.ForeignKey(FUser, to_field='id', on_delete=models.CASCADE)
    secret = models.CharField(max_length=15)
    server = models.CharField(max_length=4)
    farm = models.IntegerField()
    title = models.CharField(max_length=50)
    ispublic = models.IntegerField()
    isfriend = models.IntegerField()
    isfamily = models.IntegerField()
    ownername = models.CharField(max_length=20)
    dateadded = models.CharField(max_length=15)
    group = models.ManyToManyField(FGroup)
