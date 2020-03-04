# Generated by Django 2.1.5 on 2020-03-04 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('details', models.CharField(max_length=128)),
                ('price', models.IntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('num_req', models.IntegerField(default=0)),
                ('num_current', models.IntegerField(default=0)),
                ('age_req', models.IntegerField(default=0)),
                ('lang_req', models.CharField(max_length=128)),
                ('ed_req', models.CharField(max_length=128)),
                ('expr_full', models.BooleanField(default=False)),
                ('expr_done', models.BooleanField(default=False)),
                ('accepted', models.ManyToManyField(blank=True, related_name='accepted', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExprProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('school', models.CharField(max_length=128)),
                ('webpage', models.CharField(blank=True, max_length=128)),
                ('schoolemail', models.CharField(max_length=128)),
                ('publicnumber', models.CharField(max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
