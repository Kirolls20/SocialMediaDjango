# Generated by Django 4.2.6 on 2023-11-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0013_alter_blog_repost"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="reposted",
            field=models.BooleanField(default=False),
        ),
    ]