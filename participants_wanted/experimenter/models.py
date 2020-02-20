from django.db import models

class Experiment(models.Model):
    students = models.ManyToManyField(User, blank=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# Create experiment:
# experiment title
# experiment details
# price of bid
# start date, end date
# accepting bids y/n
# num participants req.
# num participants so far
# link to more information

class CreateExpr(models.Model):
    title = models.CharField(max_length=128)
    details = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
