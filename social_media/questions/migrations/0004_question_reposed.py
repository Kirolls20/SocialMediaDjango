# Generated by Django 4.2.6 on 2023-11-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questions", "0003_rename_repost_question_repost_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="reposed",
            field=models.BooleanField(default=False),
        ),
    ]