from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Dust(models.Model):
    '''everything is just dust in the solar wind'''
    huck = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, db_index=True)
    text = models.TextField(blank=True, db_index=True)
