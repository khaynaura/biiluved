# Generated by Django 5.1.1 on 2024-09-22 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_product_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="user",
        ),
    ]
