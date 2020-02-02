

from django.db import models
from  .choices import *


# Create your models here.





class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    place = models.CharField(max_length=75)
    reason = models.CharField(max_length=75)
    exit_date = models.DateField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    out_time = models.DateTimeField(auto_now_add=True)
    degree = models.CharField(max_length=75)
    branch = models.CharField(max_length=75)
    year = models.IntegerField()
    block_name = models.CharField(max_length=75)
    room_no = models.IntegerField()
    rt_name = models.CharField(max_length=75)
    check_with = models.CharField(max_length=75)
    pass_available = models.CharField(max_length=75)
    def __str__(self):
        return self.name




