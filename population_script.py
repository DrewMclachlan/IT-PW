import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'participants_wanted.settings')

import django
django.setup()

from rango.models import Experiment

def populate():

    expr1 = [
    {'name': 'Boredom Test', 'details':
    '''
    This experiment will test the human ability to endure extreme boredom.
    Participants will have to watch Kevin Costner's 1997 film The Postman 16
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
    {'name': 'TikTok Test', 'details':
    '''
    This experiment will seek to answer the question: has anyone over the age
    of 50 heard of TikTok?
    ''',
    'price': '9', 'start_date': '15/05/20', 'end_date': '16/05/20',
    'num_req': '12', 'num_current': '0', 'age_req': '50',
    'lang_req': 'English', 'ed_req': 'none'},]


    expr4 = [
    {'name': 'Patience Test', 'details':
    '''
    This experiment involves watching Kevin Costner's 1995 film Waterworld 21
    times in 3 days. At no point will the reason for this be explained to any
    of the participants.
    ''',
    'price': '14', 'start_date': '01/04/20', 'end_date': '04/04/20',
    'num_req': '8', 'num_current': '0', 'age_req': '18',
    'lang_req': 'English', 'ed_req': 'none'},]

    expr5 = [
    {'name': 'Perseverence Study', 'details':
    '''
    This experiment involves writing out every times table from 1 to 100 using
    a quill, ink and parchment. And the end of each day, researchers will feed
    the finished work into a shredder.
    ''',
    'price': '20', 'start_date': '03/04/20', 'end_date': '10/04/20',
    'num_req': '8', 'num_current': '0', 'age_req': '18',
    'lang_req': 'English', 'ed_req': 'none'},]

    expr6 = [
    {'name': 'Confidence Test', 'details':
    '''
    This experiment involves being asked a series of routine questions on a
    range of different subjects. Each time a participant answers, they will
    be told they're wrong and a loud horn will sound. After 7 days, researchers
    will measure the participants' confidence levels.
    ''',
    'price': '9', 'start_date': '16/04/20', 'end_date': '23/04/20',
    'num_req': '5', 'num_current': '0', 'age_req': '18',
    'lang_req': 'English', 'ed_req': 'none'},]

    exprs = {
    'expr1': {'experiments': expr1, 'name': name, 'details': details,
    'price': price, 'start_date': start_date, 'end_date': end_date,
    'num_req': num_req, 'num_current': num_current, 'age_req': age_req,
    'lang_req': lang_req, 'ed_req': ed_req},

    'expr2': {'experiments': expr2, 'name': name, 'details': details,
    'price': price, 'start_date': start_date, 'end_date': end_date,
    'num_req': num_req, 'num_current': num_current, 'age_req': age_req,
    'lang_req': lang_req, 'ed_req': ed_req},

    'expr3': {'experiments': expr3, 'name': name, 'details': details,
    'price': price, 'start_date': start_date, 'end_date': end_date,
    'num_req': num_req, 'num_current': num_current, 'age_req': age_req,
    'lang_req': lang_req, 'ed_req': ed_req},

    'expr4': {'experiments': expr4, 'name': name, 'details': details,
    'price': price, 'start_date': start_date, 'end_date': end_date,
    'num_req': num_req, 'num_current': num_current, 'age_req': age_req,
    'lang_req': lang_req, 'ed_req': ed_req},

    'expr5': {'experiments': expr5, 'name': name, 'details': details,
    'price': price, 'start_date': start_date, 'end_date': end_date,
    'num_req': num_req, 'num_current': num_current, 'age_req': age_req,
    'lang_req': lang_req, 'ed_req': ed_req},

    'expr6': {'experiments': expr6, 'name': name, 'details': details,
    'price': price, 'start_date': start_date, 'end_date': end_date,
    'num_req': num_req, 'num_current': num_current, 'age_req': age_req,
    'lang_req': lang_req, 'ed_req': ed_req},

    }

    for experiment, expr_data in exprs.items():
        e = add_expr_name(experiment)
        for e in expr_data['experiments']:
        add_expr(experiment, expr_data['name'], expr_data['details'],
        expr_data['price'],expr_data['start_date'],expr_data['end_date'],
        expr_data['num_req'],expr_data['num_current'],expr_data['age_req'],
        expr_data['lang_req'],expr_data['ed_req'])


def add_expr_name(name):
    e = Category.objects.get_or_create(name=name)[0]
    e.save()
    return e


def add_expr(experiment, name, price=0, start_date, end_date, num_req,
num_current, age_req=0, lang_req, ed_req):
    e = Experiment.objects.get_or_create(experiment=experiment, name=name,
    details=details, price=price,start_date=start_date,end_date=end_date,
    num_req=num_req, num_current=num_current, age_req=age_req,
    lang_req=lang_req, ed_req=ed_req)[0]
    e.name=name
    e.details=details
    e.price=price
    e.start_date=start_date
    e.end_date=end_date
    e.num_req=num_req
    e.num_current=num_current
    e.age_req=age_req
    e.lang_req=lang_req
    e.ed_req=ed_req
    e.save()
    return e


if __name__ == '__main__':
    print('Starting the population script...')
    populate()
