# Generated by Django 4.2.6 on 2023-11-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0012_alter_blog_repost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="repost",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
