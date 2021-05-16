# Generated by Django 3.2.1 on 2021-05-16 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Position",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, unique=True)),
                ("token", models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="position",
            field=models.ManyToManyField(
                related_name="user_set", to="accounts.Position"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="team",
            field=models.ManyToManyField(related_name="user_set", to="accounts.Team"),
        ),
    ]