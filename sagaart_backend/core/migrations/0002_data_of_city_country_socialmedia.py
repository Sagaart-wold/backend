# Generated by Django 5.0 on 2024-06-30 18:27

from django.db import migrations


def add_data(apps, schema_editor):
    Country = apps.get_model("core", "Country")
    data = [
        {
            'id': 1,
            'name': 'Россия',
        },
        {
            'id': 2,
            'name': 'Франция'
        },
        {
            'id': 3,
            'name': 'Италия'
        },
        {
            'id': 4,
            'name': 'Белорусь'
        },
    ]
    for row in data:
        Country.objects.update_or_create(**row)

    City = apps.get_model("core", "City")
    obj_country1 = Country.objects.get(id=1)
    City.objects.get_or_create(
        id=1,
        name='Москва',
        country=obj_country1,
    )

    City.objects.get_or_create(
        id=2,
        name='Санкт-Петербург',
        country=obj_country1,
    )

    City.objects.get_or_create(
        id=3,
        name='Сочи',
        country=obj_country1,
    )

    obj_country2 = Country.objects.get(id=2)
    City.objects.get_or_create(
        id=4,
        name='Париж',
        country=obj_country2,
    )

    obj_country3 = Country.objects.get(id=3)
    City.objects.get_or_create(
        id=5,
        name='Рим',
        country=obj_country3,
    )

    obj_country4 = Country.objects.get(id=4)
    City.objects.get_or_create(
        id=6,
        name='Минск',
        country=obj_country4,
    )

    SocialMedia = apps.get_model("core", "SocialMedia")
    data = [
        {
            'id': 1,
            'name': 'Telegram',
        },
        {
            'id': 2,
            'name': 'VK'
        },
    ]
    for row in data:
        SocialMedia.objects.update_or_create(**row)


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]