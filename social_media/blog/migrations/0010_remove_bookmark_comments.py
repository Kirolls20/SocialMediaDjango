# Generated by Django 4.2.6 on 2023-11-05 09:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_alter_bookmark_unique_together"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookmark",
            name="comments",
        ),
    ]
