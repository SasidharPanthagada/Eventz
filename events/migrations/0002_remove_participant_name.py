# Generated by Django 3.2.6 on 2021-09-12 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='name',
        ),
    ]
