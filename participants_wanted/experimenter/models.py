from django.db import models

class Experiment(models.Model):
    students = models.ManyToManyField(User, blank=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
