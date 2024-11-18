# Generated by Django 4.2.7 on 2024-11-18 03:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meetups", "0004_participant_meetup_participant"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetup",
            name="date",
            field=models.DateField(default="2024-10-10"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="meetup",
            name="organizers",
            field=models.EmailField(default="test@test.com", max_length=200),
            preserve_default=False,
        ),
    ]
