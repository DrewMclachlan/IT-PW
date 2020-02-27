from django.db import models
from django.contrib.auth.models import User


class Experiment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, symmetrical=False, blank=True, related_name='students')
    name = models.CharField(max_length=128)
    details = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
    num_req = models.IntegerField(default=0)
    num_current = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ExprProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    school = models.CharField(max_length=128)
    webpage = models.CharField(max_length=128, blank=True)
    schoolemail = models.CharField(max_length=128)
    publicnumber = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username

