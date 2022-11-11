from django.db import models
from django.utils import timezone


class ToDO(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    state = models.BooleanField(default=True)
    created_at = models.DateField(null=True,blank=True,default=timezone.now)
    updated_at =models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name
