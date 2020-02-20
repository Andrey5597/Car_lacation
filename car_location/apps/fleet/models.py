from django.contrib.gis.db import models


class Car(models.Model):
    code = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.code}'
