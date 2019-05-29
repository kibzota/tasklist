from django.db import models
from . import helper

# Create your models here.
class Tasks(models.Model):

    status_choices = (
        (helper.ATIVO,"Ativo"),
        (helper.EMANDAMENTO,"Em andamento"),
        (helper.CONCLUIDO, "Finalizada")
    )

    dt_create = models.DateTimeField(auto_now=True)
    dt_update = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=status_choices)
    title = models.CharField(max_length=60, blank=True)
    message = models.TextField()

    class Meta:
        ordering = ('dt_create',)

