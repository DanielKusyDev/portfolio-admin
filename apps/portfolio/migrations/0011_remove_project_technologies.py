# Generated by Django 3.2.7 on 2021-09-29 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20210929_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technologies',
        ),
    ]
