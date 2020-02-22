from django.db import models

class Experiment(models.Model):
    students = models.ManyToManyField(User, blank=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class CreateExpr(models.Model):
    title = models.CharField(max_length=128)
    details = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
    bid_accept = models.BooleanField(default=False)
    num_req = models.IntegerField(default=0)
    num_current = models.IntegerField(default=0)

    def __str__(self):
        return self.name
