# Generated by Django 3.2.7 on 2021-09-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_project_technologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(limit_choices_to={'brand__name': 'TECH'}, related_name='projects', to='portfolio.Brand'),
        ),
    ]
