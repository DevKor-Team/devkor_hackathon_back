# Generated by Django 3.2.1 on 2021-08-22 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("demo", "0009_alter_demo_thumbnail"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="demoimage",
            name="demo",
        ),
    ]
