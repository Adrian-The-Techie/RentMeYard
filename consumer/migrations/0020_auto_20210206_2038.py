# Generated by Django 3.1.2 on 2021-02-06 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0019_auto_20210206_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(default='dOlTMCndjsXAlo8XiFtHARoYDroW1I6v', max_length=255),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='url',
            field=models.CharField(default='tB1JHrCq4nFznij5EHWl3kNdhJbb33xy', max_length=255),
        ),
    ]
