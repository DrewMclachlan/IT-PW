import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'participants_wanted.settings')

import django
django.setup()

from rango.models import Experiment, ExprProfile

def populate():

    expr1 = [
    {'name': 'Boredom Test', 'details':
    '''
    This experiment will test the human ability to endure extreme boredom.
    Participants will have to watch Kevin Costner's 1997 film The Postman 20
    times in 2 days.
    ''',
    'price': '10', 'start_date': '29/03/20', 'end_date': '13/04/20',
    'num_req': '8', 'num_current': '0', 'age_req': '18',
    'lang_req': 'English', 'ed_req': 'none'},]




    # name = models.CharField(unique=True, max_length=128)
    # details = models.CharField(max_length=128)
    # price = models.IntegerField(default=0)
    # start_date = models.DateField()
    # end_date = models.DateField()
    # num_req = models.IntegerField(default=0)
    # num_current = models.IntegerField(default=0)
    # age_req = models.IntegerField(default=0)
    # lang_req = models.CharField(max_length=128)
    # ed_req = models.CharField(max_length=128)
