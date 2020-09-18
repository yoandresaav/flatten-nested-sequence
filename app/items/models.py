from django.db import models
from django.contrib.postgres.fields import ArrayField

class Item(models.Model):
    result = ArrayField(models.IntegerField())

    def __str__(self):
        return f'{self.result}'
