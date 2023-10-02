# Generated by Django 4.2.5 on 2023-10-02 09:06

from django.db import migrations


def create_data(apps, schema_editor):
    Category = apps.get_model('expenses', 'Category')
    DEFAULT_CATEGORIES = ["rent", "bills", "groceries", "tobacco", "eating out", "transport", "gifts", "extras"]

    for cat in DEFAULT_CATEGORIES:
        Category(name=cat).save()


class Migration(migrations.Migration):
    dependencies = [
        ("expenses", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
