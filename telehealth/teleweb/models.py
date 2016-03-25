from __future__ import unicode_literals

from django.db import models

# Create your models here

# continuous temperature stream

class Person(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    text = models.TextField()

    def __unicode__(self):
        return unicode(self.name)

class Temperature(models.Model)
    date_time = models.DateTimeField(blank=True, null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    basal = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.temperature)
