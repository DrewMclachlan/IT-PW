from django.contrib import admin
from .models import Experiment, Demsurv, StudentInfo

admin.site.register(Demsurv)
admin.site.register(Experiment)
admin.site.register(StudentInfo)
# Register your models here.
