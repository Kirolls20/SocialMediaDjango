# Generated by Django 4.2.6 on 2023-10-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="link",
            field=models.URLField(default="exapmle@.com", max_length=255),
        ),
        migrations.AddField(
            model_name="user",
            name="social_media_chocies",
            field=models.CharField(
                blank=True,
                choices=[("facebook", "facebook"), ("instagram", "instagram"), ("X", "X")],
                max_length=28,
                null=True,
            ),
        ),
    ]
