# Generated by Django 3.2.1 on 2021-08-19 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("demo", "0005_alter_demo_team"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="demo",
            options={"ordering": ["-created_at"]},
        ),
    ]
