# Generated by Django 3.2.1 on 2021-07-21 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0006_team_leader"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="leader",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="leader_teams",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
