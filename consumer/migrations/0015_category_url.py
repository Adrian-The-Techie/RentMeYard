# Generated by Django 3.1.2 on 2020-12-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0014_auto_20201121_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(default='MFfFRcm4K0p1v1jmlln3H8RccAvINhCk', max_length=255),
        ),
    ]
