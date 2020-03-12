import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'participants_wanted.settings')
import django
django.setup()
from django.contrib.auth.models import User
from experimenter.models import ExprProfile


def add_expr(expr, exprp):
    u = User.objects.create()
    u.username = expr['username']
    u.email = expr['email']
    u.password = expr['password']
    u.save()
    ep = ExprProfile.objects.create(user=u)
    ep.title = exprp['title']
    ep.school = exprp['school']
    ep.webpage = exprp['webpage']
    ep.schoolemail = exprp['schoolemail']
    ep.publicnumber = exprp['publicnumber']
    ep.save()




expr = [{
    'username':'expr',
    'email':'expr@account.com',
    'password': 'test'
}]

expr_profile = [{
    'title':'Prof',
    'school':'CompSci',
    'webpage':'gu.com',
    'schoolemail':'expr@compsci.gu.com',
    'publicnumber':'0000000'
}]

add_expr(expr[0], expr_profile[0])
