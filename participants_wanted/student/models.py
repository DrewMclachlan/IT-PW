from django.db import models
from django.contrib.auth.models import User


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



class Experiment(models.Model):
    students = models.ManyToManyField(User, blank=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

#Superuser
#uname: ITcw
#p: us

