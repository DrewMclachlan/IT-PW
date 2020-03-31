from django.contrib.auth.models import User
from django.test import TestCase
from datetime import date
# Create your tests here.
from student.models import Demsurv, StudentInfo
from experimenter.models import Experiment


class TestCreate(TestCase):

    def setUp(self):
        user = User.objects.create(username='teststudent')
        user.save()
        s_i = StudentInfo(user=user)
        s_i.save()
        dem = Demsurv.objects.create(user=user)
        dem.sex = 'M'
        dem.age = '30'
        dem.language = 'English'
        dem.country = 'UK'
        dem.education = 'Postgraduate'
        dem.save()

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
        user = User.objects.get(username='teststudent')
        s_i = StudentInfo.objects.get(user=user)
        Demsurv.objects.get(user=user)
        e = Experiment.objects.get(name='test')

        #Student Bids
        e.students.add(user)
        s_i.bidexpr.add(e)
        e.save()
        s_i.save()

        #Check bid
        e.students.get(id=user.id)
        s_i.bidexpr.get(name=e.name)

        


