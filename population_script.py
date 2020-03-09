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

    expr2 = [
    {'name': 'Mathematical Study', 'details':
    '''
    This experiment will study what happens when you ask people to count grains
    of sand in various containers over the course of 14 days.
    ''',
    'price': '11', 'start_date': '05/05/20', 'end_date': '19/05/20',
    'num_req': '4', 'num_current': '0', 'age_req': '16',
    'lang_req': 'any', 'ed_req': 'none'},]

    expr3 = [
    {'name': 'Patience Test', 'details':
    '''
    This experiment involves watching Kevin Costner's 1997 film The Postman 40
    times in 3 days. At no point will the reason for this be explained to any
    of the participants.
    ''',
    'price': '14', 'start_date': '01/04/20', 'end_date': '04/04/20',
    'num_req': '8', 'num_current': '0', 'age_req': '18',
    'lang_req': 'English', 'ed_req': 'none'},]


    expr4 = [
    {'name': 'TikTok Test', 'details':
    '''
    This experiment will seek to answer the question: has anyone over the age
    of 50 heard of TikTok?
    ''',
    'price': '9', 'start_date': '15/05/20', 'end_date': '16/05/20',
    'num_req': '12', 'num_current': '0', 'age_req': '50',
    'lang_req': 'English', 'ed_req': 'none'},]

    expr5 = [
    {'name': 'Perseverence Study', 'details':
    '''
    This experiment involves writing out every times table from 1 to 100 using
    a quill, ink and parchment. And the end of each day, researchers will feed
    the finished work into a shredder.
    ''',
    'price': '20', 'start_date': '01/04/20', 'end_date': '04/04/20',
    'num_req': '8', 'num_current': '0', 'age_req': '18',
    'lang_req': 'English', 'ed_req': 'none'},]
