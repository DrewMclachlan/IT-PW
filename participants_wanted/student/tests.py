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

        e2 = Experiment.objects.create(user=user, start_date=date.today(), end_date=date.today())
        e2.name = 'test2'
        e2.details = 'deets'
        e2.price = 1
        e2.num_req = 1
        e2.num_current = 0
        e2.age_req = 17
        e2.lang_req = 'None'
        e2.ed_req = 'None'
        e2.save()

    def test(self):
        user = User.objects.get(username='teststudent')
        s_i = StudentInfo.objects.get(user=user)
        Demsurv.objects.get(user=user)
        e = Experiment.objects.get(name='test')
        e2 = Experiment.objects.get(name='test')

        #Student Bids
        e.students.add(user)
        s_i.bidexpr.add(e)
        e.save()
        s_i.save()

        #Check bid
        e.students.get(id=user.id)
        s_i.bidexpr.get(name=e.name)

        #Accept Bid
        e.students.remove(user)
        e.accepted.add(user)
        s_i.currentexpr.add(e)
        s_i.bidexpr.remove(e)
        s_i.save()
        e.save()

        #check
        s_i.currentexpr.get(name=e.name)

        #New Bid
        e.students.add(user)
        s_i.bidexpr.add(e)
        e.save()
        s_i.save()

        #Decline Bid
        e2.students.remove(user)
        s_i.bidexpr.remove(e2)
        s_i.decexpr.add(e2)
        s_i.save()
        e2.save()

        #check
        s_i.decexpr.get(name=e2.name)



        


