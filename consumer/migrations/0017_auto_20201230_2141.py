# Generated by Django 3.1.2 on 2020-12-30 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0016_auto_20201214_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(default='vrBQvNx8F4qci5Qva9aG7PVcFUcroV6Y', max_length=255),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='url',
            field=models.CharField(default='sC9jxpMYeiwoN11rYx8TjKncEV0Rnxn0', max_length=255),
        ),
    ]
