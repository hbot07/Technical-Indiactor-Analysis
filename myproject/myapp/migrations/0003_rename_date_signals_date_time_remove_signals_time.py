# Generated by Django 5.0.6 on 2024-06-17 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_signals"),
    ]

    operations = [
        migrations.RenameField(
            model_name="signals",
            old_name="date",
            new_name="date_time",
        ),
        migrations.RemoveField(
            model_name="signals",
            name="time",
        ),
    ]
