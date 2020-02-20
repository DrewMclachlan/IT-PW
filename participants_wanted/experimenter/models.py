from django.db import models

class Experiment(models.Model):
    students = models.ManyToManyField(User, blank=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# Create study:
# experiment title
# experiment details
# price of bid
# start date, end date
# accepting bids y/n
# num participants req.
# num participants so far
# link to more information
