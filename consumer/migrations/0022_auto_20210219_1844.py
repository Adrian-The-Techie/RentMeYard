# Generated by Django 3.1.2 on 2021-02-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0021_auto_20210206_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='flagged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(default='e6b3atX2NU0l9VICRqHFHR7QDbJrGSa0', max_length=255),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='url',
            field=models.CharField(default='022kVz7Z08wrbpLoTAED2Qxh9sly0Noc', max_length=255),
        ),
    ]
