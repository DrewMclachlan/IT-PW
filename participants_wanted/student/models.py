from django.db import models
from django.contrib.auth.models import User
from experimenter.models import Experiment

class Demsurv(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=128)
    age = models.CharField(max_length=128)
    language = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    education = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class StudentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bidexpr = models.ManyToManyField(Experiment, blank=True, related_name='bidexpr')
    currentexpr = models.ManyToManyField(Experiment, blank=True, related_name='currentexpr')
    pastexpr = models.ManyToManyField(Experiment, blank=True, related_name='pastexpr')

    def __str__(self):
        return self.user.username

#Superuser
#uname: ITcw
#p: us

