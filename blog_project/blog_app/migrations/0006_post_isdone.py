# Generated by Django 4.2.5 on 2023-09-19 00:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog_app", "0005_admin_info"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="isDone",
            field=models.CharField(default="Y", max_length=1),
        ),
    ]