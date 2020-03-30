import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'participants_wanted.settings')
import django
django.setup()
from django.contrib.auth.models import User

from experimenter.models import Experiment, ExprProfile


def set_expr():
    expr_profile = [{
        'title': 'Prof',
        'school': 'CompSci',
        'webpage': 'gu.com',
        'schoolemail': 'expr@compsci.gu.com',
        'publicnumber': '0000000'
    }]
    add_user(expr_profile[0])

def populate():
    li = [
    {'name': 'Boredom Test',
    'details':
    "This experiment will test the human ability to endure extreme boredom. " +
    "Participants will have to watch Kevin Costner's 1997 film The Postman 16 " +
    "times in 2 days. TIMES: Flexible, Nights pref.",
    'price': '10',
    'start_date': '2020-04-29',
    'end_date': '2020-04-06',
    'num_req': '8',
     'num_current': '0',
     'age_req': '18',
    'lang_req': 'English',
     'ed_req': 'College'},

     {'name': 'Wonderpill Trial',
     'details': "Participants in this study will be testing the " +
    "latest super-drug to come out of SKYNET laboratories. Just one " +
    "pill per day will improve your confidence, your ability to " +
    "process and follow detailed instructions, and lower your anxiety. "+
    "Try this drug trial for 2 weeks and we promise you'll love the " +
    "new you just as much as you love the air, the sun, and the robots. " +
    "TIMES: Week Days.",
    'price': '25',
     'start_date': '2020-06-06',
     'end_date': '2020-06-20',
    'num_req': '50',
     'num_current': '0',
     'age_req': '18',
    'lang_req': 'English',
     'ed_req': 'College'},


    {'name': 'Dloo-Xion5 Trial',
     'details': "This drug trial will be testing the pill form of " +
    "Dloo-Xion5, a powerful formula for chemically enhancing confidence. " +
    "Participants will be asked to complete a self-evaluation form at the " +
    "start and end of each day, in-between doses of Dloo-Xion5. Please be " +
    "aware that long term use of Dloo-Xion5 may make you a bit of a t**t. " +
    "TIMES: Flexible.",
    'price': '15',
     'start_date': '2020-05-21',
     'end_date': '2020-06-08',
    'num_req': '20',
     'num_current': '0',
     'age_req': '18',
    'lang_req': 'English',
     'ed_req': 'College'},


    {'name': 'Mathematical Study',
     'details':
    "This experiment will study what happens when you ask people to count " +
    "grains of sand in various containers over the course of 14 days." +
    "TIMES: Flexible.",
    'price': '11',
    'start_date': '2020-05-05',
     'end_date': '2020-05-10',
    'num_req': '4',
     'num_current': '0',
     'age_req': '16',
    'lang_req': 'English',
     'ed_req': 'College'},

    {'name': 'TikTok Test',
     'details': "This experiment will seek to answer the question: has anyone "+
     "over the age of 50 heard of TikTok? TIMES: Weekend Days.",
    'price': '9',
     'start_date': '2020-05-15',
     'end_date': '2020-05-16',
    'num_req': '12',
     'num_current': '0',
     'age_req': '50',
    'lang_req': 'English',
     'ed_req': 'School'},


    {'name': 'Patience Test',
     'details': "This experiment involves watching Kevin Costner's 1995 film " +
     "Waterworld 21 times in 3 days. At no point will the reason for this be " +
     "explained to any of the participants. TIMES: Week Nights.",
    'price': '14',
     'start_date': '2020-04-01',
     'end_date': '2020-04-04',
    'num_req': '8',
     'num_current': '0',
     'age_req': '18',
    'lang_req': 'English',
     'ed_req': 'School'},


    {'name': 'Perseverence Study',
     'details':"This experiment involves writing out every times table from " +
     "1 to 100 using a quill, ink and parchment. And the end of each day, " +
     "researchers will feed the finished work into a shredder. TIMES: Week Days.",
    'price': '20',
     'start_date': '2020-04-03',
     'end_date': '2020-04-04',
    'num_req': '8',
     'num_current': '0',
     'age_req': '18',
    'lang_req': 'English',
     'ed_req': 'School'},


    {'name': 'Confidence Test',
     'details': "This experiment involves being asked a series of routine " +
     "questions on a range of different subjects. Each time a participant " +
     "answers, they will be told they're wrong and a loud horn will sound. " +
     "After 7 days, researchers will measure the participants' confidence levels. " +
     "TIMES: Week Days or Nights.",
    'price': '9',
     'start_date': '2020-04-16',
     'end_date': '2020-04-23',
    'num_req': '5',
     'num_current': '0',
     'age_req': '18',
    'lang_req': 'English',
     'ed_req': 'School'},

    {'name': 'Movie Study',
     'details': "This study was created after an argument between two "+
     "researchers on a prior study involving films. To settle this "+
     "argument, participants in the Movie Study will be shown each "+
     "researcher's favourite film and asked to pick the best one. " +
     "TIMES: Week nights.",
    'price': '8',
     'start_date': '2020-05-19',
     'end_date': '2020-05-20',
    'num_req': '20',
     'num_current': '0',
     'age_req': '18',
    'lang_req': 'English',
     'ed_req': 'School'},

    {'name': 'Alcohol Study',
     'details': "Participants in this study will be given two "+
     "single-question IQ tests. In-between, they will spend six hours "+
     "drinking alcohol. Researchers will measure the participants' "+
     "expected drop in IQ by asking them whether they'd like to eat "+
     "a four-day-old kebab. TIMES: Weekend Nights.",
    'price': '10',
     'start_date': '2020-06-05',
     'end_date': '2020-06-06',
    'num_req': '7',
     'num_current': '0',
     'age_req': '18',
    'lang_req': 'English',
     'ed_req': 'College'},

    {'name': 'Parenthood Study',
     'details': "This study will involve the particpants being " +
     "tested on their suitablity for parenthood. Each partipant will " +
     "spend three hours a day trying to explain a series of important " +
     "life lessons to a child while being asked 'why?' sixteen thousand " +
     "times. Anyone who lasts the full five days will receive a bonus. " +
     "TIMES: Week Days.",
    'price': '15',
     'start_date': '2020-05-20',
     'end_date': '2020-05-24',
    'num_req': '10',
     'num_current': '0',
     'age_req': '18',
    'lang_req': 'English',
     'ed_req': 'College'},
    ]

    return li




def add_user(exprp):
    u = User.objects.create_user('expr', password='test')
    u
    u.save()
    ep = ExprProfile.objects.create(user=u)
    ep.title = exprp['title']
    ep.school = exprp['school']
    ep.webpage = exprp['webpage']
    ep.schoolemail = exprp['schoolemail']
    ep.publicnumber = exprp['publicnumber']
    ep.save()


def add_expr(expr):
    user = User.objects.get(username='expr')
    e = Experiment.objects.create(user=user, start_date=expr['start_date'], end_date=expr['end_date'])
    e.name = expr['name']
    e.details = expr['details']
    e.price = expr['price']
    e.num_req = expr['num_req']
    e.num_current = expr['num_current']
    e.age_req = expr['age_req']
    e.lang_req = expr['lang_req']
    e.ed_req = expr['ed_req']
    e.save()




if __name__ == '__main__':
    set_expr()
    li = populate()
    for i in range(0, len(li)):
        add_expr(li[i])
