from django.db import models
from django.contrib.auth.models import User


class ExprProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    school = models.CharField(max_length=128)
    webpage = models.CharField(max_length=128, blank=True)
    schoolemail = models.CharField(max_length=128)
    publicnumber = models.CharField(max_length=128)
    isexpr = models.CharField(max_length=128, default=True)

    def __str__(self):
        return self.user.username


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
