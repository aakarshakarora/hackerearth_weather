import json

from django.db import models


class Record(models.Model):
    date = models.DateField()
    lat = models.FloatField()
    lon = models.FloatField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    _temperatures = models.CharField(max_length=255)

    @property
    def temperatures(self): return json.loads(self._temperatures)

    @temperatures.setter
    def temperatures(self, value):
        self._temperatures = json.dumps(value)
