# Generated by Django 3.1.2 on 2020-11-07 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0007_loginhistory_current_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(default='uploads/thumbnail.png', upload_to='uploads/'),
        ),
    ]
