# Generated by Django 3.2.1 on 2021-08-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_img",
            field=models.ImageField(blank=True, upload_to="profile_img"),
        ),
    ]
