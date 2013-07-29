from __future__ import unicode_literals
from django.db import models



class Images(models.Model):
    id = models.AutoField(max_length=10L, primary_key=True)
    image = models.CharField(max_length=10000L, blank=False)
    class Meta:
        db_table = 'images'

class Mice(models.Model):
    mouse_id = models.IntegerField(max_length=11,primary_key=True)
    ko_name = models.CharField(max_length=500L, blank=True)
    genotype_short = models.CharField(max_length=500L, blank=True)
    genotype_long = models.CharField(max_length=500L, blank=True)
    gender = models.CharField(max_length=10L, blank=True)
    generation = models.CharField(max_length=10L, blank=True)
    weight = models.FloatField(null=True, blank=True)
    background = models.CharField(max_length=500L, blank=True)
    toe_number = models.CharField(max_length=10L, blank=True)
    color = models.CharField(max_length=20L, blank=True)
    clone_name = models.CharField(max_length=500L, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    record_id = models.IntegerField(null=True, blank=True)
    source = models.CharField(max_length=255L, blank=True)
    mother_key = models.IntegerField(null=True, blank=True)
    father_key = models.IntegerField(null=True, blank=True)
    litter_key = models.IntegerField(null=True, blank=True)
    genotype_med = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'mice'
