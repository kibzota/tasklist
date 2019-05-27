from django.db import models

# Create your models here.
class Tasks(models.Model):

    dt_create = models.DateTimeField(autonow=True)
    dt_update = models.DateTimeField(autonow=True)
    status = models.IntegerField()
    title = models.CharField(max_length=60)
    message = models.TextField()
