from django.db import models
from django.contrib.auth.models import User


class Experiment(models.Model):
    AGE = (
              (0,'0'),(17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, 23), (24, '24'),
    (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'))
    LANGUAGE = (('None', 'None'),('English', 'English'), ('French', 'French'), ('German', 'German'), ('Korean', 'Korean'))
    EDUCATION = (('None', 'None'),('School', 'School'), ('College', 'College'), ('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, symmetrical=False, blank=True, related_name='students')
    accepted = models.ManyToManyField(User, symmetrical=False, blank=True, related_name='accepted')
    name = models.CharField(unique=True, max_length=128)
    details = models.CharField(max_length=600)
    price = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    num_req = models.IntegerField(default=0)
    num_current = models.IntegerField(default=0)
    age_req = models.IntegerField(choices=AGE, default=0)
    lang_req = models.CharField(choices=LANGUAGE, max_length=128)
    ed_req = models.CharField(choices=EDUCATION, max_length=128)
    expr_full = models.BooleanField(default=False)
    expr_done = models.BooleanField(default=False)
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

