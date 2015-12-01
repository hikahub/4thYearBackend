from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

class Landmarks(models.Model):
    place_name = models.CharField(max_length=120, blank=True, null=True)
    address = models.CharField(max_length=180, blank=True, null=True)
    place_desc = models.CharField(max_length=800, blank=True, null=True)
    imageUrl = models.CharField(max_length=120, blank=True, null=True)
    wiki_link = models.CharField(max_length=120, blank=True, null=True)
    opening_days = models.CharField(max_length=80, blank=True, null=True)
    admission = models.CharField(max_length=80, blank=True, null=True)
    latitude = models.CharField(max_length=120, blank=True, null=True)
    longtitude = models.CharField(max_length=120, blank=True, null=True)

    def __unicode__(self):
        return self.place_name