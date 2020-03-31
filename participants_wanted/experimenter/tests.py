from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
# Create your tests here.
from datetime import date
from experimenter.models import Experiment


class TestCreate(TestCase):

    def setUp(self):
        user = User.objects.create(username='expr')
        e = Experiment.objects.create(user=user, start_date=date.today(), end_date=date.today())
        e.name = 'test'
        e.details = 'deets'
        e.price = 1
        e.num_req = 1
        e.num_current = 0
        e.age_req = 17
        e.lang_req = 'None'
        e.ed_req = 'None'
        e.save()


    def test(self):
        Experiment.objects.get(name='test')



