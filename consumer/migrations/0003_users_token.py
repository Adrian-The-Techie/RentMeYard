# Generated by Django 3.1.2 on 2020-11-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0002_users_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
