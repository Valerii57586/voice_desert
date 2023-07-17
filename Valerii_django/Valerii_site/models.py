from django.db import models

class Car(models.Model):
    text = models.TextField()
    name = models.TextField()
    age = models.PositiveBigIntegerField()
    skill = models.TextField()