# Generated by Django 3.1.2 on 2020-12-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0015_category_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('url', models.CharField(default='WnUAFMUMtDacQVP18WrdnHHf9VviiNyY', max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(default='ppOrcPv4pLw2Aq1LWoE84vkX3CBlkND6', max_length=255),
        ),
    ]
