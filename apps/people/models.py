from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    # photo
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    location_lat = models.IntegerField(null=True, blank=True)
    location_long = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
