from django.db import models


class Lunch(models.Model):
    submitter = models.CharField(max_length=63)
    food = models.CharField(max_length=255)
