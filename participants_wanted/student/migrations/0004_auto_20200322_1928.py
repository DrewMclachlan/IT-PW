# Generated by Django 2.1.5 on 2020-03-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200322_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demsurv',
            name='education',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'School'), (2, 'College'), (3, 'Undergraduate'), (4, 'Postgraduate')], default=0),
        ),
    ]
