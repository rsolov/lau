from django.contrib.gis.db import models
from django.utils import timezone


class Marker(models.Model):
    type = models.CharField(max_length=100)
    location = models.PointField()
    date = models.DateTimeField(default=timezone.now)
