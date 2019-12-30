from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class team(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,default=None,unique=True)
    name1 = models.TextField(default='', null=True )
    name2 = models.TextField(default='', null=True )
    name3 = models.TextField(default='', null=True )
    name4 = models.TextField(default='', null=True )
    phone = models.TextField(default='', null=True )
    count=models.IntegerField(default=0)

    @classmethod
    def create(cls, uname):
        tp = cls(username = uname)
        return tp


class submissions(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,default=None,unique=True)
    sublink = models.TextField(default='', null=True )
    @classmethod
    def create(cls, uname):
        tp = cls(username = uname)
        return tp

class wifi(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,default=None,unique=True)
    pawd = models.TextField(default='', null=True )
    @classmethod
    def create(cls, uname):
        tp = cls(username = uname)
        return tp

class cafe(models.Model):
    food = models.TextField(default='', null=True )
    brand = models.TextField(default='', null=True )
    category = models.TextField(default='', null=True )
    quantity = models.IntegerField(default=0, null=True )
    time = models.TimeField(null=True)
    @classmethod
    def create(cls, foodname):
        tp = cls(food = foodname)
        return tp

class judges(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    score = models.IntegerField(default=0)
    tname = models.ForeignKey(submissions, on_delete=models.CASCADE,default=None)

    class Meta:
        unique_together = (("username", "tname"),)

    @classmethod
    def create(cls, uname):
        tp = cls(username = uname)
        return tp
