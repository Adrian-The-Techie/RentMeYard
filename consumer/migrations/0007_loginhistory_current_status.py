# Generated by Django 3.1.2 on 2020-11-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0006_loginhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginhistory',
            name='current_status',
            field=models.BooleanField(default=1),
        ),
    ]
