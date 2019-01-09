from django.db import models


class FUser(models.Model):
    nsid = models.CharField(max_length=15, primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    realname = models.CharField(max_length=30)
    location = models.CharField(max_length=200)
    iconserver = models.CharField(max_length=4)
    iconfarm = models.IntegerField()
    path_alias = models.CharField(max_length=20)


class Photo(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    owner = models.ForeignKey(FUser)
    secret = models.CharField(max_length=15)
    server = models.CharField(max_length=4)
    farm = models.IntegerField()
    dateuploaded = models.CharField(max_length=15)
    isfavourite = models.IntegerField()
    license = models.IntegerField()
    safety_level = models.IntegerField()
    rotation = models.IntegerField()
    views = models.IntegerField()


class Title(models.Model):
    id = models.ForeignKey(Photo, primary_key=True)
    content = models.CharField(max_length=100)


class Description(models.Model):
    id = models.ForeignKey(Title, primary_key=True)
    content = models.TextField()
    rel = models.TextField()


class Visibility(models.Model):
    id = models.ForeignKey(Photo, primary_key=True)
    ispublic = models.IntegerField()
    isfriend = models.IntegerField()
    isfamily = models.IntegerField()


class Dates(models.Model):
    id = models.ForeignKey(Photo, primary_key=True)
    posted = models.CharField()
    taken = models.DateTimeField()
    takengranularity = models.IntegerField()
    takenunknown = models.IntegerField()
    lastupdate = models.CharField()


class Editability(models.Model):
    id = models.ForeignKey(Photo, primary_key=True)
    cancomment = models.IntegerField()
    canaddmeta = models.IntegerField()


class Publiceditability(models.Model):
    id = models.ForeignKey(Photo, primary_key=True)
    cancomment = models.IntegerField()
    canaddmeta = models.IntegerField()


class Usage(models.Model):
    id = models.ForeignKey(Photo, primary_key=True)
    candownload = models.IntegerField()
    canblog = models.IntegerField()
    canprint = models.IntegerField()
    canshare = models.IntegerField()


class Comments(models.Model):
    id = models.ForeignKey(Photo, primary_key=True)
    content = models.IntegerField()


class Notes(models.Model):
    id = models.ForeignKey(Photo, primary_key=True)
    note = models.CharField()


class People(models.Model):
    id = models.ForeignKey(Photo, primary_key=True)
    haspeople = models.IntegerField()


class Tag(models.Model):
    id = models.SlugField(primary_key=True)
    author = models.ForeignKey(FUser)
    authorname = models.ForeignKey(FUser.username)
