# Generated by Django 2.1.2 on 2019-08-25 20:41

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0014_auto_20190821_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]