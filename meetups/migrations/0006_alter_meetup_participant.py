# Generated by Django 4.2.7 on 2024-11-30 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meetups", "0005_meetup_date_meetup_organizers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meetup",
            name="participant",
            field=models.ManyToManyField(blank=True, to="meetups.participant"),
        ),
    ]
