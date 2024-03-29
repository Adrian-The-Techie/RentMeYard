# Generated by Django 3.1.2 on 2020-11-08 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0008_category_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(default='uploads/thumbnail.png', upload_to='uploads/services/')),
                ('name', models.CharField(max_length=255)),
                ('normal_rate', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('negotiable', models.BooleanField(default=False)),
                ('has_packages', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consumer.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=255)),
                ('rate', models.CharField(max_length=255)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consumer.services')),
            ],
        ),
    ]
