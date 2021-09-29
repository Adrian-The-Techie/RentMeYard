# Generated by Django 3.1.2 on 2021-02-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0022_auto_20210219_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(default='besUB7acgKwUzoNS9DZKjwQKDdguxd4E', max_length=255),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='url',
            field=models.CharField(default='cM1DozOFbJgPONTlEu0jVBEHw8Xo7kqL', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
