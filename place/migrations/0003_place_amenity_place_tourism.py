# Generated by Django 4.0.6 on 2022-09-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_alter_place_created_by_alter_place_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='amenity',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='place',
            name='tourism',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
