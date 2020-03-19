from django.db import models
from django.contrib.auth.models import User
from experimenter.models import Experiment

class Demsurv(models.Model):
    SEX = (('M', 'Male'), ('F', 'Female'), ('N', 'Others'))
    AGE = (('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'))
    LANGUAGE = (('E', 'English'), ('F', 'French'), ('G', 'German'), ('K', 'Korean'))
    COUNTRY = (('uk', 'UK'), ('eu', 'EU'), ('others', 'Others'))
    EDUCATION = (('s', 'School'), ('c', 'College'), ('u', 'Undergraduate'), ('p', 'Postgraduate'))


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=128, choices=SEX)
    age = models.CharField(max_length=128, choices=AGE)
    language = models.CharField(max_length=128, choices=LANGUAGE)
    country = models.CharField(max_length=128, choices=COUNTRY)
    education = models.CharField(max_length=128, choices=EDUCATION)
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

