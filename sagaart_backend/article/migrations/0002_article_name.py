# Generated by Django 5.0 on 2024-07-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="name",
            field=models.CharField(blank=True, verbose_name="Краткое описание"),
        ),
    ]